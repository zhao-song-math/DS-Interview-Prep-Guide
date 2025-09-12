# Binary Search

二分搜索运用于在**有序**数组中查找一个特定元素`x`。

#### 算法步骤 
1. 从数组的中间元素开始，如果中间元素正好是`x`，查找成功；
2. 否则，用中间元素将数组分为前、后两个数组：
   1. 如果 `x < 中间元素`，查找前一个子数组；
   2. 如果 `x > 中间元素`，查找后一个子数组；
3. 重复以上步骤，直到找到 `x`，或直到子数组不存在，代表查找不成功。

![Binary Search](pics/BinarySearch.png)[^1]

#### 复杂度分析
* Time complexity: $\mathcal{O}(n)$
最糟糕的情况是，我们需要将数组迭代切分到只有一个元素：
  * 第一次切分后数组里元素个数：$n/2$
  * 第二次切分后数组里元素个数：$n/4$
  * 第k次，也就是最后一次切分之后数组里的元素个数：$n/(2^k) = 1$
所以迭代 $k = \log_2 n$ 次才能找到元素`x`。
* Space complexity: $\mathcal{O}(1)$



[^1]: https://www.geeksforgeeks.org/dsa/complexity-analysis-of-binary-search/

## Backlinks
- [Leetcode 笔记目录](Leetcode笔记目录.md)
- [33. Search in Rotated Sorted Array](33-Search_in_Rotated_Sorted_Array.md)