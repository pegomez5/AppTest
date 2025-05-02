import 'event.dart';

class Club {

  // Club Variables //
  int id;
  String name;
  String updateDate;
  String desc;
  List<Event> events;
  List<String> memberIDs;
  List<String> adminIDs;

  // Constructor //
  Club({
    required this.id,
    required this.name,
    required this.updateDate,
    this.desc = '',
    this.events = const [],
    this.memberIDs = const [],
    this.adminIDs = const []
});

  // Create custom ID (Thanks Pedro) //
  int _createID(String name, String updateDate){
    String hash = '$name$updateDate';

    return hash.hashCode;
  }

  // Change club name and date updated
  void updateClub(String? name, String? updateDate){
    if (name != null){
      this.name = name;
    }
    if (updateDate != null){
      this.updateDate = updateDate;
    }
    // Recalculate ID
    this.id = _createID(this.name, this.updateDate);
    // (Make sure ID doesn't already exist)

  }

  // Create a club //
  Club createClub(String name, String updateDate){

    int clubID = _createID(name, updateDate); // Get ID

    return Club(id:clubID, name:name, updateDate:updateDate);
  }

  int getMemberCount(){
    return memberIDs.length;
  }

  int getAdminCount(){
    return adminIDs.length;
  }

  int getEventCount(){
    return events.length;
  }

  List<String> getMemberList(){
    return memberIDs;
  }

  List<String> getAdminList(){
    return adminIDs;
  }

  List<Event> getEventList(){
    return events;
  }

  void addAdmin(userID){
    if(!memberIDs.contains(userID)){
      memberIDs.add(userID);
      adminIDs.add(userID);

    } else if(!adminIDs.contains(userID)){
      adminIDs.add(userID);

    } else {
      print("User already an admin!");
    }
  }

  void removeAdmin(userID){
    if(adminIDs.contains(userID)){
      adminIDs.remove(userID);
    } else {
      print("User not an admin!");
    }
  }

  void addMember(userID){
    if(!memberIDs.contains(userID)){
      memberIDs.add(userID);
    } else {
      print("User already a member!");
    }
  }

  void removeMember(userID){
    if(adminIDs.contains(userID)){
      adminIDs.remove(userID);
      memberIDs.remove(userID);
    } else if(memberIDs.contains(userID)){
      memberIDs.remove(userID);
    } else {
      print("User not a member!");
    }
  }

  void changeDesc(String newDesc){
    desc = newDesc;
  }

  void addEvent(Event event){
    if(!events.contains(event)){
      events.add(event); // Might change this to just storing eventID
    } else {
      print("Event already exists!"); // If storing eventID, this won't be an issue
    }
  }

  void removeEvent(Event event){
    if(events.contains(event)){
      events.remove(event);
    } else {
      print("Event doesn't exist!");
    }
  }

  bool isAdmin(userID){
    return adminIDs.contains(userID);
  }

  bool isMember(userID){
    return memberIDs.contains(userID);
  }




}