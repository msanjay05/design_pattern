# Observer Pattern

The **Observer pattern** defines a one-to-many dependency: when one object (the subject) changes state, all dependents (observers) are notified automatically.

## What Problem Does It Solve?

Without Observer, subjects must know every interested party and call them directly. Adding a new listener means editing the subject. That creates tight coupling and poor scalability.

## Core Idea

```
Subject ──publish──► Observer 1
                 ├──► Observer 2
                 └──► Observer 3
```

Observers subscribe to the subject. When state changes, the subject broadcasts an update.

## Why Is It Used?

- Decouples event producers from consumers
- Supports dynamic subscription and unsubscription
- Enables reactive, event-driven architectures
- Lets you add new observers without changing the subject

## When Should You Use It?

Use it when changes in one object should trigger updates in others, and you do not know how many listeners there will be.

Avoid it when notification order matters critically without extra design, or when debugging cascading updates becomes unmanageable.

## Real-World Examples

| Domain | Observers react to... |
|--------|------------------------|
| News | New articles published |
| UI | Button clicks, form changes |
| Stocks | Price updates |
| Microservices | Domain events on a message bus |
| Model-View | Data model changes updating views |

## Benefits and Trade-offs

**Benefits:** Loose coupling, dynamic relationships, supports event-driven design.

**Trade-offs:** Unexpected update chains, potential memory leaks if observers are not removed, notification order may be undefined.

## Related Patterns

| Pattern | Difference |
|---------|------------|
| **Mediator** | Central hub coordinates colleagues; Observer distributes updates from one subject to many |
| **Publisher-Subscriber** | Often a distributed, decoupled variant of Observer |
| **MVC** | Model notifies Views via Observer-style updates |

### Observer vs Mediator

| | Observer | Mediator |
|---|----------|----------|
| **Flow** | Subject notifies many subscribers | Colleagues communicate through one coordinator |
| **Coupling** | Observers subscribe to subject events | Colleagues avoid direct references to each other |
| **Use when** | UI binding, domain events, reactive updates | Complex many-to-many workflows (chat, forms) |

## Summary

Observer lets objects listen for changes without the subject knowing their concrete types. It is the foundation of event-driven and reactive systems.

---

Run `python3 main.py` to publish news to email and SMS subscribers.
