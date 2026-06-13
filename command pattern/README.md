# Command Pattern

The **Command pattern** encapsulates a request as an object, letting you parameterize clients, queue operations, log actions, and support undo.

## What Problem Does It Solve?

Direct method calls tie the invoker to specific receivers. You cannot easily queue requests, replay them, or reverse them. UI buttons, macros, and transaction systems need to treat actions as first-class objects.

## Core Idea

```
Invoker ──► Command.execute() ──► Receiver
         └── Command.undo()
```

Each command object knows how to perform and optionally reverse an action.

## Why Is It Used?

- Decouples who invokes an action from who performs it
- Supports undo/redo and action history
- Enables macro scripts and job queues
- Allows logging, auditing, and delayed execution

## When Should You Use It?

Use it when actions should be treated as objects: undo stacks, task schedulers, remote execution, or configurable UI commands.

Avoid it when operations are trivial one-liners with no need for queuing or reversal.

## Real-World Examples

| Domain | Commands represent... |
|--------|------------------------|
| Text editors | Cut, copy, paste, undo |
| Smart home | Turn on lights, set thermostat |
| Transactions | Debit/credit with rollback |
| Games | Player actions in replay systems |
| APIs | Async jobs submitted to a worker queue |

## Benefits and Trade-offs

**Benefits:** Flexible invocation, undo support, composable macros, clear separation of concerns.

**Trade-offs:** More classes; complex undo may require storing substantial state.

## Related Patterns

- **Strategy:** Encapsulates algorithms; Command encapsulates requests with optional undo
- **Memento:** Stores state for undo restoration
- **Composite:** Commands can be grouped into macro commands

## Summary

Command turns requests into objects. That makes actions queueable, reversible, and decoupled from the code that triggers them.

---

Run `python3 main.py` to turn on a light and undo the action with a remote control.
