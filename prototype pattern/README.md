# Prototype Pattern

The **Prototype pattern** creates new objects by copying existing ones (cloning) instead of building from scratch.

## What Problem Does It Solve?

Object creation can be expensive or complex: database reads, network calls, heavy parsing, or many nested fields. When you need a similar object with small changes, reconstructing everything is wasteful.

## Core Idea

```
Client ──► prototype.clone() ──► New object with copied state
```

The original object acts as a template. Cloning duplicates its state, then you modify only what differs.

## Why Is It Used?

- Avoids repeating costly initialization
- Simplifies creating objects that differ slightly from an existing one
- Keeps creation logic with the object itself
- Useful when classes are unknown at compile/design time

## When Should You Use It?

Use it when copying is cheaper or simpler than constructing from zero, especially with deep object graphs.

Avoid it when objects are trivial to create or when shared references in a shallow copy would cause bugs (use deep copy when needed).

## Real-World Examples

| Domain | Prototype clones... |
|--------|---------------------|
| Documents | Report templates with prefilled sections |
| Games | Enemy templates with varied stats |
| Graphics | Shape presets with minor tweaks |
| Config | Default settings objects per tenant |
| Testing | Complex fixture objects for test cases |

## Benefits and Trade-offs

**Benefits:** Faster creation, reduced subclassing, runtime flexibility.

**Trade-offs:** Must handle deep vs shallow copy correctly; circular references complicate cloning.

## Related Patterns

- **Factory:** Builds new instances from scratch
- **Memento:** Saves/restores object state (different intent: history vs duplication)
- **Builder:** Assembles objects step by step rather than copying

## Summary

Prototype copies an existing object to produce new instances. It is ideal when setup is expensive and new objects mostly resemble ones you already have.

---

Run `python3 main.py` to clone a report and modify the copy independently.
