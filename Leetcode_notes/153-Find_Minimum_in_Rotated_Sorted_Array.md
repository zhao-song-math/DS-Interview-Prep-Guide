# 153. Find Minimum in Rotated Sorted Array

[Leetcode ↗](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/) | [Neetcode ↗](https://neetcode.io/solutions/find-minimum-in-rotated-sorted-array)

<font color="#FF8F00">Medium</font> 

<span style="background-color:#E3F2FD; color:#1565C0; padding:3px 8px; border-radius:12px; font-size:12px; font-weight:bold;">Array</span> <span style="background-color:#F3E5F5; color:#4A148C; padding:3px 8px; border-radius:12px; font-size:12px; font-weight:bold;">Binary Search</span>

## Description
Suppose an array of length `n` sorted in ascending order is **rotated** between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:

- `[4,5,6,7,0,1,2]` if it was rotated `4` times.
- `[0,1,2,4,5,6,7]` if it was rotated `7` times.

Notice that **rotating** an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array `nums` of **unique** elements, return *the minimum element of this array*.

You must write an algorithm that runs in `O(log n)` time.

**Example 1:**

    Input: nums = [3,4,5,1,2]
    Output: 1
    Explanation: The original array was [1,2,3,4,5] rotated 3 times.

**Example 2:**

    Input: nums = [4,5,6,7,0,1,2]
    Output: 0
    Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

**Example 3:**

    Input: nums = [11,13,15,17]
    Output: 11
    Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 

**Constraints:**
* `n == nums.length`
* `1 <= n <= 5000`
* `-5000 <= nums[i] <= 5000`
* All the integers of `nums` are **unique**.
* `nums` is sorted and rotated between `1` and `n` times.


---

## 题目解析

### 🟢 My Submission

由于是rotated sorted array，所以元素之间都是从小到大排列，即前一个元素总是小于后一个元素，除了最大值和最小值的排列是逆序。所以问题的关键就是找到逆序排列的两个元素，然后返回两个元素中的第二个元素即为最小值。
```Python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        
        if nums[1] < nums[0]:
            return nums[1]
        else:
            index = len(nums)-1
            while nums[index-1] < nums[index]:
                index -= 1
            return nums[index]
```
第一次提交忘记`if len(nums) < 2:`，忽略了`array`里只有一个元素的情况。

* Time complexity: $\mathcal{O}(n)$. Beats 100% 👏
* Space complexity: $\mathcal{O}(1)$. Beats 80.11%👏

### 🟡 My Submission


### 🟢 Solution (Binary Search)

此解使用[Binary Search](<Binary_Search.md>)算法。步骤如下：
1. Use Binary Search with low = 0, high = n-1, and ans = INT_MAX.
2. Find mid = (low + high) / 2.
3. If nums[low] <= nums[mid]: left part sorted → update ans with nums[low], move low = mid + 1.
4. Else: right part sorted → update ans with nums[mid], move high = mid - 1.
5. Repeat until low > high. Return ans.

代码如下：、
```Python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res
```

* **Time complexity:** $\mathcal{O}(\log n)$
* **Space complexity:** $\mathcal{O}(1)$

此法时间复杂度比My submission低，但感觉步骤更绕，不太理解。