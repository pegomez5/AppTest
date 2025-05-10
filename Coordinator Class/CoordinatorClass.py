from AllClasses import *  # Replace file AllClasses with User, Event, and Club class files in Python

class Coordinator(User):
    coordinatedClubs = []
    managedEvents = [] 

    def __init__(self, first_name, last_name, username, email, password, isCoordinator):
        super().__init__(first_name, last_name, username, email, password, isCoordinator)
        self.coordinatedClubs = []
        self.managedEvents = []
        self.isCoordinator = True

    '''
    Initializes the User as a Coordinator of a certain club that will be set later 
    '''
    def setCoordinator(self):
        if (not self.isCoordinator):
            self.isCoordinator = True
        else:
            print("You are already a coordinator.")


    '''
    This function assigns a club for the Coordinator to have permission to coordinate 

    Parameter(s): 
    club: A Club object to determine the club that the Coordinator can access and manage
    '''
    def setCoordinatedClub(self,club):
        if (not club.isAdmin(self._user_id)):
            club.addAdmin(self._user_id) 
        else:
            print("You are already an admin for this club.")
        if (club not in self.coordinatedClubs):
            self.coordinatedClubs.append(club)
        else:
            print("This club is already in the list.")

    
    '''
    Adds an event to a club hosted by the coordinator 

    Parameter(s): 
    event: an Event object that will be added to this Coordinator's club 
    club: the intended club that the event will be associated with
    '''
    def hostEvent(self,event,club):
        if (club.isAdmin(self._user_id)):
            #index = self.coordinatedClubs.index(club) # Finding the specific club out of the Coordinator's possible clubs

            if (event not in self.managedEvents) & (event not in club.getEventList()): 
                self.managedEvents.append(event)  # Make sure that the coordinator is assigned to managing the event
                club.addEvent(event) # adding event to Club object using method from club class.
            elif (event not in self.managedEvents) & (event in club.getEventList()): 
                self.managedEvents.append(event)  # Add yourself as a collaborator to this club's event

            elif (event in self.managedEvents) & (event not in club.getEventList()): 
                club.addEvent(event) # adding an event currently being managed to the club.
            
            # else: do nothing since this even has already been created

        else:
            # Invalid Permissions!
            print("Invalid Permissions! You are not an Admin for this club.")

    '''
    Ends an event from a club hosted by the coordinator 

    Parameter(s): 
    event: an Event object that will be terminated from this Coordinator's club 
    club: the intended club that the event will be no longer be associated with
    '''
    def endEvent(self,event,club):
        if (club.isAdmin(self._user_id)):
            index = self.coordinatedClubs.index(club) # Finding the specific club out of the Coordinator's possible clubs

            if (event in self.managedEvents) & (event in self.coordinatedClubs[index].getEventList()): 
                self.managedEvents.remove(event)  # Make sure that the coordinator is no longer assigned to managing the event
                self.coordinatedClubs[index].removeEvent(event) # removing event from the Club object using method from club class.

            elif (event in self.managedEvents) & (event not in self.coordinatedClubs[index].getEventList()): 
                self.managedEvents.remove(event)  # Stop managing the event since the club has already ditched it

            elif (event not in self.managedEvents) & (event in self.coordinatedClubs[index].getEventList()): 
                self.coordinatedClubs[index].removeEvent(event) # removing the event currently being managed by the club.

            # else: do nothing since there is nothing to remove
        else:
            # Invalid Permissions!
            print("Invalid Permissions! You are not an Admin for this club.")


    '''
    Demotes the User from their role as a Coordinator of a certain club
    '''
    def demote(self):
        if (self.isCoordinator):
            self.isCoordinator = False
            #self.isAdmin = True
            for club in self.coordinatedClubs:
                club.removeAdmin(self._user_id)
                #self.coordinatedClubs.remove(club)
            self.managedEvents = []
            self.coordinatedClubs = []
        else:
            print("You were not already a coordinator.")


    '''
    Getter for the Coordinator's currently managed events
    '''
    def getManagedEvents(self):
        return self.managedEvents
    
    '''
    Getter for the clubs that the Coordinator is an admin for
    '''
    def getManagedClubs(self):
        return self.coordinatedClubs
    
    '''
    Relinquish admin permissions from the club if it is one that the Coordinator coordinates
    The Coordinator remains as a normal member of this club, just not an admin.

    Paramaters:
    club - Club that you no longer want to be in charge of
    '''
    def relegateAdmin(self,club):
        if (club.isAdmin(self._user_id)):
            if (club in self.coordinatedClubs):
                index = self.coordinatedClubs.index(club) # Finding the specific club out of the Coordinator's possible clubs
                self.coordinatedClubs.pop(index)
                club.removeAdmin(self._user_id)
            else:
                # Invalid index!
                print("This club is not in your list!")

        else:
            # Invalid Permissions!
            print("Invalid Permissions! You are not an Admin for this club.")
