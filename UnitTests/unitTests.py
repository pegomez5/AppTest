import unittest
from calendarClass import Calendar

class calendarTests(unittest.TestCase):
    calendar = Calendar("Test Calendar", None)

    def setUp(self):
        self.calendar = Calendar("Test Calendar", None)


    def test_add_calendar(self):
        self.calendar.calendars = []
        self.calendar.addCalendar("Fall semester 2024")
        self.assertIn("Fall semester 2024", self.calendar.calendars)

    def test_add_exxisting_calendar(self): # adding pre-existing calendar
        self.calendar.calendars = []
        self.calendar.addCalendar("Fall semester 2024")
        self.assertIn("Fall semester 2024", self.calendar.calendars)

        # should print calendar already exists
        self.calendar.addCalendar("Fall semester 2024")
        self.assertIn("Fall semester 2024", self.calendar.calendars) 
    
    def test_add_two_calendar(self):
        self.calendar.calendars = []
        self.calendar.addCalendar("Fall semester 2024")
        self.assertIn("Fall semester 2024", self.calendar.calendars)

        self.calendar.addCalendar("Holidays 2025")
        self.assertIn("Holidays 2025", self.calendar.calendars)
    
    def test_add_empty_calendar(self):
        self.calendar.calendars = []
        self.calendar.addCalendar("")
        self.assertIn("", self.calendar.calendars)
    
    def test_add_calendar_trim_spaces(self):
        self.calendar.calendars = []
        self.calendar.addCalendar("Fall semester 2024")
        self.calendar.addCalendar("  Fall semester 2024  ")

        self.assertEqual(len(self.calendar.calendars), 1)

    def test_delete_calendar(self):
        self.calendar.calendars = []
        self.calendar.addCalendar("Fall semester 2024")
        self.assertIn("Fall semester 2024", self.calendar.calendars)

        self.calendar.delete_calendar("Fall semester 2024")
        self.assertNotIn("Fall semester 2024", self.calendar.calendars)
    
    def test_delete_nonexisting_calendar(self):
        self.calendar.calendars = []
        self.calendar.addCalendar("Work Schedule")

        self.calendar.delete_calendar("Fall semester 2024")
        self.assertNotIn("Fall semester 2024", self.calendar.calendars)

    def test_delete_calendar_trim(self):
        self.calendar.calendars = []
        self.calendar.addCalendar("Work Schedule")

        self.calendar.delete_calendar(" Work Schedule ")
        self.assertNotIn(" Work Schedule ", self.calendar.calendars)
    
    def test_delete_empty_calendar(self):
        self.calendar.calendars = []
        self.calendar.addCalendar("Work Schedule")

        self.calendar.delete_calendar("")
        self.assertNotIn("", self.calendar.calendars)

    def test_add_event(self):
        self.calendar.events = []
        self.calendar.add_event("Meeting with Advisor")
        self.assertIn("Meeting with Advisor", self.calendar.events)

    def test_add_duplicate_event(self):
        self.calendar.events = []
        self.calendar.add_event("Meeting with Advisor")
        self.calendar.add_event("Meeting with Advisor")
        self.assertEqual(self.calendar.events.count("Meeting with Advisor"), 1)

    def test_add_event_case_insensitive(self):
        self.calendar.events = []
        self.calendar.add_event("Meeting with Advisor")
        self.calendar.add_event("meeting with advisor")
        self.assertEqual(len(self.calendar.events), 1)
    
    def test_add_event_empty_string(self): # Should fail/Dont want to add empty
        self.calendar.events = []
        self.calendar.add_event("")
        self.assertIn("", self.calendar.events)

    def test_combine_calendars(self):
        calendar1 = Calendar("Calendar One", None)
        calendar1.calendar_id = 1
        calendar1.events = ["CS-375", "CS-475"]

        calendar2 = Calendar("Calendar Two", None)
        calendar2.calendar_id = 2
        calendar2.events = ["Print Making", "Under water basket weaving"]

        combined = Calendar.combine_calendars(calendar1, calendar2, "Combined Calendar")
        self.assertIsNotNone(combined)
        self.assertEqual(combined.title, "Combined Calendar")
        self.assertEqual(combined.events, ["CS-375", "CS-475", "Print Making", "Under water basket weaving"])
