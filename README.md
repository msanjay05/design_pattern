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
