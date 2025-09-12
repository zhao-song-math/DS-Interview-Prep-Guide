# 206. Reverse Linked List

[Leetcode ↗](https://leetcode.com/problems/reverse-linked-list/description/) | [Neetcode ↗](https://neetcode.io/solutions/reverse-a-linked-list)

<font color="#66BB6A">Easy</font> 

<span style="background-color:#F1F8E9; color:#558B2F; padding:3px 8px; border-radius:12px; font-size:12px; font-weight:bold;">Linked List</span> <span style="background-color:#F9FBE7; color:#827717; padding:3px 8px; border-radius:12px; font-size:12px; font-weight:bold;">Recursion</span>

## Description
Given the `head` of a singly linked list, reverse the list, and return *the reversed list*.

**Example 1:**
![EX1](pics/rev1ex1.jpg)

    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]

**Example 2:**
![EX2](pics/rev1ex2.jpg)

    Input: head = [1,2]
    Output: [2,1]

**Example 3:**

    Input: head = []
    Output: []

**Constraints:**
* The number of nodes in the list is the range `[0, 5000]`.
* `-5000 <= Node.val <= 5000`

**Follow up:**
* A linked list can be reversed either iteratively or recursively. Could you implement both?

---

## 题目解析


### 🔴 My Submission 1

**解题思路**

建立一个新链表，依次遍历原链表里的节点，将节点依次从头部插入新链表。例如原链表是`1  -> 2 -> 3 -> None`，依次插入节点可得新链表为：`1 -> None` -> `2 -> 1 -> None` -> `3 -> 2 -> 1 -> None`。

**代码如下：**

```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:  
        newHead  = head
        while head != None:
            cur = head.next
            cur.next = newHead
            newHead = cur
            head = head.next

        return newHead
```

❌ 以上代码不可行是因为错误的以为新建了链表，其实一直在对原链表进行操作，导致链表错误或循环陷入死循环。问题主要出自于这句`newHead = head`。还是以链表`1 -> 2 -> 3 -> None`为例，此时内存里有三个节点，`head`指向`1`这个节点：
```css
head ─┐
      ▼
   [1 | next] ───▶ [2 | next] ─▶ [3 | next] ─▶  None
```
**`newHead = head`意思是让`newHead`指向和`head`相同的节点，** 所以是：
```css
head ─┐
      ▼
   [1 | next] ───▶ [2 | next] ─▶ None
        🔼
newHead ┘
```
所以**代码执行流程为：**
* Start: `head=1`, `newHead=1`
* Iteration 1:
  * `cur = head.next` → `cur = 2`
  * `cur.next = newHead` →` 2.next = 1`
    因为`cur.next = newHead` 并不是在修改“变量 `cur` 本身”，而是在修改它指向的节点 `2` 的 `next` 属性, 由于 `2` 是原链表节点，所以原链表也被改了。
    Now: `1.next` 还是 `2`, `2.next` 是 1 → 原链表变成了cycle between 1 and 2
  * `newHead = cur` → `newHead = 2`
  * `head = head.next` → `head = 2` 
* Iteration 2:
  * `cur = head.next` → because of the earlier change 2.next is 1, so cur = 1 (不是预想的`3`)
  * you now go in a loop between 1 and 2 forever.


### 🟡 My Submission 2

**将🔴 My Submission 1 中的代码做一下修改：**
1. `newHead = head` → `newHead  = ListNode(head.val)` 这样就创建了一个新节点`newHead`，值与`head`值相同，但 `next` 属性不同，`newHead` 指向 `None`。
2. `cur = head.next` → `cur = ListNode(head.next.val)` 与 1 同理。
3. 另外加了`if head == None:`来考虑原链表是空的情况。
   
**代码如下：**
```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        if head == None:
            return head

        newHead  = ListNode(head.val)
        while head.next != None:
            cur = ListNode(head.next.val)
            cur.next = newHead
            newHead = cur
            head = head.next

        return newHead
```

**`ChatGPT`又将代码做了如下改进：**
1. 将循环里的`head.next`改成`head`，因为原有的逻辑有点绕
2. 添加了`curr = head`。这并不是必须的，但用了之后就不会对输入参数造成破坏，并且不会额外占用空间，因为`curr = head`没有消耗额外的链表节点空间。

```Python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = None
        curr = head

        while curr:
            node = ListNode(curr.val)  # 创建新节点
            node.next = newHead        # 插入到新链表前面
            newHead = node             # 更新新链表头
            curr = curr.next           # 原链表往后走

        return newHead
```
* **Time complexity:** $\mathcal{O}(n)$. 遍历所有节点
* **Space complexity:** $\mathcal{O}(n)$. 创建了新链表


### 🟢 Solution 1 (Iteratioon)

解决 [Linked List](Linked_List.md) 问题通常有两种方法：Iteration 和 Recursion。🟢 Solution 1 和 2 分别给出了这两种解法。

**解题思路**

Iteration 方法主要是依次遍历节点，并将前一个节点指向后一节点的链接断开，转而指向前一个节点的前一节点。比如由`1 -> 2 -> 3 -> None` 变成 `None <- 1`  `2 -> 3 -> None`。在断开节点`1`和节点`2`的链接后会将`2`丢失，为了避免丢失，需要在断开链接前 用一个变量存储`2`。**迭代步骤如下：**
1. 初始化两个指针`prev`和`curr`
```css
prev     head
 ▼        ▼
None     [1 | next] ───▶ [2 | next]───▶ [3 | next] ───▶ None
```
2. 存储节点`2`
```css
prev     head            temp
 ▼        ▼               ▼
None     [1 | next] ───▶ [2 | next]───▶ [3 | next] ───▶ None
```
3. 断开节点`1`和`2`的链接，并将`1`指向变量`prev`
```css
prev      head            temp
 ▼         ▼               ▼
None <--  [1 | next]      [2 | next]───▶ [3 | next] ───▶ None
```
4. 更新指针`prev`和`curr`的位置，分别向后移一位。
```css
          prev          head/temp
           ▼               ▼
None <--  [1 | next]      [2 | next]───▶ [3 | next] ───▶ None
```

**代码如下：**

```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        prev, curr = None, head # two pointers

        while curr:
            temp = curr.next # 存储 curr 所指向的下一个节点
            curr.next = prev # 将 curr 指向的节点 指向 prev
            
            # 更新前后指针，将两个指针同时向后移一位
            prev = curr
            curr = temp

        return prev
```
* **Time complexity:** $\mathcal{O}(n)$. 遍历所有节点
* **Space complexity:** $\mathcal{O}(1)$. 没有占用额外空间


### 🟢 Solution 2 (Recursion)

**解题思路**

此解使用 [Recursion](Recursion.md) 递归算法。以`1 -> 2 -> 3 -> None`为例。函数逐层调用，
1. 第一层调用`reverseList()`输入是`head`指向`1`
2. 第二层调用`reverseList()`输入是`head`指向`2`
3. 第三层调用`reverseList()`输入是`head`指向`3`

直到满足退出条件开始回退 逐层返回函数。首先是`2 -> 3 -> None`，这一层回退时需要做的是：
1. 更改`3`的`next`指针，让它指向`2`
2. 断开`2 -> 3` 之间的链接，让`2`指向`None`

**代码如下：**
```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        newHead = head

        # head为空，返回head; head不为空，返回尾节点。
        if not head or not head.next: 
            return head

        newHead = self.reverseList(head.next)
        head.next.next = head # reverse reference: head.next -> head
        head.next = None # 断开 head -> head.next, head 变成尾结点
      
        return newHead
```

以下以`1 -> 2 -> 3 -> None`为例来**逐步跟踪以上代码的递归实现：**

* 调用展开 （递归向下，直到尾节点）
  1. 调用`reverseList(head=1)`
     * `newHead = head` `newHead`指向`1`
     * `if not head or not head.next:` 不触发
     * 调用`reverseList(head=2)`
    栈上现在有： `frame1(head=1)`（等待 `reverseList(head=2)` 的返回）

  2. 调用`reverseList(head=2)`
     * `newHead = head` `newHead`指向`2`
     * `if not head or not head.next:` 不触发
     * 调用`reverseList(head=3)`
    栈上现在有： `frame1(head=1)`、`frame2(head=2)`（等待 `reverseList(head=3)` 的返回）

  3. 调用`reverseList(head=3)`
     * `newHead = head` `newHead`指向`3`
     * `if not head or not head.next:` `head.next=None`，返回`3`
    此时函数`reverseList(head=3)`返回，返回值（给上一个栈帧）是 `newHead=3`，代表反转后的子链表头是 `3` 并指向 `None`。
    
* 递归回退（unwinding）并做指针翻转
  1. 回到`frame2(head=2)`
    此时 `newHead`（从递归返回）是 `3`（代表子链表 `3 -> None`）。
    在`frame2(head=2)`中接下来执行的语句：
     ```Python
     head.next.next = head # 3.next=2，把 3 指向 2
     head.next = None # 把`2指向`3`的链接断开，让`2`指向`None`，此时局部链表为：`3 -> 2 -> None`

     return newHead # 仍然返回`3`
     ``` 
        此时全局链表的状态：
     ```rust
     1 -> 2 -> None    (因为 2.next 已被设为 None)
     newHead(sublist) -> 3 -> 2 -> None
     ```
  2. 回到`frame1(head=1)`
    此时`newHead`是 `3`（代表子链表 `3 -> 2 -> None`）。
    在`frame1(head=1)`中接下来执行的语句：
     ```Python
     head.next.next = head # 2.next=1，把 2 指向 1
     head.next = None # 把`1指向`2`的链接断开，让`1`指向`None`，此时局部链表为：`3 -> 2 -> 1 -> None`

     return newHead # 仍然返回`3`
     ``` 
  这就是最终返回给最初调用者的 `newHead: 3`，代表完整反转后的链表 `3 -> 2 -> 1 -> None`。


**复杂度分析**
* **Time complexity:** $\mathcal{O}(n)$. 每个节点恰好处理一次
* **Space complexity:** $\mathcal{O}(n)$. 递归栈深度为链表长度 n。