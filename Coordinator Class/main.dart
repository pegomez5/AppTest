import 'user.dart';
import 'club.dart';
import 'event.dart';
import 'coordinator.dart';

void main() {
  final coordinator = Coordinator("Michael", "Connors", "mconnors", "mconnors@ursinus.edu", "password",true);

  print("User ID: ${coordinator.userId}");
  print("Is Coordinator: ${coordinator.isCoordinator}");


  var club = Club(
  id: 4, 
  name: 'hi',
  updateDate: 'hey',
  );

  final event = Event(5,"hi","there");

  //coordinator.setCoordinatedClub(club);  # bugs in Club code don't let my method work
  coordinator.hostEvent(event,club);

  print("ManagedEvents: ${coordinator.getManagedEvents()}");
  print("isCoordinator: ${coordinator.isCoordinator}");
  
}
