Desktop application to help writers to create content.

Ideas for implementing the event service:

Event service must be singleton object:
* Use \__new\__ method to return the unique instance

Use Case 1:
* Event must be registered on subject initialization  <--
* Subscriber be registered on subscriber initialization <--
* User clicks on open file menu
* Menu function request observers subscribed to an event
    from event service <-- X2
* Menu calls update on every observer
    
Test scenarios:
* As application, I want events to be registered
* As component, I want to subscribe to an event 
* As component, I want to retrieve observers subscribed to an event
