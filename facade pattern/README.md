# Facade Pattern

The **Facade pattern** provides a simplified interface to a complex subsystem. It hides intricate details behind one easy-to-use entry point.

## What Problem Does It Solve?

Large subsystems expose many classes, methods, and configuration steps. Clients that talk to every component directly become tightly coupled and hard to maintain.

## Core Idea

```
Client ──► Facade ──► Subsystem A
                   ├── Subsystem B
                   └── Subsystem C
```

One facade method can orchestrate dozens of internal calls in the right order.

## Why Is It Used?

- Reduces coupling between clients and subsystems
- Makes common workflows simple and discoverable
- Provides a stable API even when internals change
- Improves readability of client code

## When Should You Use It?

Use it when a subsystem is complex but clients only need a few high-level operations.

Avoid it when clients genuinely need fine-grained control over every subsystem detail.

## Real-World Examples

| Domain | Facade simplifies... |
|--------|----------------------|
| Home theater | Power on, set input, play movie |
| Travel booking | Flights + hotel + car in one call |
| Compilers | Parse, optimize, emit behind `compile()` |
| Frameworks | High-level APIs over low-level modules |
| Microservices | API gateway aggregating multiple services |

## Benefits and Trade-offs

**Benefits:** Simpler client code, better layering, easier onboarding.

**Trade-offs:** Facade can grow into a "god object" if it absorbs too much logic; not a substitute for good subsystem design.

## Related Patterns

| Pattern | Difference |
|---------|------------|
| **Adapter** | Changes interface to fit; Facade simplifies but keeps subsystem intent and does not redesign APIs |
| **Mediator** | Coordinates ongoing peer-to-peer workflows; Facade is a one-way simplification layer |
| **Abstract Factory** | Can hide creation complexity behind a Facade |

### Facade vs Adapter vs Mediator

| | Facade | Adapter | Mediator |
|---|--------|---------|----------|
| **Role** | Simple entry point to a subsystem | Interface translator | Central communication hub |
| **Direction** | Client → subsystem | Client ↔ adaptee | Colleagues ↔ mediator |
| **Use when** | Many classes, one easy API needed | One component has the wrong interface | Many objects would otherwise reference each other |

## Summary

Facade offers a single, friendly entry point to a complicated system. Clients get simplicity; the subsystem keeps its internal structure.

---

Run `python3 main.py` to watch a movie through a home theater facade.
