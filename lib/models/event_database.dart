import 'package:cloud_firestore/cloud_firestore.dart';
import 'event.dart';

class EventDatabase {
    static final EventDatabase instance = EventDatabase._init();
    final FirebaseFirestore _firestore = FirebaseFirestore.instance;

    EventDatabase._init();

    /// Add (insert) an event to the "events" collection
    Future<void> insertEvent({ required int date, required String location,
            required String coordinator, required int id }) async {
 
        if (await isIdInDatabase(id)) {
            throw Exception('Event with ID $id already exists.');
        }
        await _firestore.collection('events').add({
                'date': date,
                'location': location,
                'coordinator': coordinator,
                'id': id,
                'timestamp': FieldValue.serverTimestamp(), // optional: for sorting
                });
    }

    /// Delete an event by its ID
    Future<void> deleteEvent(int id) async {
        final snapshot = await _firestore
            .collection('events')
            .where('id', isEqualTo: id)
            .get();

        if (snapshot.docs.isNotEmpty) {
            await snapshot.docs.first.reference.delete();
        }
    }

    /// Get event by id
    Future<Event> getEventById(int id) async {
        final snapshot = await _firestore
            .collection('events')
            .where('id', isEqualTo: id)
            .get();

        if (snapshot.docs.isNotEmpty) {
            final doc = snapshot.docs.first;
            return Event(
                date: doc['date'],
                location: doc['location'],
                coordinator: doc['coordinator'],
                id: doc['id']
            );
        } else {
            throw Exception('Event with ID $id not found.');
        }
    }

    /// Fetch a list of events (List<Event>) from the db
    Future<List<Event>> getEvents() async {
        final snapshot = await _firestore.collection('events').get();
        /// Convert all of the documents to a list of Event objects
        list<Event> events = snapshot.docs.map((doc) {
            return Event(
                date: doc['date'],
                location: doc['location'],
                coordinator: doc['coordinator'],
                id: doc['id']
            );
        }).toList();
        return events;
    }
    
    /// Update an events date or location by its ID
    Future<void> updateEvent(Event ev, String? date, String? location) async {
        int oldid = ev.id;
        int newid = ev.updateEvent(date, location).id;

        /// If an event with newid exists, this event cant be updated
        if (await isIdInDatabase(newid)) {
            throw Exception('Event with ID $newid already exists.');
        }

        final snapshot = await _firestore
            .collection('events')
            .where('id', isEqualTo: oldid)
            .get();

        /// If the event exists in db, update it
        if (snapshot.docs.isNotEmpty) {
            final docRef = snapshot.docs.first.reference;
            await docRef.update({
                if (date != null) 'date': date,
                if (location != null) 'location': location,
                'id': newid,
            });
        }
    }

    /// Is Id in the database?
    Future<bool> isIdInDatabase(int id) async {
        final snapshot = await _firestore
            .collection('events')
            .where('id', isEqualTo: id)
            .get();

        return snapshot.docs.isNotEmpty;
    }


}
