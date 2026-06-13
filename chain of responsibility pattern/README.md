# Chain of Responsibility Pattern

The **Chain of Responsibility pattern** passes a request along a chain of handlers. Each handler decides whether to process the request or forward it to the next handler.

## What Problem Does It Solve?

Multiple components may need to handle a request (auth, rate limiting, logging, business logic), but you do not want the sender coupled to every handler or a rigid central dispatcher.

## Core Idea

```
Request ──► Handler A ──► Handler B ──► Handler C ──► result / None
              │              │              │
           may handle    may handle     may handle
           or pass       or pass        or pass
```

Handlers link together dynamically. The request travels until someone handles it or the chain ends.

## Why Is It Used?

- Decouples senders from receivers
- Lets you add/reorder handlers without changing sender code
- Supports flexible processing pipelines
- Each handler focuses on one concern

## When Should You Use It?

Use it when more than one object may handle a request and the handler is not known in advance.

Avoid it when there is always exactly one handler or when guaranteed processing is required (a chain may leave requests unhandled).

## Real-World Examples

| Domain | Chain includes... |
|--------|-------------------|
| Web middleware | Auth, rate limit, validation, controller |
| Support systems | Tier 1, tier 2, tier 3 escalation |
| Logging | Filters by level, source, destination |
| Event handling | UI event propagation |
| Approval workflows | Manager, director, VP sign-off |

## Benefits and Trade-offs

**Benefits:** Loose coupling, flexible ordering, single-responsibility handlers.

**Trade-offs:** No guarantee of handling; debugging flow can be harder; performance overhead for long chains.

## Related Patterns

- **Decorator:** Similar chaining structure but adds behavior every time
- **Composite:** Can be part of a chain in tree structures
- **Command:** Handlers can be command objects

## Summary

Chain of Responsibility routes a request through linked handlers until one processes it. It is ideal for middleware, pipelines, and escalation flows.

---

Run `python3 main.py` to pass API requests through auth, rate limit, and business handlers.
