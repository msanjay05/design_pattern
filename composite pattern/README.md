# Composite Pattern

The **Composite pattern** composes objects into tree structures to represent part-whole hierarchies. Clients treat individual objects and groups of objects uniformly.

## What Problem Does It Solve?

Tree-structured data (files/folders, org charts, UI components) forces clients to distinguish between leaf nodes and containers with different code paths. That spreads conditional logic everywhere.

Composite lets you work with the whole tree through one interface.

## Core Idea

```
Component (interface)
    ├── Leaf
    └── Composite ──► children: [Leaf, Composite, ...]
```

Both leaves and composites implement the same operations (`display`, `size`, etc.).

## Why Is It Used?

- Uniform treatment of individual and grouped objects
- Simplifies client code that traverses trees
- Makes adding new component types easier
- Natural fit for recursive structures

## When Should You Use It?

Use it when you need to represent hierarchies where nodes and groups should support the same operations.

Avoid it when the structure is flat or when leaf and composite behavior diverges too much.

## Real-World Examples

| Domain | Composite models... |
|--------|---------------------|
| File systems | Files and folders |
| UI | Panels containing buttons, inputs, nested layouts |
| Org charts | Employees and departments |
| Graphics | Shapes and groups of shapes |
| Menus | Items and submenus |

## Benefits and Trade-offs

**Benefits:** Simple client code, easy to add new component types, recursive operations are natural.

**Trade-offs:** Can make the shared interface too generic; type safety may be weaker.

## Related Patterns

| Pattern | Difference |
|---------|------------|
| **Decorator** | Similar tree structure but wraps one object to add behavior; Composite groups children into a part-whole tree |
| **Iterator** | Traverses composite trees without exposing internal structure |
| **Visitor** | Adds operations across the tree without changing element classes |

### Composite vs Decorator

| | Composite | Decorator |
|---|-----------|-----------|
| **Structure** | Tree of children (leaves and containers) | Single wrapper chain around one object |
| **Intent** | Treat one item and a group uniformly | Add responsibilities dynamically |
| **Use when** | Files/folders, UI components, org charts | Logging, compression, pricing layers on one object |

## Summary

Composite builds tree structures where leaves and containers share one interface. Clients treat one item and a whole subtree the same way.

---

Run `python3 main.py` to build and display a folder tree with total size.
