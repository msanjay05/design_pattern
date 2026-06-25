# Factory Pattern

The **Factory pattern** is a creational design pattern. It provides an interface for creating objects without specifying their exact class at the call site. Creation logic is moved into a dedicated factory, so the rest of the application works with abstractions instead of concrete implementations.

## What Problem Does It Solve?

In many applications, the class you need to instantiate depends on runtime conditions: user input, configuration, environment, or business rules. Without a factory, that decision logic gets duplicated everywhere:

```python
# Creation logic scattered across the codebase
if payment_type == "card":
    processor = CreditCardProcessor()
elif payment_type == "paypal":
    processor = PayPalProcessor()
else:
    processor = BankTransferProcessor()

processor.charge(amount)
```

This leads to several problems:

| Problem | Description |
|---------|-------------|
| **Tight coupling** | Client code depends on concrete classes (`CreditCardProcessor`, `PayPalProcessor`, etc.) instead of a shared interface. |
| **Duplicated logic** | The same `if/elif` creation blocks appear in multiple places. |
| **Hard to extend** | Adding a new type means editing every place that creates objects. |
| **Hard to test** | You cannot easily swap implementations because clients construct objects directly. |
| **Violates Open/Closed Principle** | The system is open for modification every time a new product type is added. |

The Factory pattern solves this by **centralizing object creation** in one place and **returning objects through a common interface**.

## Core Idea

```
Client  →  asks Factory to create  →  Product (interface)
                                              ↑
                                    ConcreteProductA, B, C...
```

The client says *what* it needs (or the factory decides based on context). The factory handles *how* the object is built and *which* concrete class to use. The client only calls methods on the product interface.

## Why Is It Used?

1. **Encapsulation of creation logic** — Complex instantiation (reading config, validating input, choosing subclasses) stays inside the factory.
2. **Loose coupling** — Clients depend on abstractions, not concrete classes.
3. **Easier maintenance** — Change how objects are created in one place instead of across the codebase.
4. **Easier testing** — Inject a mock factory or stub product without changing client code.
5. **Consistency** — All objects of a given type are created the same way, with the same defaults and validation.

## Common Variants

### Simple Factory

A single class or function creates the right object based on a parameter.

```python
def create_notification(channel: str) -> Notification:
    if channel == "email":
        return EmailNotification()
    if channel == "sms":
        return SMSNotification()
    raise ValueError(f"Unknown channel: {channel}")
```

**Best for:** Straightforward selection by type, config, or string key.

**Trade-off:** The factory itself must be modified when new types are added (unless you use a registry/map).

### Factory Method

An abstract creator class defines a factory method. Each subclass overrides it to produce a different product.

```python
class NotificationService(ABC):
    @abstractmethod
    def create_notification(self) -> Notification: ...

    def notify(self, message: str) -> None:
        notification = self.create_notification()
        notification.send(message)


class EmailNotificationService(NotificationService):
    def create_notification(self) -> Notification:
        return EmailNotification()
```

**Best for:** Frameworks and class hierarchies where each subclass should produce its own product type.

**Trade-off:** More classes, but better alignment with the Open/Closed Principle — extend by adding subclasses instead of editing existing code.

### Abstract Factory

Provides an interface for creating **families of related objects** without specifying their concrete classes.

Example: A `UIFactory` that creates matching `Button`, `Checkbox`, and `Dialog` for either Windows or macOS. You pick one factory and get a consistent set of components.

**Best for:** Systems where products must be used together and belong to the same "family" or platform.

## When Should You Use It?

Use a Factory when:

- Object creation involves conditional logic or configuration.
- You want clients to depend on an interface, not concrete classes.
- The set of product types may grow over time.
- Creation is non-trivial (dependencies, setup steps, pooling, caching).
- You need to hide implementation details from the rest of the system.

Avoid it when:

- You always create exactly one concrete type with no variation.
- A plain constructor call is enough and unlikely to change.
- The extra indirection adds complexity without a clear benefit.

## Real-World Examples

| Domain | Factory creates... |
|--------|-------------------|
| Logging | `FileLogger`, `ConsoleLogger`, `CloudLogger` based on config |
| Databases | `MySQLConnection`, `PostgreSQLConnection` from a connection string |
| UI frameworks | Platform-specific widgets (Windows vs macOS) |
| Games | Different enemy or weapon types by level or difficulty |
| APIs | Serializers for JSON, XML, or Protobuf |
| Dependency injection | Services wired with the correct implementation at runtime |

## Benefits and Trade-offs

**Benefits**

- Single place to manage creation logic
- Clients work against interfaces
- Easier to add new product types
- Supports dependency inversion and testability

**Trade-offs**

- More classes and indirection
- Can be overkill for simple, stable object creation
- Simple Factory may still need changes when new types are added (unless designed with a registry)

## Relationship to Other Patterns

| Pattern | Difference |
|---------|------------|
| **Abstract Factory** | Creates *families* of related products; Factory Method creates *one* product per factory |
| **Builder** | Focuses on step-by-step construction of a *complex* object; Factory returns a fully built product |
| **Prototype** | Creates objects by cloning existing instances instead of calling `new`/constructors |
| **Singleton** | Ensures one instance exists; often used *inside* a factory but solves a different problem |

### Factory Method vs Abstract Factory vs Builder

| | Factory Method | Abstract Factory | Builder |
|---|----------------|------------------|---------|
| **Creates** | One product per factory subclass | Matched sets of related products | One complex object step by step |
| **Client knows** | Which factory to use | Which product family to use | Builder API and final `build()` call |
| **Use when** | Creation varies by subclass | Products must stay in the same theme/platform | Many optional parts and assembly steps |

## Summary

The Factory pattern separates **object creation** from **object use**. Instead of sprinkling `new`/constructor calls and conditionals throughout your code, you delegate creation to a factory that returns products through a shared interface. That keeps your system flexible, testable, and easier to extend as new types are introduced.

---

This folder contains a Python example (`products.py`, `simple_factory.py`, `factory_method.py`, `main.py`) that demonstrates Simple Factory and Factory Method in practice. Run `python3 main.py` to see both variants in action.
