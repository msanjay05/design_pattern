# Adapter Pattern

The **Adapter pattern** lets objects with incompatible interfaces work together. It wraps an existing class and exposes the interface the client expects.

## What Problem Does It Solve?

You often integrate third-party libraries, legacy systems, or external APIs whose interfaces do not match your application's abstractions. Rewriting them is costly; changing all client code is risky.

Adapter sits in between and translates calls.

## Core Idea

```
Client ──► Target Interface ──► Adapter ──► Adaptee (legacy/external)
```

The client calls methods it understands. The adapter converts those calls to the adaptee's API.

## Why Is It Used?

- Integrates legacy or third-party code without modifying it
- Keeps domain code clean and consistent
- Supports incremental migration to new interfaces
- Reuses existing components in new contexts

## When Should You Use It?

Use it when you need to use a class but its interface does not match what your code expects.

Avoid it when you own the code and can change the interface directly, or when the mismatch is too large to translate cleanly.

## Real-World Examples

| Domain | Adapter connects... |
|--------|---------------------|
| Payments | Legacy gateway to modern `PaymentProcessor` |
| Data | XML API to JSON consumer |
| UI | Third-party chart library to internal widget API |
| Auth | OAuth provider to app's `Authenticator` interface |
| Storage | S3 SDK to internal `FileStore` contract |

## Benefits and Trade-offs

**Benefits:** Reuse without rewrite, separation of concerns, smoother integrations.

**Trade-offs:** Extra indirection layer; adapter can become a maintenance point if APIs drift.

## Related Patterns

| Pattern | Difference |
|---------|------------|
| **Facade** | Simplifies a whole subsystem behind one entry point; Adapter makes one incompatible interface fit another |
| **Decorator** | Keeps the same interface and adds behavior; Adapter translates between different interfaces |
| **Bridge** | Designs abstraction/implementation separation upfront; Adapter retrofits existing mismatches |

### Adapter vs Facade vs Decorator

| | Adapter | Facade | Decorator |
|---|---------|--------|-----------|
| **Changes** | Interface shape | Perceived complexity | Behavior (wraps and extends) |
| **Target** | One incompatible component | Entire subsystem | One object, same interface |
| **Use when** | Legacy or third-party API does not match yours | Clients need a simple API over many classes | You want optional, stackable features |

## Summary

Adapter translates one interface into another. It is the glue that lets incompatible components work together without rewriting either side.

---

Run `python3 main.py` to charge via a legacy payment gateway through a modern adapter.
