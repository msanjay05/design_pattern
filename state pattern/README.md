# State Pattern

The **State pattern** lets an object alter its behavior when its internal state changes. The object appears to change its class.

## What Problem Does It Solve?

Large state machines implemented with `if/elif` or `switch` become unmaintainable:

```python
if state == "idle":
    ...
elif state == "has_coin":
    ...
```

Every new state adds branches everywhere. State pattern gives each state its own class with behavior localized there.

## Core Idea

```
Context ──► State Interface ──► ConcreteStateA
                           └──► ConcreteStateB
```

The context delegates to the current state object. State transitions replace the current state with another.

## Why Is It Used?

- Eliminates sprawling conditionals
- Makes state-specific behavior explicit and localized
- Simplifies adding new states
- Models finite state machines cleanly

## When Should You Use It?

Use it when an object's behavior depends on its state and it transitions between well-defined states.

Avoid it when there are only one or two simple states, or when transitions are not meaningful.

## Real-World Examples

| Domain | States include... |
|--------|-------------------|
| Vending machines | Idle, has coin, dispensing |
| Orders | Pending, paid, shipped, delivered |
| Media players | Stopped, playing, paused |
| TCP connections | Listen, established, closed |
| Workflows | Draft, review, approved, rejected |

## Benefits and Trade-offs

**Benefits:** Clear state logic, easier extension, aligns with Open/Closed Principle.

**Trade-offs:** More classes; transitions must be managed carefully to avoid invalid states.

## Related Patterns

- **Strategy:** Similar structure; Strategy is usually chosen externally and does not imply transitions
- **Finite State Machine:** State pattern is the OOP expression of an FSM
- **Command:** Can trigger state transitions

## Summary

State encapsulates state-specific behavior in separate classes. The context delegates to the active state, making complex state machines readable and maintainable.

---

Run `python3 main.py` to operate a vending machine across idle and has-coin states.
