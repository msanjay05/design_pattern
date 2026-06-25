# Interpreter Pattern

The **Interpreter pattern** defines a representation for a language's grammar and provides an interpreter to evaluate sentences in that language.

## What Problem Does It Solve?

When you need to evaluate simple domain-specific languages, rules, or expressions repeatedly, embedding parsing logic in scattered conditionals becomes unmaintainable.

Interpreter models grammar rules as classes and builds an expression tree.

## Core Idea

```
Context + Expression Tree ──► interpret() ──► Result

Add(Variable("x"), Number(3)).interpret({"x": 10})  →  13
```

Each grammar rule is a class. Composite expressions combine simpler ones.

## Why Is It Used?

- Maps grammar rules directly to classes
- Easy to extend with new expression types
- Good for simple, frequently evaluated languages
- Makes rule evaluation explicit and composable

## When Should You Use It?

Use it for simple grammars with relatively stable rules: query filters, rule engines, template expressions.

Avoid it for complex languages — use parser generators or dedicated parsing libraries instead.

## Real-World Examples

| Domain | Interpreter evaluates... |
|--------|--------------------------|
| Search | Query syntax (`title:foo AND tag:bar`) |
| Spreadsheets | Cell formulas |
| Rules engines | Business conditions |
| SQL WHERE clauses | Filter expressions |
| Regular expressions | Pattern matching (internally) |

## Benefits and Trade-offs

**Benefits:** Clear grammar mapping, extensible expression tree, easy to compose expressions.

**Trade-offs:** Complex grammars lead to many classes; performance may lag specialized parsers.

## Related Patterns

| Pattern | Difference |
|---------|------------|
| **Composite** | Expression trees are often built as composite structures |
| **Visitor** | Traverses expression trees for evaluation, optimization, or export |
| **Strategy** | Swaps evaluation approach; Interpreter defines grammar as an object tree |

### Interpreter vs Visitor vs Strategy

| | Interpreter | Visitor | Strategy |
|---|-------------|---------|----------|
| **Models** | Grammar rules as objects | Operations separate from structure | Interchangeable algorithms |
| **Traversal** | Recursive evaluation of the tree | Double dispatch: element accepts visitor | Direct delegation, no tree required |
| **Use when** | Small domain-specific languages or rule engines | Many operations over a stable object structure | Picking among algorithm variants |

## Summary

Interpreter represents grammar as an object tree and evaluates it against a context. It suits small, domain-specific languages and rule systems.

---

Run `python3 main.py` to evaluate `(x + y) - 3` with a variable context.
