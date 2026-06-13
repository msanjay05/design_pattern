# Template Method Pattern

The **Template Method pattern** defines the skeleton of an algorithm in a base class, deferring some steps to subclasses.

## What Problem Does It Solve?

Multiple classes follow the same high-level process but differ in specific steps. Duplicating the overall flow in each subclass leads to copy-paste and drift. You want one place for the algorithm structure and hooks for customization.

## Core Idea

```
BaseClass.template_method():
    step1()        # concrete in base
    step2()        # abstract — subclass implements
    step3()        # abstract — subclass implements
    step4()        # concrete in base
```

Subclasses override specific steps without changing the sequence.

## Why Is It Used?

- Reuses common algorithm structure
- Enforces consistent process across variants
- Lets subclasses customize only what differs
- Implements "Hollywood Principle": don't call us, we'll call you

## When Should You Use It?

Use it when several classes share the same algorithm steps in the same order but differ in details.

Avoid it when the algorithm structure itself varies, or when composition (Strategy) is more flexible than inheritance.

## Real-World Examples

| Domain | Template defines... |
|--------|---------------------|
| Data mining | Open → parse → analyze → report |
| Web frameworks | Request lifecycle hooks |
| Build tools | Compile pipeline with customizable stages |
| Games | Turn sequence with subclass-specific actions |
| Testing | Setup → run test → teardown |

## Benefits and Trade-offs

**Benefits:** DRY algorithm structure, controlled extension points, consistent workflows.

**Trade-offs:** Inheritance-based (less flexible than Strategy); subclasses constrained to the template's skeleton.

## Related Patterns

- **Strategy:** Replaces algorithm via composition; Template Method varies steps via inheritance
- **Factory Method:** Often used inside template steps to create objects
- **Hook methods:** Optional override points in the template (not always required)

## Summary

Template Method locks in the algorithm's structure in a base class while subclasses fill in the variable steps. It is ideal for shared workflows with customizable details.

---

Run `python3 main.py` to mine PDF and JSON data using the same pipeline.
