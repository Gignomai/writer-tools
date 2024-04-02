import unittest
from domain.event_manager.EventManager import EventManager


class TestEventCreation(unittest.TestCase):
    def test_event_registration(self):
        event = "Event"
        event_manager = EventManager()
        event_manager.register(event)

        self.assertEqual(event_manager.events[event], [])

    def test_event_add_subscriber(self):
        event = "Event"
        event_manager = EventManager()
        event_manager.register(event)

        first_component = "Component 1"
        second_component = "Component 2"
        event_manager.subscribe(event, first_component)
        event_manager.subscribe(event, second_component)

        self.assertEqual(first_component, event_manager.events[event][0])
        self.assertEqual(second_component, event_manager.events[event][1])

    def test_return_subscribers_to_an_event(self):
        event = "Event"
        event_manager = EventManager()
        event_manager.register(event)

        first_component = "Component 1"
        second_component = "Component 2"
        event_manager.subscribe(event, first_component)
        event_manager.subscribe(event, second_component)

        subscribers = event_manager.get_subscribers("Event")

        self.assertEqual(2, len(subscribers))
        self.assertEqual(first_component, subscribers[0])
        self.assertEqual(second_component, subscribers[1])


if __name__ == '__main__':
    unittest.main()
