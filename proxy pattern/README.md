# Proxy Pattern

The **Proxy pattern** provides a surrogate or placeholder that controls access to another object. The proxy implements the same interface as the real subject.

## What Problem Does It Solve?

You may need to delay expensive operations, add security checks, log access, cache results, or manage remote objects. Putting that logic inside the real object violates single responsibility. Clients should not care whether they talk to the real object or a stand-in.

## Core Idea

```
Client ──► Proxy ──► (optional checks) ──► Real Subject
```

The proxy implements the same interface and decides when/how to forward calls.

## Common Proxy Types

| Type | Purpose |
|------|---------|
| **Virtual** | Lazy-load expensive objects |
| **Protection** | Enforce permissions |
| **Remote** | Represent object in another process/network |
| **Caching** | Return cached results when possible |

## Why Is It Used?

- Defers costly creation until needed
- Adds cross-cutting concerns without changing the real object
- Controls access to sensitive resources
- Hides distribution complexity (remote proxy)

## When Should You Use It?

Use it when you need indirection around an object for control, optimization, or security.

Avoid it when the extra layer adds complexity without a clear benefit.

## Real-World Examples

| Domain | Proxy handles... |
|--------|------------------|
| Images | Lazy loading large files |
| APIs | Rate limiting and auth |
| ORM | Lazy-loading database relations |
| Files | Access control before read/write |
| Networks | Local representative of remote service |

## Benefits and Trade-offs

**Benefits:** Open/closed extension, transparent to clients, separation of concerns.

**Trade-offs:** Extra indirection; can obscure performance characteristics if overused.

## Related Patterns

- **Decorator:** Adds behavior; Proxy often controls access or defers work
- **Adapter:** Changes interface; Proxy keeps the same interface
- **Facade:** Simplifies a subsystem; Proxy represents one object

## Summary

Proxy stands in for another object and controls how clients reach it. It is ideal for lazy loading, access control, caching, and remote access.

---

Run `python3 main.py` to see lazy image loading through a virtual proxy.
