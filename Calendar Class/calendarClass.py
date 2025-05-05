import random
import uuid


class Calendar:
    calendars = []
    events = []

    def __init__(self, title: str, event):
        self.calendar_id = str(uuid.uuid4())
        self.title = title
        self.event = event


    def addCalendar(self, calendar):
        calendar = calendar.strip()
        hasCalendar = [i.lower() for i in self.calendars]
        if calendar.lower() in hasCalendar:
            print("Calendar already exists.")
        elif calendar == "":
            print("Calendar name cannot be empty.")
        else:
            self.calendars.append(calendar)

    def delete_calendar(self, target):
        target = target.strip()
        for calendar in self.calendars:
            if calendar == target:
                self.calendars.remove(calendar)
                break

    def add_event(self, event):
        hasEvent = [i.lower() for i in self.events]
        if event.lower() in hasEvent:
            print("Event is already on the calendar.")
        else:
            self.events.append(event)
    
    def upload_calendar(calendar_data: dict):
        calendar = Calendar(calendar_data['title'])

        for event in calendar_data.get('events', []):
            event = event(**event)
            calendar.events.append(event)

        return calendar

    def combine_calendars(calendar1, calendar2, new_title: str):
        if calendar1.calendar_id == calendar2.calendar_id:
            return None

        combined = Calendar(new_title, None)
        combined.events = calendar1.events + calendar2.events
        
        return combined