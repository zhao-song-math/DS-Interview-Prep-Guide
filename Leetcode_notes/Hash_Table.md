<!-- TOC -->

<!-- /TOC -->

# Hash Table

## Hashmap (dict in Python)
使用键-值对(key-value pairs)存储，具有极快的查找和插入速度,不会随着key的增加而变慢；但是需要占用大量的内存，内存浪费多。
**定义**一个字典:
```
>>> d = {Abby: 95, Charlie: 75, Hudson: 85}
```
### 操作
**插入** key-value pair
```
>>> d['Daphne'] = 65
```
**删除** key-value pair, `pop(key)`, 返回value.
```
>>> d.pop('Abby')
95
>>> d
{Charlie: 75, Hudson: 85, Daphne: 65}
```
**查找**可以通过`in`判断key是否存在,返回true/false
```
>>> 'Abby' in d
False
```
或者可以使用`get(key)`,返回value 或者 false(如果key不存在)
```
>>> d.get('Abby')
None
>>> d.get('Abby', -1)
-1
```

## Hashset (set in Python)
set和dict类似，也是一组key的集合，但不存储value。set可以看成数学意义上的无序和无重复元素的集合, key不能重复。要创建一个set，用`{x,y,z,...}`列出每个元素：
```
>>> s = {1, 2, 3}
>>> s
{1, 2, 3}
```
或者提供一个list作为输入集合：
```
>>> s = set([1, 1, 2, 2, 3, 3])
>>> s
{1, 2, 3}
```
注意，传入的参数`[1, 1, 2, 2, 3, 3]`是一个list，而显示的`{1, 2, 3}`只是告诉你这个set内部有1，2，3这3个元素，重复元素在set中自动被过滤，显示的顺序也不表示set是有序的。

### 操作
**插入**: 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
```
>>> s.add(4)
>>> s
{1, 2, 3, 4}
>>> s.add(4)
>>> s
{1, 2, 3, 4}
```
**删除**： 通过`remove(key)`方法可以删除元素：
```
>>> s.remove(4)
>>> s
{1, 2, 3}
```
两个set可以做数学意义上的交集、并集等操作：
```
>>> s1 = {1, 2, 3}
>>> s2 = {2, 3, 4}
>>> s1 & s2
{2, 3}
>>> s1 | s2
{1, 2, 3, 4}
```

## Backlinks
- [Leetcode问题目录](Leetcode问题目录.md)
- [1. Two Sum](1-Two_Sum.md)
- [217. Contains Duplicate](217-Contains_Duplicate.md)
- [242. Valid Anagram](242-Valid_Anagram.md)