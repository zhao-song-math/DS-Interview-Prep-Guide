# 125. Valid Palindrome

[Leetcode ↗](https://leetcode.com/problems/valid-palindrome/description/?envType=problem-list-v2&envId=xi4ci4ig) | [Neetcode ↗](https://neetcode.io/problems/is-palindrome?list=blind75)

<font color="#66BB6A">Easy</font> | <span style="background-color:#FFFDE7; color:#F9A825; padding:3px 8px; border-radius:12px; font-size:12px; font-weight:bold;">Two Pointers</span> <span style="background-color:#FFF8E1; color:#EF6C00; padding:3px 8px; border-radius:12px; font-size:12px; font-weight:bold;">String</span>

## Description
A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` *if it is a **palindrome**, or `false` otherwise.*

**Example 1:**

    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

**Example 2:**

    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.

**Example 3:**

    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome.

**Constraints:**
* `1 <= s.length <= 2 * 10^5`
* `s` consists only of printable ASCII characters.

---


## 题目解析


### 🟢 Solution 1: Reverse String

```Python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum(): # check (a-z,A-Z,0-9)
                newStr += c.lower()
        return newStr == newStr[::-1] # reverse string
```

创建新的 [string](String.md) 其中只包含字母和数字，然后再比较新string和它的reversed string 是否相同。
* Time complexity: $\mathcal{O}(n)$
* Space complexity: $\mathcal{O}(n)$


### 🟢 Solution 2： Two Pointers

```Python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while(l<r):
            while(l<r and not self.alphaNum(s[l])):
                l += 1
            while(l<r and not self.alphaNum(s[r])):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            
            l,r = l+1, r-1

        return True

    def alphaNum(self,c): # define fuction input里别忘了加self
        return (ord('a') <= ord(c) <= ord('z') or 
        ord('A') <= ord(c) <= ord('Z') or
        ord('0') <= ord(c) <= ord('9'))
```

此解运用 [Two Pointers](Two_Pointers.md) 算法。用前后两个反向而行的指针来比较string里的元素，直到两个指针错过或者停留在同一位置。每次指针指向一个元素时需要查看此元素是否是数字或字母，如果不是，指针指向下一个元素，如果是，将此元素的字母变成小写。

如果面试中不让用`isalnum()`来check字母和数字，可以如上自定义函数来check。

* Time complexity: $\mathcal{O}(n)$
* Space complexity: $\mathcal{O}(1)$

## Backlinks
- [Leetcode 笔记目录](Leetcode笔记目录.md)
- [String](String.md)
- [Two Pointers](Two_Pointers.md)