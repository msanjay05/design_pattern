# Iterator Pattern

The **Iterator pattern** provides a way to access elements of a collection sequentially without exposing its internal representation.

## What Problem Does It Solve?

Collections store data in different ways (arrays, linked lists, trees), but clients should traverse them uniformly. Exposing internal structure couples clients to implementation details and makes change costly.

## Core Idea

```
Collection ──► create_iterator() ──► Iterator
                                      │
                                 next(), hasNext()
```

The iterator encapsulates traversal logic. Clients loop without knowing how data is stored.

## Why Is It Used?

- Uniform traversal across different collection types
- Supports multiple simultaneous traversals
- Hides internal storage details
- Enables lazy/paginated access

## When Should You Use It?

Use it when you need standard sequential access to a collection without leaking its structure.

Note: Python built-in iterators (`__iter__`, `__next__`) implement this pattern natively. Custom iterators are still useful for complex traversal orders (BFS, filtered views, paginated APIs).

## Real-World Examples

| Domain | Iterator traverses... |
|--------|------------------------|
| Collections | Lists, sets, custom data structures |
| Databases | Result set cursors |
| File systems | Directory contents |
| APIs | Paginated endpoints |
| Trees/graphs | BFS/DFS order |

## Benefits and Trade-offs

**Benefits:** Single Responsibility for traversal, multiple iterators per collection, polymorphic iteration.

**Trade-offs:** Extra objects; for simple lists native loops may suffice.

## Related Patterns

| Pattern | Difference |
|---------|------------|
| **Composite** | Iterators commonly walk composite trees without exposing internals |
| **Visitor** | Often applied during iteration to run operations on each element |
| **Memento** | Can store iterator position for bookmarks or resume points |

### Iterator vs Visitor

| | Iterator | Visitor |
|---|----------|---------|
| **Provides** | Sequential access to collection elements | Type-specific operations on each element |
| **Coupling** | Hides how the collection is stored | Adds behavior without changing element classes |
| **Use when** | You need uniform traversal (`for item in collection`) | You need many operations over a stable structure |

## Summary

Iterator separates collection traversal from the collection itself. Clients access elements one by one through a standard interface.

---

Run `python3 main.py` to iterate over a book collection.
