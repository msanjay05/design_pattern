# Visitor Pattern

The **Visitor pattern** lets you define new operations on elements of an object structure without changing the classes of those elements.

## What Problem Does It Solve?

Many unrelated operations (area calculation, export, serialization, validation) across a stable class hierarchy lead to bloated classes or scattered logic. Adding a new operation means editing every element class.

Visitor moves operations into separate visitor classes.

## Core Idea

```
Element.accept(visitor) ──► visitor.visitConcreteElement()

Shapes ──► AreaVisitor / ExportVisitor / ...
```

Double dispatch: the element calls the visitor method matching its type.

## Why Is It Used?

- Adds new operations without modifying element classes
- Groups related behavior in one visitor class
- Useful when the object structure is stable but operations evolve
- Keeps element classes focused on data, not every possible algorithm

## When Should You Use It?

Use it when you have a stable hierarchy and frequently add new operations across all types.

Avoid it when the hierarchy changes often (every new element requires updating all visitors) or when the structure is small and simple.

## Real-World Examples

| Domain | Visitors perform... |
|--------|---------------------|
| AST/code | Lint, compile, optimize passes |
| Documents | Export to PDF, HTML, Markdown |
| Shapes | Area, perimeter, render |
| File trees | Search, size calculation, backup |
| E-commerce | Tax, discount, shipping calculations |

## Benefits and Trade-offs

**Benefits:** Open/closed for new operations, related logic grouped together, clean element classes.

**Trade-offs:** Hard to add new element types; breaks encapsulation of element internals; less known to newcomers.

## Related Patterns

| Pattern | Difference |
|---------|------------|
| **Composite** | Visitor often traverses composite tree structures |
| **Iterator** | Walks elements; Visitor performs operations on each via double dispatch |
| **Interpreter** | Visitors can evaluate or transform expression trees |

### Visitor vs Iterator

| | Visitor | Iterator |
|---|---------|----------|
| **Adds** | New operations without changing element classes | Traversal without exposing collection internals |
| **Dispatch** | Double dispatch (`element.accept(visitor)`) | Single interface (`next()`, `has_next()`) |
| **Use when** | Many operations on a stable structure (export, tax, print) | Uniform access to items in any collection |

## Summary

Visitor separates algorithms from the object structure they operate on. Elements accept visitors that perform type-specific operations without modifying the elements themselves.

---

Run `python3 main.py` to compute area and export shapes with different visitors.
