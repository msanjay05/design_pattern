# Flyweight Pattern

The **Flyweight pattern** minimizes memory use by sharing intrinsic (common) state among many objects instead of storing duplicate data in each instance.

## What Problem Does It Solve?

Applications with huge numbers of similar objects (trees in a forest, characters in a document, tiles on a map) can consume excessive memory when each object stores the same repeated data.

## Core Idea

```
FlyweightFactory ──► shared intrinsic state (TreeType)
                              ▲
Context objects ──► extrinsic state (x, y position)
```

Separate what is shared from what varies per instance.

## Why Is It Used?

- Reduces memory footprint dramatically
- Improves performance when many similar objects exist
- Centralizes shared immutable data

## When Should You Use It?

Use it when you have many objects, most state can be shared, and extrinsic state can be passed in at use time.

Avoid it when objects are few, state is mostly unique, or sharing adds unacceptable complexity.

## Real-World Examples

| Domain | Shared state includes... |
|--------|--------------------------|
| Text editors | Character glyphs (font, size, style) |
| Games | Tree/grass/sprite types across a map |
| Browser | DOM nodes with shared CSS/style data |
| Maps | Tile textures reused at many coordinates |
| Networking | Connection metadata templates |

## Benefits and Trade-offs

**Benefits:** Lower memory use, faster instantiation, centralized shared data.

**Trade-offs:** Code complexity, must carefully split intrinsic vs extrinsic state, factory/cache management overhead.

## Related Patterns

| Pattern | Difference |
|---------|------------|
| **Singleton** | Flyweight factory often behaves like a controlled pool of shared instances |
| **Composite** | Flyweight leaves can be shared inside composite trees |
| **State** | Can share state objects similarly, but State models behavior transitions |

### Flyweight vs Singleton vs State

| | Flyweight | Singleton | State |
|---|-----------|-----------|-------|
| **Shares** | Intrinsic data across many lightweight objects | One instance of a class | State objects representing phases |
| **Goal** | Reduce memory for huge numbers of similar objects | Guarantee a single global instance | Change behavior via state transitions |
| **Use when** | Thousands of trees, tiles, or characters share texture data | One config manager or connection pool | Finite state machines |

## Summary

Flyweight shares common data across many lightweight objects. Only extrinsic, context-specific state lives in each instance.

---

Run `python3 main.py` to render many trees while sharing one `TreeType` object.
