# Data Structures and Lists

## Introduction

In data science and Python programming, lists are one of the most important structures for storing collections of data. They allow us to organize multiple items together.

## Creating Lists

You can create a list using square brackets:

```python
numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]
```

## Accessing List Elements

Lists are indexed starting at 0. You can access elements using their index:

```python
first = numbers[0]  # Gets 1
second = names[1]   # Gets "Bob"
```

## Adding Elements to Lists

You can add elements using the `append()` method:

```python
numbers.append(6)
# Now numbers = [1, 2, 3, 4, 5, 6]

# You can also use extend() to add multiple items
numbers.extend([7, 8, 9])
```

## Common Mistakes with Lists

A common error is confusing list indexing with counting. Remember:
- Lists are 0-indexed (the first element is at index 0)
- The last element at index length - 1

```python
my_list = ["a", "b", "c"]
my_list[0]  # Correct: Gets "a"
my_list[3]  # WRONG: This will cause an IndexError because there is no index 3
```

## List Methods

Here are the most important list methods:

| Method | Description | Example |
|--------|-------------|---------|
| `append(x)` | Adds x to the end | `lst.append(5)` |
| `remove(x)` | Removes first x | `lst.remove(5)` |
| `pop()` | Removes and returns last item | `item = lst.pop()` |
| `insert(i, x)` | Inserts x at index i | `lst.insert(2, 5)` |
| `sort()` | Sorts the list in place | `lst.sort()` |

## Summary

Lists are fundamental data structures in Python. Understanding how to create, access, and modify lists is essential for data science work. Practice with different list operations to become comfortable with them.

---

**Next Lesson:** Dictionary Data Structures
