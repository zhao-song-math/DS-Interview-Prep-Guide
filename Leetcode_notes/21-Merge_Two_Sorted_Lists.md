# Merge Two Sorted Lists

[Leetcode ↗](https://leetcode.com/problems/merge-two-sorted-lists/description/) | [Neetcode ↗](https://neetcode.io/solutions/merge-two-sorted-lists)

<font color="#66BB6A">Easy</font> 

<span style="background-color:#F1F8E9; color:#558B2F; padding:3px 8px; border-radius:12px; font-size:12px; font-weight:bold;">Linked List</span> <span style="background-color:#F9FBE7; color:#827717; padding:3px 8px; border-radius:12px; font-size:12px; font-weight:bold;">Recursion</span>

### Description  
You are given the heads of two sorted linked lists `list1` and `list2`.  

Merge the two lists into one **sorted** list. The list should be made by splicing together the nodes of the first two lists.  

Return *the head of the merged linked list*.

---

### Examples

**Example 1:**
![merge_ex1](pics/merge_ex1.jpg)

    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]

**Example 2:**

    Input: list1 = [], list2 = []
    Output: []

**Example 3:**

    Input: list1 = [], list2 = [0]
    Output: [0]


**Constraints**
- The number of nodes in both lists is in the range `[0, 50]`.  
- `-100 <= Node.val <= 100`  
- Both `list1` and `list2` are sorted in **non-decreasing** order.  


## 题目解析


### 🟡 My Submission (Iteration)

#### 解题思路
分别用一个指针遍历两个[链表](Linked_List.md)，逐个比较两个指针指向的节点值，值小的加入合并链表。

❌ 思路正确但是考虑具体步骤时考虑的太复杂，导致代码太乱，总有考虑不完善的情况出现，代码提交不成功。看了答案解决了自己的困惑：
1. Dummy node simplifies handling the head. 巧妙地在链表最开始用了一个`dummy`节点作为头结点，相当于最后的链表是`dummy`节点指向合并后的链表，最后返回`dummy.next`
2. 只考虑了`list1`和`list2`都不为空的情况，其他情况只用`curr.next = l1 or l2`就非常巧妙地解决了，其他情况如下：
   - 初始`list1`和`list2`都不为空，但在循环结束时，其中有一个还有剩余节点
   - 初始`list1`和`list2`有一个为空
   - 对于初始`list1`和`list2`都为空的情况，也能通过`dummy.next`返回正确输出
 
#### 代码

```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1, l2 = list1, list2 # solution: 没有此句
        dummy = curr = ListNode()

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = ListNode(l1.val) # solution: curr.next = l1
                l1 = l1.next
                
            else:
                curr.next = ListNode(l2.val) # solution: curr.next = l2
                l2 = l2.next
            
            curr = curr.next

        curr.next = l1 or l2
           
        return dummy.next
```

**Differences between My Submission and Solution:**
Solution中没有执行`l1, l2 = list1, list2`，用了原有的`list1`和`list2`；并且在给`curr.next`赋值时没有创建新节点，而是直接用了原来两个链表里的节点，不同之处在于，值都相同但`next`指针不同。
* **My Submission**: Copies values into new nodes → original lists remain untouched.
* **Solution**: Directly reuses existing nodes → faster and uses less memory, but original lists get modified.

#### 复杂度分析
* **Time complexity:** $\mathcal{O}(m+n)$. 两个链表里的每个节点都被访问。
* **Space complexity:** $\mathcal{O}(m+n)$. 创建新的节点得到了新的链表，但是 Solution 的空间复杂度是$\mathcal{O}(1)$，因为没有创建新节点。


### 🟢 Solution 1 (Recursion)

#### 解题思路
**核心思想：** 使用[递归算法](Recursion.md)。值小的节点先放，递归合并两链表剩下的部分。
- **递归过程**：将两个链表当前节点值较小的那个节点作为当前合并链表的“头结点”，并把问题缩小（从两个链表里“去掉”这个“头结点”，只考虑剩余几点）
- **终止条件**：一个链表空了，直接把另一个链表挂上去
- **返回结果**
  - 每一层递归返回的都是“从当前选择的结点开始的合并结果”
  - 递归最内层返回的是最终合并链表的头结点
- 根据两链表当前节点 **选择 合并链表当前头节点**
  - 比较 `list1.val` 和 `list2.val`：
    - 如果 `list1.val <= list2.val`，说明 `list1` 指向的结点应该排在前面：
      - 把 `list1.next` 指向 合并之后的结果（即 `merge(list1.next, list2)`）。
      - 返回 `list1`, 即合并链表当前头节点。
    - 否则，说明 `list2` 指向的结点更小：
      - 把 `list2.next` 指向 合并之后的结果（即 `merge(list1, list2.next)`）。
      - 返回 `list2`, 即合并链表当前头节点。
#### 代码
```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        if not list1: # 包含 list1为空list2不为空 和 list1和list2都为空 的情况
            return list2

        if not list2: # list1不为空list2为空
            return list1        

        if list1 and list2:
            if list1.val <= list2.val: # list1指向的结点应该排在前面
                list1.next = self.mergeTwoLists(list1.next, list2) # list1从list1.next开始，问题规模缩小
                return list1
            else: # list2指向的结点应该排在前面
                list2.next = self.mergeTwoLists(list1, list2.next) # list1从list1.next开始，问题规模缩小
                return list2
```
#### 代码流程

0. 初始链表
    ```css
     list1
       ▼
       1 ───▶ 2 ───▶ None

     list2
       ▼
       1 ───▶ 3 ───▶ None
    ``` 
1. **递进（往下调用）**
   1. 第一次调用: `mergeTwoLists([1 -> 2],[1 -> 3])`
      1. 比较`list1.val=1`和`list2.val=1`
      2. 因为`list1.val=1 <= list2.val=1`, pick`list1`作为合并链表 当前 头结点
      3. `list1.next = mergeTwoLists(list1.next,list2)` -> `1.next=mergeTwoLists([2],[1 -> 3])`

      当前状态
      ```css
            list1
              ▼
              2 ───▶ None

      list2
       ▼
       1 ───▶ 3 ───▶ None

       1(list1) ───▶ ? （等待 mergeTwoLists([2],[1 -> 3]) 的结果）
       ``` 

   2. 第二次调用: `mergeTwoLists([2],[1 -> 3])`
      1. 比较`list1.val=2`和`list2.val=1`
      2. 因为`list1.val=2 > list2.val=1`, pick`list2`作为合并链表 当前 头结点
      3. `list2.next = mergeTwoLists(list1,list2.next)` ---> `1.next=mergeTwoLists([2],[3])` 

      当前状态
      ```css
            list1
              ▼
              2 ───▶ None

            list2
              ▼
              3 ───▶ None

       1(list1) ───▶ ?（等待 mergeTwoLists([2],[1 -> 3]) 的结果）

       1(list2) ───▶ ?（等待 mergeTwoLists([2],[3]) 的结果）
       ``` 

   3. 第三次调用: `mergeTwoLists([2],[3])`
      1. 比较`list1.val=2`和`list2.val=3`
      2. 因为`list1.val=2 <= list2.val=3`, pick`list1`作为合并链表 当前 头结点
      3. `list1.next = mergeTwoLists(list1.next,list2)` ---> `2.next=mergeTwoLists([],[3])` 

      当前状态
      ```css
                    list1
                      ▼
                     None

            list2
              ▼
              3 ───▶ None

       1(list1) ───▶ ?（等待 mergeTwoLists([2],[1 -> 3]) 的结果）

       1(list2) ───▶ ?（等待 mergeTwoLists([2],[3]) 的结果）

       2 ───▶ ?（等待 mergeTwoLists([],[3]) 的结果）
       ``` 
   4. 第四次调用(base case): `mergeTwoLists([],[3])`
      1. 比较`list1=None` ---> 返回`list2=3`
      2. 递归停止

2. **回退（逐层返回结果）**
   1. 从第四层回退
      1. 返回`mergeTwoLists([], [3])=[3]`
      2. 所以上一层的`2`指向`3`
  
      当前状态
      ```css
       1(list1) ───▶ ?（等待 mergeTwoLists([2],[1 -> 3]) 的结果）

       1(list2) ───▶ ?（等待 mergeTwoLists([2],[3]) 的结果）

       2 ───▶ 3
       ``` 
   2. 第三层回退
      1. 返回`mergeTwoLists([2],[3]) = [2 -> 3]`
      2. 所以上一层的`1(list2)`指向`[2 -> 3]`
  
      当前状态
      ```css
       1(list1) ───▶ ?（等待 mergeTwoLists([2],[1 -> 3]) 的结果）

       1(list2) ───▶ 2 ───▶ 3
       ``` 
   3. 第二层回退
      1. 返回`mergeTwoLists([2],[1 -> 3]) = [1(list2) -> 2 -> 3]`
      2. 所以上一层的`1(list1)`指向`[1(list2) -> 2 -> 3]`
  
      当前状态
      ```css
       1(list1) ───▶ 1(list2) ───▶ 2 ───▶ 3
       ``` 
   4. 第一层回退
      1. 返回最终结果`mergeTwoLists([1 -> 2],[1 -> 3]) = [1(list1) ->1(list2) -> 2 -> 3]`

#### 复杂度分析
* **Time complexity:** $\mathcal{O}(n)$. 两个链表里的每个节点都被访问。
* **Space complexity:** $\mathcal{O}(n)$. 递归栈的深度。

## Backlinks
- [Leetcode 笔记目录](Leetcode笔记目录.md)
- [Linked List](Linked_List.md)
- [Recursion](Recursion.md)