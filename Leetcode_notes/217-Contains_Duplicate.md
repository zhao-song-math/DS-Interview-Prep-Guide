# 217. Contains Duplicate 

[Leetcode ↗](https://leetcode.com/problems/contains-duplicate/description/?envType=problem-list-v2&envId=xi4ci4ig) | [Neetcode ↗](https://neetcode.io/solutions/contains-duplicate)

<font color="#66BB6A">Easy</font> | <span style="background-color:#E3F2FD; color:#1565C0; padding:3px 8px; border-radius:12px; font-size:12px; font-weight:bold;">Array</span> <span style="background-color:#E8F5E9; color:#2E7D32; padding:3px 8px; border-radius:12px; font-size:12px; font-weight:bold;">Hash Table</span> <span style="background-color:#FFEBEE; color:#B71C1C; padding:3px 8px; border-radius:12px; font-size:12px; font-weight:bold;">Sorting</span>

## Description
Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

**Example 1:**

    Input: nums = [1,2,3,1]
    Output: true
    Explanation: The element 1 occurs at the indices 0 and 3.

**Example 2:**

    Input: nums = [1,2,3,4]
    Output: false
    Explanation: All elements are distinct.

**Example 3:**

    Input: nums = [1,1,1,3,3,4,3,2,4,2]
    Output: true

**Constraints:**
* `1 <= nums.length <= 10^5`
* `-10^9 <= nums[i] <= 10^9`

---

## 题目解析


### 🔴 My Submission

```Python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        list = []
        for i in range(len(nums)):
            if nums[i] in list:
                return True
            else:
                list.append(nums[i])
        return False
```

此解exceeds the time limit, 主要问题出在`if nums[i] in list:`, 时间复杂度太高. 最差的情况是此 array 没重复元素, 最后一次循环时需要遍历前面的 n-1 个元素，一共 n 此循环，所以时间复杂度是$\mathcal{O}(n^2)$。这种情况下list完整复制了array 里面的元素，所以空间复杂度是$\mathcal{O}(n)$.


为了降低时间复杂度，我们可以考虑用 [Hash Table](Hash_Table.md) 这种数据结构来存储已经出现过的元素。以下两种解法用了set来存储。

### 🟢 Solution 1

```Python
class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
      seen = set()
      for num in nums:
          if num in seen:
              return True
          else:
              seen.add(num)
      return False
```

此解与My Submissio思路相同，不同点在于用了不同的数据结构存储数据。在list里查找元素时遵循的线性查找，即按照顺序出头到尾查找；而在set中查找元素是通过hash function直接定位元素，所以时间复杂度是$\mathcal{O}(1)$。最糟糕的情况是`nums`中没有重复元素，循环需要迭代n次，最终时间复杂度是$\mathcal{O}(n)$。又因此时set中存储了所有`nums`的元素，所以空间复杂度是$\mathcal{O}(n)$。


### 🟢 Solution 2
由于set里无重复元素，所以也可以通过对比set和`nums`的长度来判断`nums`中是否有重复元素。

```Python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
```

* Time complexity: $\mathcal{O}(n)$
* Space complexity: $\mathcal{O}(n)$

## Backlinks
- [Leetcode 笔记目录](Leetcode笔记目录.md)
- [Hash Table](Hash_Table.md)