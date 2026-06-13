# Mediator Pattern

The **Mediator pattern** defines an object that encapsulates how a set of objects interact. Colleagues communicate through the mediator instead of referencing each other directly.

## What Problem Does It Solve?

When many objects talk to each other directly, you get a dense web of dependencies. Adding or changing one object forces updates across many others.

Mediator centralizes coordination logic.

## Core Idea

```
Colleague A ──┐
Colleague B ──┼──► Mediator ──► routes/coordinates messages
Colleague C ──┘
```

Objects send messages to the mediator; the mediator decides who gets notified.

## Why Is It Used?

- Reduces chaotic many-to-many dependencies
- Centralizes interaction rules
- Makes components easier to reuse independently
- Simplifies adding new colleagues

## When Should You Use It?

Use it when many objects communicate in complex, changing ways and direct references would tangle the system.

Avoid it when the mediator becomes a monolithic "god object" absorbing too much logic.

## Real-World Examples

| Domain | Mediator coordinates... |
|--------|-------------------------|
| Chat | Users in a chat room |
| Air traffic | Planes and control tower |
| UI dialogs | Form fields and validation |
| Microservices | Event bus / orchestrator |
| Games | Turn order and event routing |

## Benefits and Trade-offs

**Benefits:** Loose coupling, centralized control, easier component changes.

**Trade-offs:** Mediator complexity can grow; can become a bottleneck if overloaded.

## Related Patterns

- **Observer:** Distributes events; Mediator orchestrates bidirectional communication
- **Facade:** Simplifies subsystem access; Mediator manages ongoing interactions
- **Command:** Colleagues can send command objects to the mediator

## Summary

Mediator replaces direct colleague-to-colleague communication with centralized coordination. Components stay loosely coupled and easier to maintain.

---

Run `python3 main.py` to send chat messages through a chat room mediator.
