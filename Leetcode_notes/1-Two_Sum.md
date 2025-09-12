# 1. Two Sum 

[Leetcode ↗](https://leetcode.com/problems/two-sum/description/?envType=problem-list-v2&envId=xi4ci4ig) | [Neetcode ↗](https://neetcode.io/problems/two-integer-sum?list=blind75) 

<font color="#66BB6A">Easy</font> 

<span style="background-color:#E3F2FD; color:#1565C0; padding:3px 8px; border-radius:12px; font-size:12px; font-weight:bold;">Array</span> <span style="background-color:#E8F5E9; color:#2E7D32; padding:3px 8px; border-radius:12px; font-size:12px; font-weight:bold;">Hash Table</span>

## Description
Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.

You may assume that each input would have  , and you may not use the same element twice.

You can return the answer in any order.

**Example 1:**

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

**Example 2:**

    Input: nums = [3,2,4], target = 6
    Output: [1,2]

**Example 3:**

    Input: nums = [3,3], target = 6
    Output: [0,1]

**Constraints:**
* `2 <= nums.length <= 104`
* `-109 <= nums[i] <= 109`
* `-109 <= target <= 109`
* Only one valid answer exists.

**Follow-up:** Can you come up with an algorithm that is less than O(n2) time complexity?

---

## 题目解析


### 🟡 My Submission

```Python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                d[nums[i]+nums[j]] = [i,j]
        return d[target]
```

对长度为`n`的数组求两数之和一共有${n \choose 2}$种组合，所以循环一共迭代${n \choose 2}$次，`dict`的尺寸也为${n \choose 2}$。
* **Time complexity:** $\mathcal{O}(n^2)$
* **Space complexity:** $\mathcal{O}(n^2)$

### 🟢 Solution 1: Hash Map (Two Pass)

考虑[Hash Table](Hash_Table.md)。先构造一个`nums`值-`index`的`dict`, 接着通过遍历`nums`选取第一个值`x`，再检查第二个值`y = traget - x`是否在`dict`中。

```Python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        d = {} # value -> index
        for i,num in enumerate(nums):
            d[num] = i 
        for i,x in enumerate(nums): 
            y = target - x
            if y in d and d[y] != i:
                return [d[y], i ]
```

两次循环都迭代`n`次，时间复杂度都是$\mathcal{O}(n)$，所以最终是$\mathcal{O}(2n)$. 空间上构造了一个size是`n`的`dict`。
* **Time complexity:** $\mathcal{O}(n)$
* **Space complexity:** $\mathcal{O}(n)$


### 🟢 Solution 2: Hash Map (One Pass)

此解在Solution 1的基础上考虑边check`y`在不在`dict`里边构造`dict`。

根据次思路先写出一下代码，fail掉当input是两个相同的数得出的和的情况，例如`Input: nums = [3,3], target = 6`。当循环迭代完第一次后`d = {3:0}`,接着进行第二次迭代`i = 1, x = 3`,通过`d[x] = i`, 字典就变成`d = {3:1}`，而第一次循环添加的`{3:0}`就被覆盖掉了，这样导致之后的if语句fail，无法返回正确结果`[0,1]`。

```Python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        d = {}
        for i,x in enumerate(nums):
            d[x] = i
            y = target - x
            if y in d and d[y] != i:
                return [d[y], i]
```

通过改变`d[x] = i`的位置，让代码先check if语句，再给字典添加元素可以让`Input: nums = [3,3], target = 6`返回正确值。

```Python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        d = {}
        for i,x in enumerate(nums):
            y = target - x
            if y in d:
                return [d[y], i]
            d[x] = i
```

* **Time complexity:** $\mathcal{O}(n)$
* **Space complexity:** $\mathcal{O}(n)$

## Backlinks
- [Leetcode 笔记目录](Leetcode笔记目录.md)
- [Hash Table](Hash_Table.md)