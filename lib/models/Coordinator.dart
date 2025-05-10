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

  '''
  Initializes the User as a Coordinator of a certain club that will be set later by setting isCoordinator to true
  '''
  void setCoordinator() {
    if (!isCoordinator) {
      isCoordinator = true;
    } else {
      print("You are already a coordinator.");
    }
  }

  '''
  This function assigns a club for the Coordinator to have permission to coordinate 

  Parameter(s): 
  club: A Club object to determine the club that the Coordinator can access and manage
  '''
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

  '''
  Adds an event to a club hosted by the coordinator and to the coordinator's list of events

  Parameter(s): 
  event: an Event object that will be added to this Coordinator's club 
  club: the intended club that the event will be associated with
  '''
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
  
  '''
  Ends an event from a club hosted by the coordinator by removing it from the club
  and the Coordinator's list of managed events

  Parameter(s): 
  event: an Event object that will be terminated from this Coordinator's club 
  club: the intended club that the event will be no longer be associated with
  '''
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

  '''
  Demotes the User from their role as a Coordinator of a certain club
  '''
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

  '''
  Getter for the Coordinator's currently managed events
  '''
  List<Event> getManagedEvents() {
    return managedEvents;
  }

  '''
  Getter for the clubs that the Coordinator is an admin for
  '''
  List<Club> getManagedClubs() {
    return coordinatedClubs;
  }

  '''
  Relinquish admin permissions from the club if it is one that the Coordinator coordinates
  The Coordinator remains as a normal member of this club, just not an admin.

  Paramaters:
  club - Club that you no longer want to be in charge of
  '''
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

