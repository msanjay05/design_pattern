# Abstract Factory Pattern

The **Abstract Factory pattern** provides an interface for creating families of related objects without specifying their concrete classes.

## What Problem Does It Solve?

Some systems need groups of objects that must work together consistently. A Windows button should pair with a Windows checkbox, not a Mac checkbox. Scattering individual factory calls risks mixing incompatible components.

## Core Idea

```
Client ──► AbstractFactory ──► ProductA + ProductB + ProductC
                │
     ┌──────────┴──────────┐
WindowsFactory          MacFactory
```

You choose one factory implementation and get a coherent set of products.

## Why Is It Used?

- Ensures product families stay compatible
- Decouples client code from concrete classes
- Makes swapping entire platforms/themes/configurations easy

## When Should You Use It?

Use it when you need multiple related products and must guarantee they belong to the same family.

Avoid it when you only create one type of object (use Factory Method or Simple Factory instead).

## Real-World Examples

| Domain | Families include... |
|--------|---------------------|
| UI | Button, Checkbox, Dialog per OS theme |
| Cloud | Storage + Queue + Cache for AWS vs Azure |
| Documents | Parser + Writer + Validator per format |
| Games | Terrain + Enemy + UI skin per level theme |

## Benefits and Trade-offs

**Benefits:** Consistency across related objects, easy environment switching, strong encapsulation.

**Trade-offs:** Harder to add a new product type (every factory must implement it), more classes.

## Related Patterns

| Pattern | Difference |
|---------|------------|
| **Factory Method** | Creates one product per factory; Abstract Factory creates matched *families* of related products |
| **Builder** | Assembles one complex object step by step; Abstract Factory returns ready-made related objects |
| **Prototype** | Clones existing instances instead of building new families from factories |

### Abstract Factory vs Factory Method

| | Abstract Factory | Factory Method |
|---|------------------|----------------|
| **Creates** | Families of related products (e.g. Windows UI kit) | One product type per factory subclass |
| **Client picks** | Which factory (family) to use | Which concrete factory creates the product |
| **Use when** | Products must stay consistent within a theme or platform | You need one creation point that varies by subclass |

## Summary

Abstract Factory produces matched sets of related objects. Pick a factory once, and every product it creates belongs to the same family.

---

Run `python3 main.py` to render Windows and Mac UI component families.
