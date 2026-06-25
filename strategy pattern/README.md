# Strategy Pattern

The **Strategy pattern** defines a family of interchangeable algorithms, encapsulates each one, and makes them swappable at runtime.

## What Problem Does It Solve?

Conditional logic for behavior variants clutters classes:

```python
if payment == "card":
    ...
elif payment == "paypal":
    ...
```

Every new algorithm requires editing existing code. Strategy moves each variant into its own class behind a common interface.

## Core Idea

```
Context ──► Strategy Interface ──► ConcreteStrategyA
                              └──► ConcreteStrategyB
```

The context delegates work to the current strategy. You can change strategies without changing the context's structure.

## Why Is It Used?

- Eliminates large conditional blocks
- Makes algorithms independently testable
- Allows runtime switching of behavior
- Follows Open/Closed Principle

## When Should You Use It?

Use it when you have multiple ways to perform a task and want to switch between them dynamically.

Avoid it when there is only one algorithm or the variation is trivial.

## Real-World Examples

| Domain | Strategies handle... |
|--------|----------------------|
| Payments | Card, PayPal, bank transfer |
| Routing | Fastest, cheapest, scenic |
| Compression | ZIP, GZIP, Brotli |
| Validation | Strict, lenient, regional rules |
| Games | Easy, normal, hard AI behavior |

## Benefits and Trade-offs

**Benefits:** Cleaner code, isolated algorithms, flexible configuration.

**Trade-offs:** More classes; clients must understand which strategy to choose.

## Related Patterns

| Pattern | Difference |
|---------|------------|
| **State** | Same delegation structure, but states represent phases and trigger transitions; Strategy represents swappable algorithms chosen externally |
| **Template Method** | Uses inheritance for algorithm skeleton; Strategy uses composition to replace the whole algorithm |
| **Command** | Encapsulates actions (often with undo); Strategy encapsulates how to perform a task |

### Strategy vs State

Both patterns use a context delegating to objects behind a common interface. In this repo, compare `strategy.py` (checkout payments) with `../state pattern/state.py` (vending machine).

| | Strategy | State |
|---|----------|-------|
| **Why** | Multiple ways to do the same job | Behavior depends on the object's current phase |
| **Switching** | `checkout.set_strategy(PayPalPayment())` from outside | `IdleState` sets `machine.state = HasCoinState()` after an event |
| **Coupling** | Strategies do not know about each other | States know valid transitions |
| **Use when** | You have swappable algorithms (payment, routing, compression) | You have a state machine (orders, connections, workflows) |

## Summary

Strategy packages interchangeable behaviors behind one interface. The context uses whichever strategy fits the situation, without conditional spaghetti.

---

Run `python3 main.py` to switch payment strategies at checkout.
