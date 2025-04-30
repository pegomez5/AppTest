class Event {
  // ------------- Create event variables -------------
  int id;
  String date;
  String location;
  Event_Coordinator coordinator;

  // ------------- Constructor ------------- 
  Event(this.id, this.date, this.location);

  // ------------- Methods -------------
  // Create event ID
  int _ev_create_id(String date, String location) {
    // Concatenate date & location for a unique hash
    String hash = '$date$location';
    // Return hashcode of string (thanks dart for builtin hash)
    return hash.hashCode;
  }

  // Change event date/location
  void ev_update_fields(String? date, String? location){
    // If date, change this.date to date
    // if location, tomato tomāto
    if (date != null){ this.date = date; }
    if (location != null){ this.location = location; }
    // Recalculate ID
    this.id = _ev_create_id(this.date, this.location);
    // Later we'll have to validate the ID
    // (Make sure ID doesn't already exist)

  }
    
  // Create event
  // - Should return an event instance 
  Event ev_create_event(String date, String location){
    return Event(_ev_create_id(date, location), date, location);
  }

  // 
}
