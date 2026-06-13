# Builder Pattern

The **Builder pattern** constructs complex objects step by step. It separates the construction process from the object's representation so the same construction steps can create different variations.

## What Problem Does It Solve?

Objects with many optional fields or nested parts lead to telescoping constructors:

```python
Pizza("large", "thin", ["cheese", "pepperoni"], True, False, ...)
```

This is hard to read, easy to misuse, and painful to extend. Builder replaces that with a fluent, readable API.

## Core Idea

```
Director/Client ──► Builder ──► step-by-step assembly ──► Product
```

The builder exposes methods for each part. The final `build()` call returns the completed object.

## Why Is It Used?

- Makes object construction readable and self-documenting
- Allows different representations using the same building steps
- Isolates complex assembly logic from business code
- Supports optional parameters without long constructor lists

## When Should You Use It?

Use it when an object has many configuration options or assembly happens in multiple stages.

Avoid it when a simple constructor or dataclass is enough.

## Real-World Examples

| Domain | Builder constructs... |
|--------|------------------------|
| APIs | HTTP requests with headers, body, auth |
| SQL | Queries with filters, joins, ordering |
| UI | Forms and layouts from components |
| Documents | Reports with sections and formatting |
| Games | Characters with stats, gear, skills |

## Benefits and Trade-offs

**Benefits:** Readable construction, flexible combinations, single place for validation before `build()`.

**Trade-offs:** More classes and boilerplate for simple objects.

## Related Patterns

- **Factory:** Creates objects in one step; Builder assembles in multiple steps
- **Abstract Factory:** Creates families of related products
- **Composite:** Often built recursively with a Builder

## Summary

Builder breaks complex construction into clear, chainable steps. It improves readability and maintainability when objects have many optional parts.

---

Run `python3 main.py` in this folder to build a pizza step by step.
