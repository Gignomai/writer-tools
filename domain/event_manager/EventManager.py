class EventManager:
    _instance = None
    events = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(EventManager, cls).__new__(cls)
        return cls._instance

    def register(self, event):
        self.events[event] = []

    def subscribe(self, event_name, subscriber):
        self.events[event_name].append(subscriber)

    def get_subscribers(self, event):
        return self.events[event]
