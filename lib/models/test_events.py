import pytest
from event import Event, Event_Manager

date = "2023-10-01"
location = "New York"
coordinator = "John Doe"

# Test for proper use
def test_event_creation():
    event_manager = Event_Manager()
    event = event_manager.create_event(date, location, coordinator)
    assert event.date == "2023-10-01"
    assert event.location == "New York"
    assert event.coordinator == "John Doe"
    assert event.id is not None

def test_get_event():
    event_manager = Event_Manager()
    event = event_manager.create_event(date, location, coordinator)
    retrieved_event = event_manager.get_event_by_id(event.id)
    assert retrieved_event == event

def test_event_delete():
    event_manager = Event_Manager()
    event = event_manager.create_event(date, location, coordinator)
    assert event_manager.delete_event(event) == True
    assert event_manager.get_event_by_id(event.id) is None

def test_event_update():
    event_manager = Event_Manager()
    event = event_manager.create_event(date, location, coordinator)
    event_manager.update_event(event, date="2023-11-01", location="Mars")
    assert event.date == "2023-11-01"
    assert event.location == "Mars"

def test_get_all_events():
    event_manager = Event_Manager()
    event1 = event_manager.create_event(date, location, coordinator)
    event2 = event_manager.create_event("2023-11-01", "Mars", "Jane Doe")
    all_events = event_manager.get_all_events()
    assert len(all_events) == 2
    assert event1 in all_events
    assert event2 in all_events

def test_get_event_by_id():
    event_manager = Event_Manager()
    event = event_manager.create_event(date, location, coordinator)
    retrieved_event = event_manager.get_event_by_id(event.id)
    assert retrieved_event == event
    assert retrieved_event.id == event.id

# Test for improper use
def test_event_update_with_none():
    event_manager = Event_Manager()
    event = event_manager.create_event(date, location, coordinator)
    event_manager.update_event(event, date=None, location="Mars")
    assert event.date == "2023-10-01"
    assert event.location == "Mars"

def test_event_delete_nonexistent():
    event_manager = Event_Manager()
    event = event_manager.create_event(date, location, coordinator)
    event_manager.delete_event(event)
    assert event_manager.delete_event(event) == False
    assert event_manager.get_event_by_id(event.id) is None

