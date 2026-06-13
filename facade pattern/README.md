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

- **Adapter:** Changes interface to match; Facade simplifies but keeps subsystem intent
- **Mediator:** Coordinates peer components; Facade is one-directional simplification
- **Abstract Factory:** Can be used with Facade to hide creation complexity

## Summary

Facade offers a single, friendly entry point to a complicated system. Clients get simplicity; the subsystem keeps its internal structure.

---

Run `python3 main.py` to watch a movie through a home theater facade.
