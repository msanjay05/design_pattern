# Memento Pattern

The **Memento pattern** captures and externalizes an object's internal state so it can be restored later, without exposing implementation details.

## What Problem Does It Solve?

You need undo, rollback, or snapshot capability, but exposing all internal fields breaks encapsulation. Clients should not need to know how state is stored inside the originator.

## Core Idea

```
Originator ──save()──► Memento (snapshot)
           ◄─restore()──

Caretaker stores mementos but cannot modify them
```

The originator creates and reads mementos. A caretaker holds history but treats mementos as opaque.

## Why Is It Used?

- Implements undo/redo cleanly
- Preserves encapsulation while saving state
- Enables checkpoints and rollback
- Separates state storage from business logic

## When Should You Use It?

Use it when you must save and restore object state and direct field access would violate encapsulation.

Avoid it when state is huge, snapshots are frequent, or immutable data structures make history unnecessary.

## Real-World Examples

| Domain | Memento enables... |
|--------|---------------------|
| Text editors | Undo/redo |
| Games | Save/load checkpoints |
| Transactions | Rollback to prior state |
| Form wizards | Step back without losing data |
| Version control | Snapshot commits |

## Benefits and Trade-offs

**Benefits:** Clean undo support, encapsulated state capture, caretaker/origator separation.

**Trade-offs:** Memory cost for many snapshots; caretaker lifecycle must be managed.

## Related Patterns

| Pattern | Difference |
|---------|------------|
| **Command** | Undo often uses mementos to restore prior state after executing a command |
| **State** | State objects can be saved as mementos for rollback |
| **Prototype** | Clones objects to create new instances; Memento restores existing instances |

### Memento vs Prototype vs Command

| | Memento | Prototype | Command |
|---|---------|-----------|---------|
| **Purpose** | Snapshot and restore object state | Copy an object to make a new one | Encapsulate an action with optional undo |
| **Direction** | Backward in time (undo/restore) | Forward to new instances | Execute now, possibly reverse later |
| **Use when** | Editors, games, transactional rollback | Expensive object setup | Action history, macros, queued jobs |

## Summary

Memento saves object state in an opaque snapshot for later restoration. It powers undo, redo, and checkpoint features without breaking encapsulation.

---

Run `python3 main.py` to edit text and restore a previous version from history.
