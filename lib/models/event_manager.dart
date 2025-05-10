import 'event_database.dart';
import 'event.dart';

class EventManager {
    // ------------- Create event variables -------------
    EventDatabase eventDatabase = EventDatabase.instance;
    
    // ------------- Constructor ------------- 
    EventManager();
    
    // ------------- Methods -------------
    
    // Create event
    Event createEvent(String date, String location, Event_Coordinator coordinator, string? desc) {
        int id = '$date$location'.hashCode;
        ev = Event(
            date: date,
            location: location,
            coordinator: coordinator,
            id: id,
            desc: desc
        );
        if (eventDatabase.isIdInDatabase(id)) {
            throw Exception('Event with ID $id already exists.');
        }
        // Store ev in database
        eventDatabase.insertEvent(date, location, coordinator, id);
        // Return event object
        return ev;

    }

    // Delete Event
    void deleteEvent(Event event) {
        // Delete event from database
        eventDatabase.deleteEvent(event.id);
    }

    // Update Event
    void updateEvent(Event event, String? date, String? location) {
        // Update event in database
        eventDatabase.updateEvent(event, date, location);

    // Get event by ID
    Event getEventById(int id) {
        // Get event from database
        return eventDatabase.getEventById(id);
    }

    // Get Events list
    List<Event> getEvents(){
        // Get events from database
        return eventDatabase.getEvents();
    }
}

