#  List [^1][^2]


列表是一种可修改的集合类型，其元素可以是数字、字符串等基本类型，也可以是列表、元组、字典等集合类型，甚至可以是自定义的类型。

创建一个列表，只要用逗号分隔的不同的数据，然后使用方括号括起来即可：

```
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
list = list(('a', 'b', 'c'))
print(len(letters))
```

列表元素的**读取和更新**：

```
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[2:5])
print(letters[10]) # list index out of range error
letters[-2] = 2019
print(letters[-2])
if 'a' in letters:
    print("letter 'a' is in the list")
```

**插入**：
list是一个可变的有序表，可以往list中追加元素到末尾：
```
>>> list = ['apple', 'pear']
>>> list.append('banana')
>>> list
['apple', 'pear', 'banana']
```

也可以把元素插入到指定的位置，比如索引号为`1`的位置：
```
>>> list.insert(1, 'orange') 
>>> list
['apple', 'orange', 'pear', 'banana']
```

复制一个list里的元素到另一个list里：
```
>>> list2 = list.copy()
>>> list2
['apple', 'orange', 'pear', 'banana']
```

**删除**：
要删除list末尾的元素，用`pop()`方法：
```
>>> list.pop()
'banana'
>>> list
['apple', 'orange', 'pear']
```

要删除指定位置的元素，用`pop(i)`方法，其中`i`是索引位置：
```
>>> list.pop(1)
'orange'
>>> list
['apple', 'pear']
```

也可以用`remove()`删除指定元素:
```
>>> list.remove('apple')
>>> list
['pear']
```

要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
```
>>> list[0] = 'kiwi'
>>> list
['kiwi]
```

**列表的运算：**

```
list1, list2 = [1, 2, 3], [4, 5, 6]
print(list1 + list2) # [1, 2, 3, 4, 5, 6]
print(list1 * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

**列表的其他函数：**
`sorted()`和`list.sort()`的差别可查看[[Python_Methods]]. 
```
letters = ['a', 'g', 'f', 'b', 'c', 'd', 'e']
sorted(letters) 
letters.sort() # The list is sorted permently
print(letters)
letters.reverse()
print(letters)
```

[^1]: [廖雪峰的官方网站](https://liaoxuefeng.com/books/python/basic/list-tuple/index.html)
[^2]: [图灵星球](https://turingplanet.org/2019/08/24/python%e6%95%b0%e6%8d%ae%e9%9b%86%e5%90%88%e7%b1%bb%e5%9e%8b-list-tuple-set-dictionary/)

## Backlinks
- [Leetcode问题目录](Leetcode问题目录.md)
- [20. Valid Parentheses](20-Valid_Parentheses.md)