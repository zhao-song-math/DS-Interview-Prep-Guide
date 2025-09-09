# 242. Valid Anagram

[Leetcode ↗](https://leetcode.com/problems/valid-anagram/description/?envType=problem-list-v2&envId=xi4ci4ig) | [Neetcode ↗](https://neetcode.io/problems/is-anagram?list=blind75)

<font color="#66BB6A">Easy</font> | <span style="background-color:#E8F5E9; color:#2E7D32; padding:3px 8px; border-radius:12px; font-size:12px; font-weight:bold;">Hash Table</span> <span style="background-color:#FFF8E1; color:#EF6C00; padding:3px 8px; border-radius:12px; font-size:12px; font-weight:bold;">String</span> <span style="background-color:#FFEBEE; color:#B71C1C; padding:3px 8px; border-radius:12px; font-size:12px; font-weight:bold;">Sorting</span>


## Description
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

**Example 1:**

    Input: s = "anagram", t = "nagaram"
    Output: true

**Example 2:**

    Input: s = "rat", t = "car"
    Output: false

**Constraints:**
* `1 <= s.length, t.length <= 5 * 10^4`
* `s` and `t` consist of lowercase English letters.

**Follow up:** What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

---

## 题目解析

### 🟡 My Submission: Sorting

```Python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        else:
            return False
```

参考 [Sorting](Sorting.md)。`sorted()`的时间复杂度是$\mathcal{O}(n\log n)$，比较两个新建 已排序的`list`需要将每一个元素逐一对比，所以时间复杂度是$\mathcal{O}(n)$。所以最终时间复杂度是$\mathcal{O}(n\log n)+\mathcal{O}(n\log n)+\mathcal{O}(n)=\mathcal{O}(n\log n)$。

`sorted()`函数新建了新的`list`，所以空间复杂度是$\mathcal{O}(n)$。
* Time complexity: $\mathcal{O}(n\log n)$
* Space complexity: $\mathcal{O}(n)$


### 🟢 Solution 1: Hash Map

```Python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d_s = {} # count characters
        d_t = {}
        for i in range(len(s)):
            d_s[s[i]] = d_s.get(s[i],0) + 1
            d_t[t[i]] = d_t.get(t[i],0) + 1
        
        return d_s == d_t
```

考虑 [Hash Table](Hash_Table.md)。给两个 [String](String.md) 分别创建一个字典来存储每个字母在string里出现的频率，然后直接用`==`来判断两个字典是否包含相同的key-value pairs。
* Time complexity: $\mathcal{O}(n)$
* Space complexity: $\mathcal{O}(1)$ 因为字典的长度取决于string里有多少不同的字母，最多有26个字母。

## Backlinks
- [Leetcode问题目录](Leetcode问题目录.md)
- [Hash Table](Hash_Table.md)
- [Sorting](Sorting.md)
- [String](String.md)