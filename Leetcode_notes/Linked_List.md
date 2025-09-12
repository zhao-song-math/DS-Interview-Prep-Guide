# Linked List 链表[^1][^2]

## 定义
**如何定义链表？**
 1. 先定义一个一个的节点
```Python
node1 = ListNode(1) # 先给 node 赋值，next 指针默认是 None
node2 = ListNode(2)
node3 = ListNode(3)
```
 2. 再把每个节点的关系表示出来
```Python
node1.next = node2
node2.next = node3 # 注意：这里 node3.next 是 None
```

## 链表的类型

## 链表的基本操作

#### 插入

#### 删除

#### 查找（遍历）

#### 更新

## 解决链表问题的方法

### Iteration: 通常使用[Two Pointers](Two_Pointers.md)来解决。

### Recursion


[^1]: [CSDN博客](https://blog.csdn.net/weixin_46312449/article/details/106792544)
[^2]: [图灵星球](https://turingplanet.org/2020/06/20/%e9%93%be%e8%a1%a8linked-list%e9%a2%98%e5%9e%8b%e5%a5%97%e8%b7%af%e3%80%90leetcode%e5%88%b7%e9%a2%98%e5%a5%97%e8%b7%af%e6%95%99%e7%a8%8b4%e3%80%91/)