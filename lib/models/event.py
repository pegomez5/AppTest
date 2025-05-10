class Event:
    def __init__(self, date, location, coordinator, id=None, desc=""):
        self.date = date
        self.location = location
        self.coordinator = coordinator
        self.id = id
        self.desc = desc

    def _create_id(self, date, location):
        # Create a hash from date and location
        return hash((date, location))

    def updateEvent(self, date=None, location=None):
        if date:
            self.date = date
        if location:
            self.location = location
        self.id = self._create_id(self.date, self.location)


class Event_Manager:
    def __init__(self):
        self.events = [] # our python "database". superb

    # Returns an event
    def create_event(self, date, location, coordinator, id=None, desc=""):
        event = Event(date, location, coordinator, hash((date, location)), desc)
        self.events.append(event)
        return event

    # Returns true if event is deleted
    def delete_event(self, event):
        if event in self.events:
            self.events.remove(event)
            return True
        return False

    # Returns the event with the given id
    def get_event_by_id(self, id):
        for event in self.events:
            if event.id == id:
                return event
        return None

    # Returns list of events
    def get_all_events(self):
        return self.events

    # Returns true if event is updated
    def update_event(self, event, date=None, location=None):
        if event in self.events:
            event.updateEvent(date, location)
            return True
        return False


