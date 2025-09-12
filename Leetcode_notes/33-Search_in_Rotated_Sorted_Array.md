# 33. Search in Rotated Sorted Array

[Leetcode ↗](https://leetcode.com/problems/search-in-rotated-sorted-array/description/) | [Neetcode ↗](https://neetcode.io/solutions/search-in-rotated-sorted-array)

<font color="#FF8F00">Medium</font> 

<span style="background-color:#E3F2FD; color:#1565C0; padding:3px 8px; border-radius:12px; font-size:12px; font-weight:bold;">Array</span> <span style="background-color:#F3E5F5; color:#4A148C; padding:3px 8px; border-radius:12px; font-size:12px; font-weight:bold;">Binary Search</span>

## Description
There is an integer array `nums` sorted in ascending order (with **distinct** values).

Prior to being passed to your function, `nums` is **possibly rotated** at an unknown pivot index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (0-indexed). For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index `3` and become `[4,5,6,7,0,1,2]`.

Given the array `nums` **after** the possible rotation and an integer `target`, return *the index of* `target` *if it is in* `nums`*, or* `-1` *if it is not in* `nums`.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**

    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4

**Example 2:**

    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1

**Example 3:**

    Input: nums = [1], target = 0
    Output: -1

**Constraints:**
* `1 <= nums.length <= 5000`
* `-10^4 <= nums[i] <= 10^4`
* All values of `nums` are **unique**.
* `nums` is an ascending array that is possibly rotated.
* `-10^4 <= target <= 10^4`

---


## 题目解析


### 🔴 My Submission 1 (Binary Search)

此解使用[Binary Search](Binary_Search.md)算法。步骤如下：
1. 寻找逆序位置，将`nums`分为两个有序的数组，比如：`[4,5,6,7,0,1,2]` 找到 `7,0`，将数组分为`[4,5,6,7]`和`[0,1,2]`;
   * 如何寻找？可以通过比较`nums[m]`和`nums[r]`
     * 如果`nums[m] > nums[r]`，逆序在右边子数组；
     * 否则，逆序在左边子数组。
   * 此步需考虑`nums`本身是有序的情况！此中情况跳过`  步骤 2`，直接到`步骤 3`。
2. 判断`target`是在哪个子数组里；
3. 在子数组中用binary search算法寻找`target`。

```Python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1. search cut
        l, r = 0, len(nums)-1
        m = (l+r) // 2

        while l+1 < r: # when l+1 = r, cut found
            if nums[m] > nums[r]: # cut in right sub-array
                l = m
            else:
                r = m # cut in left sub-array

        # 2. cut found, two sub-array got, check target in which sub-array
        if target > nums[l]: # target in right sub-array
            binarySearch(r, len(nums)-1, nums, target)
        else: # target in right sub-array
            binarySearch(0, l, nums, target)

        return -1 # search failed

    # 3. binary search target
    def binarySearch(self, ll, rr, nums, target):
        mm = (ll+rr) // 2

        while ll < rr:
            if  target == nums[mm]:
                return mm
            elif target > nums[mm]: # target in right sub-array
                ll = mm + 1
            else: # target in left sub-array
                rr = mm - 1
```
❌ 运行结果：`Time Limit Exceeded`。原因如下：
1. `m = (l+r) // 2`和`mm = (ll+rr) // 2`都放在了循环外，所以左、中、右指针不更新，导致陷入死循环；
2. `search()`函数没有`return`；
3. 没有考虑如果array没有被rotate的情况；
4. 调用`binarySearch()`没加`self.`，正确调用：`self.binarySearch()`；
5. `binarySearch()`中没有考虑`ll`和`rr`相等的情况。



### 🟢 My Submission 2 (Binary Search - Two Pass)

此解是`My Submission 1`的修订版。
```Python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1. search cut
        l, r = 0, len(nums)-1

        while l+1 < r: # when l+1 = r
            m = (l+r) // 2
            if nums[m] > nums[r]: # cut in right sub-array
                l = m
            else:
                r = m # cut in left sub-array
                
        if nums[l] < nums[r]:
            return self.binarySearch(0, len(nums)-1, nums, target)

        # 2. cut found, two sub-array got, check target in which sub-array
        if target < nums[0]: # target in right sub-array
            return self.binarySearch(r, len(nums)-1, nums, target)
        else: # target in right sub-array
            return self.binarySearch(0, l, nums, target)

    # 3. binary search target
    def binarySearch(self, ll, rr, nums, target):
        while ll <= rr:
            mm = (ll+rr) // 2
            if  target == nums[mm]:
                return mm
            elif target > nums[mm]: # target in right sub-array
                ll = mm + 1
            else: # target in left sub-array
                rr = mm - 1
        
        return -1 # search failed
```
* **Time Complexity:** $\mathcal{O}(\log n)$. Finding the pivot takes $\mathcal{O}(\log n)$ time, and the final binary search also takes $\mathcal{O}(\log n)$ time. The total time is $\mathcal{O}(\log n) + \mathcal{O}(\log n)$, which simplifies to $\mathcal{O}(\log n)$. ⏱️

* **Space Complexity:** $\mathcal{O}(1)$. You are only using a few variables to store pointers (l, r, m, etc.), so the memory usage is constant and does not depend on the input size. 


### 🟢 Solution 1 (Binary Search - One Pass)
My Submission 2 是其中一种解法，分为 拆分原有数组为两个子数组 和 从子数组中寻找 `target` 两步。在此展式另一种解法 -- 直接用 binary search 算法寻找 `target`。并通过比较 `nums[l]` 和 `nums[mid]`的大小来确定左右哪个子数组存在逆序。

代码如下：
```Python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]: # 逆序在右边数组，左边数组有序 [4,5,6,7,0,1,2]
                if target > nums[mid] or target < nums[l]: #  target 在右边 逆序存在的数组
                    l = mid + 1
                else: # target 在左边的有序数组
                    r = mid - 1

            else: # 逆序在左边数组，右边数组有序 [6,7,0,1,2,4,5]
                if target < nums[mid] or target > nums[r]: # target 在左边 逆序存在的数组
                    r = mid - 1
                else: # target 在右边的有序数组
                    l = mid + 1
        return -1
```



* **Time complexity:** $\mathcal{O}(n)$
* **Space complexity:** $\mathcal{O}(n)$

## Backlinks
- [Leetcode 笔记目录](Leetcode笔记目录.md)
- [Binary Search](Binary_Search.md)