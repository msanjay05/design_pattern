# Bridge Pattern

The **Bridge pattern** splits a large class or set of closely related classes into two separate hierarchies — abstraction and implementation — which can evolve independently.

## What Problem Does It Solve?

When both the high-level logic (remote control) and low-level platform details (TV, radio, device drivers) vary, inheritance leads to a combinatorial explosion: `BasicTVRemote`, `AdvancedTVRemote`, `BasicRadioRemote`, etc.

Bridge separates "what you control" from "how it works."

## Core Idea

```
Abstraction (Remote) ──► Implementation (Device)
       │                         │
 BasicRemote                   TV
AdvancedRemote                Radio
```

The abstraction holds a reference to the implementation interface instead of extending every device type.

## Why Is It Used?

- Avoids permanent binding between abstraction and implementation
- Both hierarchies can be extended independently
- Hides implementation details from clients
- Replaces subclass explosion with composition

## When Should You Use It?

Use it when you have multiple dimensions of variation that would otherwise require multiplying subclasses.

Avoid it when a simple hierarchy or Strategy is sufficient.

## Real-World Examples

| Domain | Bridge separates... |
|--------|---------------------|
| UI | Widgets from rendering backends (OpenGL, DirectX) |
| Remotes | Control logic from device hardware |
| Messaging | Message format from transport (email, SMS) |
| Databases | ORM queries from database drivers |
| Graphics | Shapes from drawing APIs |

## Benefits and Trade-offs

**Benefits:** Cleaner class structure, independent evolution, better adherence to Single Responsibility.

**Trade-offs:** More classes and indirection; may be overkill for simple cases.

## Related Patterns

| Pattern | Difference |
|---------|------------|
| **Adapter** | Retrofits existing interfaces; Bridge designs separation between abstraction and implementation from the start |
| **Strategy** | Picks one behavior variant; Bridge decouples two independent dimensions so both can vary |
| **Abstract Factory** | Can create implementation objects used by the Bridge |

### Bridge vs Strategy

| | Bridge | Strategy |
|---|--------|----------|
| **Splits** | Abstraction hierarchy from implementation hierarchy | Algorithm choice from the context |
| **Dimensions** | Two axes that evolve independently (e.g. remote × device) | One task, multiple interchangeable ways to do it |
| **Use when** | Both interface and backend need to vary without combinatorial subclasses | Runtime algorithm swapping for a single operation |

## Summary

Bridge decouples an abstraction from its implementation so both can vary independently. It replaces "inheritance of implementations" with composition.

---

Run `python3 main.py` to control TV and radio with different remote abstractions.
