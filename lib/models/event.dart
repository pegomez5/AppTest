class Event {
  // ------------- Create event variables -------------
  String date;
  String location;
  Event_Coordinator coordinator;
  int? id;
  string? desc;

  // ------------- Constructor ------------- 
  Event({
    required this.date,
    required this.location,
    required this.coordinator,
    this.id = null,
    this.desc = ''
  });

  // ------------- Methods -------------
  // Create event ID
  int _create_id(String date, String location) {
    // Concatenate date & location for a unique hash
    String hash = '$date$location';
    // Return hashcode of string (thanks dart for builtin hash)
    return hash.hashCode;
  }

  // Change event date/location
  void updateEvent(String date, String location){
    this.date = date;
    this.location = location;
    // Recalculate ID
    this.id = _create_id(this.date, this.location);
  }
}


