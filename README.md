# Python Dataclasses Guide

## Introduction
Dataclasses simplify creating classes focused on storing data by automatically generating special methods like `__init__`, `__repr__`, and `__eq__`.

## Basic Usage

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    location: str = "Unknown"
```

## Dataclasses vs Regular Classes

### Attribute Declaration
**Regular Classes**:
- Attributes are defined and initialized in `__init__`
```python
class Person:
    def __init__(self, name, age, location="Unknown"):
        self.name = name
        self.age = age
        self.location = location
```

**Dataclasses**:
- Attributes are declared at class level with type hints
- Default values are specified directly in the class body
```python
@dataclass
class Person:
    name: str
    age: int
    location: str = "Unknown"  # Default value
```

### Generated Methods
Dataclasses automatically generate:
- `__init__`: Creates constructor with parameters for each attribute
- `__repr__`: Creates string representation
- `__eq__`: Implements equality comparison
- Optional: `__hash__`, `__lt__`, etc.

## Key Features

- **Init-only fields**: Fields used in `__init__` but not stored as instance attributes
- **Post-initialization**: `__post_init__` for custom initialization logic
- **Field options**: Use `field()` for fine-grained control
```python
@dataclass
class User:
    id: int = field(compare=False)
    password: str = field(repr=False)
```

## Common Patterns

### Immutable Dataclasses
```python
@dataclass(frozen=True)
class Config:
    host: str
    port: int = 8000
```

### Default Values with Computation
```python
from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Event:
    name: str
    timestamp: datetime = field(default_factory=datetime.now)
```

## Example

From the provided example:
```python
@dataclass 
class Lendbuzz:
    location: str
    mode: str
    mission: str
    contact: str
        
    def is_hiring(self) -> bool:
        return True
    
    # Methods for job description and requirements
```

This creates a class with:
- Automatically generated `__init__`, `__repr__` and `__eq__`
- Parameters matching declared attributes
- Type hints for better code documentation

## Best Practices

1. Use type hints consistently for clarity
2. Use `field(default_factory=...)` for mutable defaults
3. Consider `frozen=True` for immutable data objects
4. Use `__post_init__` for complex initialization logic
