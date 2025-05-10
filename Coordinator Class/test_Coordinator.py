import pytest
from CoordinatorClass import *
from AllClasses import User,Event,Club # Replace file AllClasses with the respective three files

# Make sure the constructor is working as intended
def test_coordinator_creation():
    Michael = Coordinator("Michael", "Connors", "mconnors", "mconnors@ursinus.edu", "password", False)
    assert Michael.isCoordinator
    assert Michael.getManagedClubs() == []
    assert Michael.getManagedEvents() == []
    assert Michael in users

# Make sure the club is in coordinatedClubs and you are in the club's admin list.
def test_set_coordinated_club():
    Hannah = Coordinator("Hannah", "Jeffers", "hjeffers", "hjeffers@ursinus.edu", "password", True)
    club = Club("CS-375", "Software Engineering")

    Hannah.setCoordinatedClub(club)
    assert club in Hannah.getManagedClubs()
    assert Hannah._user_id in club.getAdminList()

# Make sure the club is not coordinated when the method is called for a second time
def test_set_same_coordinated_club(capsys):
    Hannah = Coordinator("Hannah", "Jeffers", "hjeffers", "hjeffers@ursinus.edu", "password", True)
    club = Club("CS-375", "Software Engineering")

    Hannah.setCoordinatedClub(club)

    Hannah.setCoordinatedClub(club)

    # The user should be told that this club is already being coordinated with this
    captured = capsys.readouterr()
    assert "This club is already in the list." in captured.out
    assert "You are already an admin for this club." in captured.out

# If a club is in your coordinatedClubs and you have admin perms, then relegating admin will remove the club from your
# coordinatedClubs list and remove your id from the club's admin list
def test_relegate_admin():
    Pat = Coordinator("Pat", "McManus", "pmcmanus", "pmcmanus@ursinus.edu", "password", False)
    club = Club("CS-375", "Software Engineering")
    Pat.setCoordinatedClub(club)

    Pat.relegateAdmin(club)
    assert club not in Pat.getManagedClubs()
    assert Pat._user_id not in club.getAdminList()

# When you are not an admin for a club, it should not be possible to take away admin status that doesn't exist
def test_relegate_admin_without_perms(capsys):
    Pat = Coordinator("Pat", "McManus", "pmcmanus", "pmcmanus@ursinus.edu", "password", False)
    club = Club("CS-375", "Software Engineering")
    Pat.setCoordinatedClub(club)

    Pat.relegateAdmin(club) # Initially take away perms

    Pat.relegateAdmin(club) # Now test if the method still works w/o those perms

    # The user should be told that they are not an Admin for the club
    captured = capsys.readouterr()
    assert "Invalid Permissions! You are not an Admin for this club." in captured.out

# While you may have admin permissions for this club, if for some reason it is not a part
# of your coordinatedClubs list, then we do not want to pop an element that doesn't exist
def test_relegate_admin_not_managed_club(capsys):
    Pat = Coordinator("Pat", "McManus", "pmcmanus", "pmcmanus@ursinus.edu", "password", False)
    club = Club("CS-375", "Software Engineering")
    Pat.setCoordinatedClub(club)

    Pat.coordinatedClubs.remove(club)

    Pat.relegateAdmin(club)
    # The user should be told that the club isn't in their list
    captured = capsys.readouterr()
    assert "This club is not in your list!" in captured.out

# General test of the host event where the event has not been touched at all yet, the intended output is for it
# to be in Coordinator's managedEvents and in the club's event list
def test_host_event():
    Pedro = Coordinator("Pedro", "Gomez", "pgomez", "pgomez@ursinus.edu", "password", True)
    club = Club("CS-375", "Software Engineering")
    event = Event("Project Presentation", "1:00 PM", 10, 5, 2025)

    Pedro.setCoordinatedClub(club)
    Pedro.hostEvent(event, club)

    assert event in Pedro.getManagedEvents()
    assert event in club.getEventList()

# Make sure that if the event is already assigned to a club, the coordinator still gets it
# added to their list of coordinated clubs
def test_host_event_already_in_club():
    Pedro = Coordinator("Pedro", "Gomez", "pgomez", "pgomez@ursinus.edu", "password", True)
    club = Club("CS-375", "Software Engineering")
    event = Event("Project Presentation", "1:00 PM", 10, 5, 2025)

    club.addEvent(event)

    Pedro.setCoordinatedClub(club)
    Pedro.hostEvent(event, club)

    assert event in Pedro.getManagedEvents()
    assert event in club.getEventList()

# if the event is already in the Coordinator's list of managedEvents, then we need to make
# sure it still gets assigned to the club's list of managed events as well
def test_host_event_already_being_managed():
    Pedro = Coordinator("Pedro", "Gomez", "pgomez", "pgomez@ursinus.edu", "password", True)
    club = Club("CS-375", "Software Engineering")
    event = Event("Project Presentation", "1:00 PM", 10, 5, 2025)

    Pedro.managedEvents.append(event)

    Pedro.setCoordinatedClub(club)
    Pedro.hostEvent(event, club)

    assert event in Pedro.getManagedEvents()
    assert event in club.getEventList()

# Without any admin permissions for the club, the event should not be added to 
# the club or the Coordinator's managedEvents
def test_host_event_without_perms(capsys):
    Pedro = Coordinator("Pedro", "Gomez", "pgomez", "pgomez@ursinus.edu", "password", True)
    club = Club("CS-375", "Software Engineering")
    event = Event("Project Presentation", "1:00 PM", 10, 5, 2025)


    Pedro.setCoordinatedClub(club)

    Pedro.demote() # Take away perms

    Pedro.hostEvent(event, club)

    # The user should be told that they are not an Admin for the club
    captured = capsys.readouterr()
    assert "Invalid Permissions! You are not an Admin for this club." in captured.out

# Test to see if an active event that is in the Coordinator's managedEvents and in the club's clubEvents
# will be removed from both upon calling this method
def test_end_event():
    Matt = Coordinator("Matthew", "Latta", "mlatta", "mlatta@ursinus.edu", "password", False)
    club = Club("CS-375", "Software Engineering")
    event = Event("Project Presentation", "1:00 PM", 10, 5, 2025)

    Matt.setCoordinatedClub(club)
    Matt.hostEvent(event, club)
    Matt.endEvent(event, club)

    assert event not in Matt.getManagedEvents()
    assert event not in club.getEventList()

# If the event is not being managed by the Coordinator anymore, but they are an admin for the club,
# they should still have permissions to remove the event from the club's event list.
def test_end_event_not_managed():
    Matt = Coordinator("Matthew", "Latta", "mlatta", "mlatta@ursinus.edu", "password", False)
    club = Club("CS-375", "Software Engineering")
    event = Event("Project Presentation", "1:00 PM", 10, 5, 2025)

    Matt.setCoordinatedClub(club)
    Matt.hostEvent(event, club)

    Matt.managedEvents.remove(event)

    Matt.endEvent(event, club)

    assert event not in Matt.getManagedEvents()
    assert event not in club.getEventList()

# If an event does not exist for a club but still remains in the Coordinator's managedEvents,
# then this should be removed accordingly
def test_end_event_not_in_club():
    Matt = Coordinator("Matthew", "Latta", "mlatta", "mlatta@ursinus.edu", "password", False)
    club = Club("CS-375", "Software Engineering")
    event = Event("Project Presentation", "1:00 PM", 10, 5, 2025)

    Matt.setCoordinatedClub(club)
    Matt.hostEvent(event, club)

    club.removeEvent(event)

    Matt.endEvent(event, club)

    assert event not in Matt.getManagedEvents()
    assert event not in club.getEventList()

# Without any admin permissions for this club, you should not be able to remove an event
# from the club or your own managedEvents list.
def test_end_event_without_perms(capsys):
    Pedro = Coordinator("Pedro", "Gomez", "pgomez", "pgomez@ursinus.edu", "password", True)
    club = Club("CS-375", "Software Engineering")
    event = Event("Project Presentation", "1:00 PM", 10, 5, 2025)


    Pedro.setCoordinatedClub(club)
    Pedro.hostEvent(event, club)
    
    Pedro.demote() # Take away perms

    Pedro.endEvent(event,club)

    # The user should be told that they are not an Admin for the club
    captured = capsys.readouterr()
    assert "Invalid Permissions! You are not an Admin for this club." in captured.out

# Make sure that when a Coordinator's status is taken away, their admin permissions are wiped from all
# clubs they managed and they lose management over their previously owned events.
def test_demote_coordinator():
    ProfMongan = Coordinator("Bill", "Mongan", "wmongan", "wmongan@ursinus.edu", "password", True)
    club1 = Club("CS-375", "Software Engineering")
    club2 = Club("CS-376", "Engineering Software")
    ProfMongan.setCoordinatedClub(club1)
    ProfMongan.setCoordinatedClub(club2)

    event = Event("Project Presentation", "1:00 PM", 10, 5, 2025)
    ProfMongan.hostEvent(event, club1)

    ProfMongan.demote()

    assert not ProfMongan.isCoordinator
    assert ProfMongan.getManagedClubs() == []
    assert ProfMongan.getManagedEvents() == []
    assert ProfMongan._user_id not in club1.getAdminList()
    assert ProfMongan._user_id not in club2.getAdminList()

# If you were not a coordinator in the first place, then demoting you should throw up an error.
def test_demote_non_coordinator(capsys):
    ProfMongan = Coordinator("Bill", "Mongan", "wmongan", "wmongan@ursinus.edu", "password", True)
    ProfMongan.isCoordinator = False

    ProfMongan.demote()

    captured = capsys.readouterr()
    assert "You were not already a coordinator." in captured.out
