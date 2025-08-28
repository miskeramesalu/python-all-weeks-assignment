# Person–Doctor OOP (Python)

This project demonstrates **Object-Oriented Programming (OOP)** concepts in Python using a simple `Person` class and a `Doctor` subclass.  
It covers **encapsulation, inheritance, and method overriding**.

---

## 🔑 Key Concepts

1. **Encapsulation**  
   - The `age` attribute is private (`__age`) and can only be accessed using the getter method `get_age()`.

2. **Inheritance**  
   - The `Doctor` class inherits from the `Person` class, reusing its attributes and methods.

3. **Method Overriding**  
   - The `introduce()` method is overridden in the `Doctor` class to give a specialized introduction.

---

## 📂 Code Overview

### Parent Class: `Person`
- Attributes: `name`, `__age` (private), `city`
- Methods:
  - `introduce()` → Introduces the person.
  - `get_age()` → Getter to safely access the private age attribute.

### Child Class: `Doctor`
- Inherits from `Person`.
- Adds an attribute: `specialization`.
- Overrides `introduce()` to include doctor-specific information.

---

## 🧪 Example Usage

```python
# Create objects
person1 = Person("Qufa", 40, "Addis Ababa")
doctor1 = Doctor("Qufa", 40, "Addis Ababa", "Cardiologist")

# Test
print(person1.introduce())       # My name is Qufa, and I live in Addis Ababa.
print(doctor1.introduce())       # Dr. Qufa, a Cardiologist specialist, is practicing in Addis Ababa.
print(doctor1.get_age())         # 40
✅ Output
pgsql
Copy code
My name is Qufa, and I live in Addis Ababa.
Dr. Qufa, a Cardiologist specialist, is practicing in Addis Ababa.
40
🚀 How to Run
Save the Python code in a file, e.g., person_doctor.py.

Open a terminal and run:

bash
Copy code
python person_doctor.py
📘 Learning Points
Use __ prefix to create private attributes.

Always provide getter methods to safely access private data.

Subclasses can extend or override parent methods for customization.