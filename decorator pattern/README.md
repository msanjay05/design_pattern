# Decorator Pattern

The **Decorator pattern** attaches new behavior to objects dynamically by wrapping them in decorator classes that share the same interface.

## What Problem Does It Solve?

Subclassing for every combination of features explodes the class hierarchy: `Coffee`, `CoffeeWithMilk`, `CoffeeWithMilkAndSugar`, and so on. You need flexible, mix-and-match behavior at runtime.

## Core Idea

```
Client ──► Decorator ──► Decorator ──► Core Component
              │              │
           adds cost      adds sugar
```

Each decorator implements the same interface as the core object and delegates to the wrapped object while adding its own behavior.

## Why Is It Used?

- Adds responsibilities without modifying original classes
- Composes behavior at runtime
- Follows Open/Closed Principle: extend by wrapping, not editing
- Avoids combinatorial subclass explosion

## When Should You Use It?

Use it when you need optional, stackable features on a base object.

Avoid it when behavior combinations are fixed and few (a simple class may suffice), or when debugging deep decorator chains becomes too hard.

## Real-World Examples

| Domain | Decorators add... |
|--------|-------------------|
| I/O | Buffering, compression, encryption on streams |
| Web | Middleware layers on HTTP handlers |
| UI | Borders, scrollbars, shadows on widgets |
| Coffee/food | Toppings and extras |
| Logging | Timestamps, formatting, filtering |

## Benefits and Trade-offs

**Benefits:** Flexible composition, single responsibility per decorator, runtime configurability.

**Trade-offs:** Many small classes; order of decorators can matter; harder to reason about than a flat object.

## Related Patterns

| Pattern | Difference |
|---------|------------|
| **Adapter** | Changes interface to make components work together; Decorator keeps interface and adds behavior |
| **Composite** | Groups children in a tree; Decorator wraps a single object in a chain |
| **Proxy** | Controls access or defers work; Decorator adds functionality |

### Decorator vs Proxy vs Adapter

| | Decorator | Proxy | Adapter |
|---|-----------|-------|---------|
| **Interface** | Same as wrapped object | Same as real subject | Different — translates to what client expects |
| **Purpose** | Add features (stackable) | Control access (lazy, security, remote) | Make incompatible code work together |
| **Use when** | Optional layers like logging or encryption | Expensive creation, permissions, remote calls | Integrating legacy or third-party APIs |

## Summary

Decorator wraps objects to add behavior layer by layer. It is the standard way to extend functionality without subclass explosion.

---

Run `python3 main.py` to stack milk and sugar decorators on a coffee.
