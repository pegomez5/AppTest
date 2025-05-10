import 'event.dart';
import 'club.dart';
import 'user.dart';

class Coordinator extends User {
  //bool isCoordinator = false;
  List<Club> coordinatedClubs = [];
  List<Event> managedEvents = [];
  //int userId = 0;

  Coordinator(String firstName, String lastName, String username, String email, String password, bool isCoordinator)
      : super(firstName: firstName, lastName: lastName, username: username,email: email,password: password,isCoordinator: true) {
    //coordinatedClubs = [];
    //managedEvents = [];
    //this.isCoordinator = true;
  }

  void setCoordinator() {
    if (!isCoordinator) {
      isCoordinator = true;
    } else {
      print("You are already a coordinator.");
    }
  }

  void setCoordinatedClub(Club club) {
    if (!club.isAdmin(this.userId)) {
      club.addAdmin(this.userId);
    } else {
      print("You are already an admin for this club.");
    }
    if (!coordinatedClubs.contains(club)) {
      coordinatedClubs.add(club);
    } else {
      print("This club is already in the list.");
    }
  }

  void hostEvent(Event event, Club club) {
    if (club.isAdmin(this.userId)) {
      if (!managedEvents.contains(event) && !club.getEventList().contains(event)) {
        managedEvents.add(event);
        club.addEvent(event);
      } else if (!managedEvents.contains(event) && club.getEventList().contains(event)) {
        managedEvents.add(event);
      } else if (managedEvents.contains(event) && !club.getEventList().contains(event)) {
        club.addEvent(event);
      }
    } else {
      print("Invalid Permissions! You are not an Admin for this club.");
    }
  }

  void endEvent(Event event, Club club) {
    if (club.isAdmin(this.userId)) {
      int index = coordinatedClubs.indexOf(club);
      if (managedEvents.contains(event) && coordinatedClubs[index].getEventList().contains(event)) {
        managedEvents.remove(event);
        coordinatedClubs[index].removeEvent(event);
      } else if (managedEvents.contains(event) && !coordinatedClubs[index].getEventList().contains(event)) {
        managedEvents.remove(event);
      } else if (!managedEvents.contains(event) && coordinatedClubs[index].getEventList().contains(event)) {
        coordinatedClubs[index].removeEvent(event);
      }
    } else {
      print("Invalid Permissions! You are not an Admin for this club.");
    }
  }

  void demote() {
    if (isCoordinator) {
      isCoordinator = false;
      for (var club in coordinatedClubs) {
        club.removeAdmin(this.userId);
      }
      managedEvents = [];
      coordinatedClubs = [];
    } else {
      print("You were not already a coordinator.");
    }
  }

  List<Event> getManagedEvents() {
    return managedEvents;
  }

  List<Club> getManagedClubs() {
    return coordinatedClubs;
  }

  void relegateAdmin(Club club) {
    if (club.isAdmin(this.userId)) {
      if (coordinatedClubs.contains(club)) {
        int index = coordinatedClubs.indexOf(club);
        coordinatedClubs.removeAt(index);
        club.removeAdmin(this.userId);
      } else {
        print("This club is not in your list!");
      }
    } else {
      print("Invalid Permissions! You are not an Admin for this club.");
    }
  }
}

