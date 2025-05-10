import random

'''

THIS FILE IS JUST TO LET MY COORDINATOR CLASS FUNCTION SINCE IT RELIES ON THE OTHER CLASSES METHODS


'''




###### HANNAH's USER CLASS ######

users = []

class User:
    _user_id = 0 # int Private, unique id per user 
    isCoordinator = False # If User is a Coordinator (default False; if True, make Coordinator object)
    __isDeactivated = False # If User is deactivated (aka deleted) (default False; if True, delete User object)
    clubs = [] # List of Clubs a User follows
    preferences = [] # List of preferences a User follows

    def __init__(self, first_name, last_name, username, email, password, isCoordinator):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.__password = password
        self.isCoordinator = isCoordinator
        random.seed(self.username)
        self._user_id = random.random()
        users.append(self)

    def addClub(self, club):
        hasClub = [i.lower() for i in self.clubs if i in self.clubs]
        if club.lower() in hasClub:
            print("Already has club.")
        else:
            self.clubs.append(club)

    def removeClub(self, club):
        for i in self.clubs:
            if i == club:
                self.clubs.remove(club)

    def addPreference(self, preference):
        hasPreference = [i.lower() for i in self.preferences if i in self.preferences]
        if preference.lower() in hasPreference:
            print("Already has preference.")
        else:
            self.preferences.append(preference)

    def removePreference(self, preference):
        for i in self.preferences:
            if i == preference:
                self.preferences.remove(preference)

    def __deactivateUser(self):
        self.__isDeactivated = True

def isEmailWithUser(email):
    for i in users:
        if i.email == email:
            return True
    return False

def isUsernameWithUser(username):
    for i in users:
        if i.username == username:
            return True
    return False

def __getUserIDFromEmail(email):
    for i in users:
        if i.email == email:
            return i.__user_id
    return None

def __removeUser(__user_id):
    for i in users:
        if i.__user_id == __user_id:
            if i.isDeactivated == True:
                users.remove(i)


####### MICHAEL'S COORDINATOR CLASS ######

class Coordinator(User):
    #isCoordinator = False #inherited from Person class, placeholder for now.
    coordinatedClubs = []
    managedEvents = [] #List<Event>

    def __init__(self, first_name, last_name, username, email, password, isCoordinator):
        super().__init__(first_name, last_name, username, email, password, isCoordinator)
        print(self._user_id)
        self.coordinatedClubs = []
        self.managedEvents = []
        self.isCoordinator = True

    '''
    Initializes the User as a Coordinator of a certain club that will be set later 
    '''
    def setCoordinator(self):
        if (not self.isCoordinator):
            self.isCoordinator = True
            #self.isAdmin = True
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

###### PEDRO'S EVENT CLASS ########

class Event:
    attending = [] # List of users attending

    def __init__(self, eventName, startTime, dateDay, dateMonth, dateYear, endTime = "NA", eventDesc = "NA", lenTime = 0):
        self.eventName = eventName
        self.eventDesc = eventDesc
        self.startTime = startTime
        self.endTime = endTime
        self.dateDay = dateDay
        self.dateMonth = dateMonth
        self.dateYear = dateYear
        self.lenTime = lenTime

    def changeTime(self, newStartTime, newEndTime):
        self.startTime = newStartTime
        self.endTime = newEndTime
    
    def changeDate(self, newDay, newMonth, newYear):
        self.dateDay = newDay
        self.dateMonth = newMonth
        self.dateYear = newYear
    
    def changeDesc(self, newDesc):
        self.eventDesc = newDesc
    
    def changeName(self, newName):
        self.eventName = newName
    
    # depending on event, require RSVP (too lazy to type)
    # possible bool to determine if repeating event

##### MATT'S CLUB CLASS #######

class Club:
    __memberIDs = []
    __adminIDs = []

    def __init__(self, clubName, clubDesc, clubEvents = [], memberIDs = [], adminIDs = []):
        self.clubName = clubName
        self.clubDesc = clubDesc
        self.clubEvents = clubEvents
        self.__memberIDs = memberIDs
        self.__adminIDs = adminIDs
    
    def getMemberCount(self):
        return len(self.__memberIDs)
    
    def getAdminCount(self):
        return len(self.__adminIDs)
    
    def getEventCount(self):
        return len(self.clubEvents)
    
    def getMemberList(self):
        return self.__memberIDs
    
    def getAdminList(self):
        return self.__adminIDs
    
    def getEventList(self):
        return self.clubEvents


    def addAdmin(self, userID):
        if(userID not in self.__memberIDs):
            self.__memberIDs.append(userID)
        if(userID not in self.__adminIDs):
            self.__adminIDs.append(userID)
        else:
            print("User already an admin!")

    def removeAdmin(self, userID):
        if(userID in self.__adminIDs):
            self.__adminIDs.remove(userID)
        else:
            print("User not an admin!")

    def addMember(self, userID):
        if(userID not in self.__memberIDs):
            self.__memberIDs.append(userID)
        else:
            print("User already a member!")

    def removeMember(self, userID):
        if(userID in self.__adminIDs):
            self.__adminIDs.remove(userID)
        if(userID in self.__memberIDs):
            self.__memberIDs.remove(userID)
        else:
            print("User not a member!")

    def changeDesc(self, newDesc):
        self.clubDesc = newDesc

    def addEvent(self, event):
        if(event not in self.clubEvents):
            self.clubEvents.append(event)
        else:
            print("Event already exists!")

    def removeEvent(self, event):
        if(event in self.clubEvents):
            self.clubEvents.remove(event)
        else:
            print("Event doesn't exist!")

    def isAdmin(self, userID):
        return userID in self.__adminIDs

    def isMember(self, userID):
        return userID in self.__memberIDs
            
