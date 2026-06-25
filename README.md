# Design Patterns

A collection of all **23 Gang of Four (GoF)** design pattern examples in Python. Each folder contains a runnable demo and a README with a generic explanation of the pattern.

## Patterns

### Creational — object creation

| Pattern | Folder | Description |
|---------|--------|-------------|
| Factory | `factory pattern/` | Centralizes object creation behind an interface |
| Abstract Factory | `abstract factory pattern/` | Creates families of related objects |
| Builder | `builder pattern/` | Constructs complex objects step by step |
| Prototype | `prototype pattern/` | Creates objects by cloning |
| Singleton | `singleton pattern/` | Ensures only one instance exists |

### Structural — composition and relationships

| Pattern | Folder | Description |
|---------|--------|-------------|
| Adapter | `adapter pattern/` | Makes incompatible interfaces work together |
| Bridge | `bridge pattern/` | Separates abstraction from implementation |
| Composite | `composite pattern/` | Treats individual objects and groups uniformly |
| Decorator | `decorator pattern/` | Adds behavior dynamically via wrapping |
| Facade | `facade pattern/` | Simplifies access to a complex subsystem |
| Flyweight | `flyweight pattern/` | Shares common state to reduce memory use |
| Proxy | `proxy pattern/` | Controls access to another object |

### Behavioral — communication and responsibility

| Pattern | Folder | Description |
|---------|--------|-------------|
| Chain of Responsibility | `chain of responsibility pattern/` | Passes requests through a handler chain |
| Command | `command pattern/` | Encapsulates requests as objects |
| Interpreter | `interpreter pattern/` | Evaluates grammar-based expressions |
| Iterator | `iterator pattern/` | Traverses collections without exposing internals |
| Mediator | `mediator pattern/` | Centralizes communication between objects |
| Memento | `memento pattern/` | Saves and restores object state |
| Observer | `observer pattern/` | Notifies dependents when state changes |
| State | `state pattern/` | Changes behavior based on internal state |
| Strategy | `strategy pattern/` | Swaps interchangeable algorithms at runtime |
| Template Method | `template method pattern/` | Defines algorithm skeleton with customizable steps |
| Visitor | `visitor pattern/` | Adds operations without changing element classes |

## How to Run

```bash
cd "<pattern folder>"
python3 main.py
```

Example:

```bash
cd "visitor pattern"
python3 main.py
```

Run all demos:

```bash
for dir in *pattern*; do echo "=== $dir ===" && (cd "$dir" && python3 main.py); done
```

## Suggested Learning Order

1. **Strategy**, **Observer**, **Iterator** — common in everyday code
2. **Factory**, **Builder**, **Singleton** — creational patterns you'll use often
3. **Decorator**, **Adapter**, **Facade**, **Proxy** — integration and extension
4. **Composite**, **Bridge**, **Flyweight** — structural composition
5. **State**, **Command**, **Chain of Responsibility**, **Mediator** — behavior and workflows
6. **Template Method**, **Visitor**, **Memento**, **Interpreter** — advanced specialization

## Commonly Confused Patterns

State and Strategy look almost identical in code — both use a context that delegates to interchangeable objects behind an interface. The difference is **intent and who controls the switch**.

| Aspect | State | Strategy |
|--------|-------|----------|
| **Purpose** | Model behavior that changes as the object moves through defined states | Swap one algorithm for another at runtime |
| **Who changes the active object** | The current state object (or context reacting to events) | The client or context, usually explicitly |
| **Transitions** | States define valid next states (e.g. idle → has coin) | Strategies are independent; no built-in transitions |
| **Mental model** | Finite state machine | Pluggable algorithm |
| **Example** | Vending machine: idle, has coin, dispensing | Checkout: credit card, PayPal, bank transfer |

**Rule of thumb:** If behavior changes because of *what phase the object is in*, use **State**. If behavior changes because the *user or caller picks a different way to do the same task*, use **Strategy**.

Other pairs that are often mixed up:

| Pair | Key difference |
|------|----------------|
| **Strategy vs Template Method** | Strategy swaps whole algorithms via composition; Template Method fixes the skeleton in a base class and subclasses override steps via inheritance |
| **Bridge vs Strategy** | Bridge separates two independent dimensions (abstraction vs implementation); Strategy picks one behavior variant for a single task |
| **Command vs Strategy** | Command encapsulates a request (often with undo/history); Strategy encapsulates how to perform a task |
| **Decorator vs Proxy** | Decorator adds responsibilities; Proxy controls access (lazy load, security, remote) |
| **Adapter vs Facade** | Adapter makes one incompatible interface fit another; Facade simplifies a whole subsystem behind one entry point |
| **Observer vs Mediator** | Observer broadcasts changes to many listeners; Mediator routes communication through a central hub |
| **Memento vs Prototype** | Memento saves snapshots for undo/restore; Prototype clones objects to create new instances |
| **Composite vs Decorator** | Composite groups children into a tree; Decorator wraps one object to add behavior |
