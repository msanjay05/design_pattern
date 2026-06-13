# Singleton Pattern

The **Singleton pattern** ensures a class has only one instance and provides a global access point to it.

## What Problem Does It Solve?

Some resources should exist exactly once in an application: database connection pools, configuration managers, loggers, or hardware device handles. Creating multiple instances can waste memory, cause inconsistent state, or break system constraints.

Without Singleton, every part of the code can do `DatabaseConnection()` and you end up with many independent connections.

## Core Idea

```
Client ──► get_instance() ──► The One Instance
```

The class controls its own instantiation. The first call creates the object; later calls return the same object.

## Why Is It Used?

- Guarantees a single shared instance
- Provides controlled global access
- Defers creation until first use (lazy initialization)
- Avoids duplicate initialization of expensive resources

## When Should You Use It?

Use it when exactly one instance must coordinate actions across the system.

Avoid it when:

- You need multiple independent instances
- Global state makes testing harder than the problem warrants
- Dependency injection can provide a shared instance more cleanly

## Real-World Examples

| Domain | Singleton manages... |
|--------|----------------------|
| Apps | Configuration / settings |
| Logging | Central logger |
| Hardware | Printer spooler, GPU context |
| Caching | In-memory cache manager |
| Threading | Connection pool coordinator |

## Benefits and Trade-offs

**Benefits:** Controlled access, reduced duplication, lazy initialization.

**Trade-offs:** Hidden global state, harder unit testing, can violate Single Responsibility if overused.

## Related Patterns

- **Factory:** Can return the same Singleton instance
- **Monostate:** Shares state across instances instead of enforcing one instance
- **Dependency Injection:** Often preferred over Singleton in modern apps

## Summary

Singleton restricts instantiation so only one object exists. Use it sparingly for truly shared resources, and prefer explicit dependency injection when possible.

---

Run `python3 main.py` in this folder to see a shared database connection instance.
