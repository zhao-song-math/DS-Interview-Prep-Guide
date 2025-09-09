# Sorting

## `sorted()` VS `list.sort()`

**In-place modification vs. New List Creation:**
* `list.sort()`: This is a method of list objects and sorts the list in-place, meaning it modifies the original list directly and returns None.
* `sorted()`: This is a built-in function that returns a new sorted list without modifying the original iterable.

**Applicability:**
* `list.sort()`: Can only be used on list objects.
* `sorted()`: Can be used on any iterable (e.g., lists, tuples, strings, dictionaries, generators).

**Return Value:**
* `list.sort()`: Returns None.
* `sorted()`: Returns a new sorted list.

**Memory Usage:**
* `list.sort()`: Generally more memory-efficient for lists as it sorts in-place and does not create a new object.
* `sorted()`: Creates a new list, which can consume more memory, especially for large datasets.

## Backlinks
- [Leetcode 笔记目录](Leetcode笔记目录.md)
- [242. Valid Anagram](242-Valid_Anagram.md)