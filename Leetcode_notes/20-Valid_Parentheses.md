# 20. Valid Parentheses

[Leetcode ↗](https://leetcode.com/problems/valid-parentheses/?envType=problem-list-v2&envId=xi4ci4ig) | [Neetcode ↗](https://neetcode.io/solutions/valid-parentheses)

<font color="#66BB6A">Easy</font> | <span style="background-color:#FFF8E1; color:#EF6C00; padding:3px 8px; border-radius:12px; font-size:12px; font-weight:bold;">String</span> <span style="background-color:#FFEBEE; color:#C62828; padding:3px 8px; border-radius:12px; font-size:12px; font-weight:bold;">Stack</span>

## Description
Given a string `s` containing just the characters `(`, `)`, `{`, `}`, `[` and `]`, determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

**Example 1:**

    Input: s = "()"
    Output: true

**Example 2:**

    Input: s = "()[]{}"
    Output: true

**Example 3:**

    Input: s = "(]"
    Output: false

**Constraints:**
* `1 <= s.length <= 10^4`
* `s` consists of parentheses only `'()[]{}'`.

---


## 题目解析


### 🟢 Solution: Stack
此方法所用 stack 在 Python 中即是 [List](List.md)。
1. 遍历`s`，如果是 open bracket, 将此 open bracket 放入 [Stack](Stack.md);
2. 如果是 close bracket, 查看 stack，如果 stack 不为空，并且最后一个元素是对应的 open bracket，`stack.pop()`; 如果 stack 为空，或者其中最后一个元素没有与之对应的 open bracket，返回`False`; 。
3. 直到遍历完成，最后 stack 为空，返回True；不为空，返回 False。

* 如何检查两个 brackets 是否 match? 创建一个以下的 Hash Map:
  ```
  ')' -> '('
  '}' -> '{'
  ']' -> '['
  ```

**代码如下：**
看过正确答案之后所写。

```Python
class Solution:
    def isValid(self, s: str) -> bool:
        d = {')': '(', '}': '{', ']': '['}
        stack = []

        for a in s:
            if a in d:
                if len(stack) > 0 and d[a] == stack[-1]:
                    stack.pop()
                else:
                    return False

            else: # a is a open bracket.
                stack.append(a)
        
        return len(stack) == 0
```
        
* Time complexity: \(\mathcal{O}(n)\)
  遍历了`s`里的所有元素
* Space complexity: \(\mathcal{O}(n)$\)
  最糟糕的情况 `stack` 存满了 `s` 的所有元素。

## Backlinks
- [Leetcode问题目录](Leetcode问题目录.md)
- [List](List.md)
- [Stack](Stack.md)