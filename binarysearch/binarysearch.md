# 二分查找专题笔记(2021.5.31-2021.6.4)

这周的专题主要是二分查找，难度个人觉得相比于上一个DFS专题有所下降。可能是因为二分查找本身的实现思想比较简单吧，接下来下面是这周的笔记：

# Leetcode题目编号

- \#34 Find First and Last Position of Element in Sorted Array
- \#718 Maximum Length of Repeated Subarray
- \#74 Search a 2D Matrix
- \#300 Longest Increasing Subsequence
- \#658 Find K Closest Elements
- \#278 First Bad Version
- \#209 Minimum Size Subarray Sum
- \#240 Search a 2D Matrix II
- \#704 Binary Search
- \#222 Count Complete Tree Nodes

# 数据结构

## 基础数据结构：数组

二分查找对应的数据结构为队列。队列的要求有且仅有一个：**必须是已经排序过的队列（升序降序均可）。**

## 拓展：矩阵

对应的拓展数据结构为矩阵，我们可以通过将矩阵转换为类似队列的数据结构来进行二分查找。如\#74 Search a 2D Matrix的矩阵，我们可以讲矩阵从左上至右下构造一个单调递增的数组，并对其进行二分查找。

![img](binarysearch.assets/mat.jpg)

对于\#240 Search a 2D Matrix II中间矩阵的行和列都分别递增的情况，我们对它的每一行和每一列分别进行二分查找即可。

![img](binarysearch.assets/searchgrid2.jpg)

## 拓展：完全二叉树

一棵深度为k的有n个结点的二叉树，对树中的结点按从上至下、从左到右的顺序进行编号，如果编号为i（1≤i≤n）的结点与满二叉树中编号为i的结点在二叉树中的位置相同，则这棵二叉树称为完全二叉树。

https://baike.baidu.com/item/%E5%AE%8C%E5%85%A8%E4%BA%8C%E5%8F%89%E6%A0%91

![img](binarysearch.assets/complete.jpg)

图中是一棵不满的完全二叉树，其最底层的节点取值范围落在$[2^h,2^{h+1}-1]$中，其中h是树的高度，根节点的高度为0。

需要特别指出的是，在完全二叉树中，节点编号的二进制还标明了从根节点至该节点的路径。除第一位外，余下各位0代表左节点，1代表右节点，如上图所示二叉树：

- 5的二进制为1 0 1，则5号节点的访问路径为：根节点（1）-左孩子（2）-右孩子（5）
- 6的二进制为1 1 0，则6号节点的访问路径为：根节点（1）-右孩子（3）-左孩子（6）

我们可以利用这个性质来根据节点编号直接访问节点，具体实现将在#222中说明。

## 基础算法

当数据量很大适宜采用该方法。采用二分法查找时，数据需是排好序的。 基本思想：假设数据是按升序排序的，对于给定值key，

从序列的中间位置k开始比较：

- 如果当前位置arr[k]值等于key，则查找成功；

- 若key小于当前位置值arr[k]，则在数列的前半段中查找,arr[low,mid-1]；

- 若key大于当前位置值arr[k]，则在数列的后半段中继续查找arr[mid+1,high]，

直到找到为止,时间复杂度:O(log(n))。

```python
class Solution:
    def search(self, nums, target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        while hi >= lo:  # 慎重选择截截止条件，一般要循环到数组为空
            mid = (lo + hi) // 2
            if nums[mid] == target:  # 找到匹配
                return mid
            elif nums[mid] < target:  # 二分点数值小于target，二分点右移
                lo = mid + 1
            elif nums[mid] > target:  # 二分点数值大于target，二分点左移
                hi = mid - 1
        return -1
```

*摘自#704 Binary Search代码

LeetCode总结，二分法一般性总结: https://blog.csdn.net/EbowTang/article/details/50770315

# 题解

这周的刷题顺序并没有完全的按照从简单到困难的顺序，同时相同类型的题目有的分布在了两天，因此本文对于题解中题目顺序做了一定调整。

## #704 Binary Search

具体请见基础算法部分。

```python
class Solution:
    def search(self, nums, target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        while hi >= lo:  # 慎重选择截截止条件，一般要循环到数组为空
            mid = (lo + hi) // 2
            if nums[mid] == target:  # 找到匹配
                return mid
            elif nums[mid] < target:  # 二分点数值小于target，二分点右移
                lo = mid + 1
            elif nums[mid] > target:  # 二分点数值大于target，二分点左移
                hi = mid - 1
        return -1
```



## #34 Find First and Last Position of Element in Sorted Array

### 思路

本题主要给出了一个升序数组，需要在此升序数组中找到target。看到升序数组查找，就应该想到用二分法了。

需要注意的是，target在数组中可以重复出现，这说明我们不但要找到target同时还要向前向后寻找其上下界的index。

### 题解

```python
class Solution:
    def searchRange(self, nums, target: int):
        def search(mid, target):
            """
            考虑到nums中存在重复出现的数字，所以当nums[mid]找到target之后要向前向后搜索范围
            :param mid: 中间index
            :param target: 搜索目标
            :return: [目标lower索引，目标upper索引]
            """
            ret_mid = mid  # 临时变量用于后续自增自减
            while ret_mid > 0 and nums[ret_mid - 1] == target:
                """
                先向序列小的位置搜索
                需要注意当index为-1时已经越界但是并不会报错，所以要同时判断ret_mid > 0
                注意ret_mid等于0时不可取，这是因为下面ret_mid -= 1时将越界
                """
                ret_mid -= 1  # 向前移位
            ret_low = ret_mid  # 找到low索引
            ret_mid = mid  # 准备寻找upper索引
            while ret_mid + 1 < len(nums) and nums[ret_mid + 1] == target:
                """
                同样要注意nums数组的下标有无越界，所以要判断ret_mid < len(nums) - 1
                """
                ret_mid += 1
            ret_upper = ret_mid

            return ret_low, ret_upper

        low = 0
        upper = len(nums) - 1
        mid = math.ceil((upper + low) * 0.5)
        if not nums:  # 判断空数组情况
            return [-1, -1]
        if target == nums[mid]:  # 判断刚开始已经找到匹配
            return search(mid, target)
        while low <= upper:
            if target == nums[mid]:  # 判断mid下标是否已经找到target
                return search(mid, target)  # 搜索target的lower和upper下标
            elif target < nums[mid]:  # 如果target比二分中间值小
                upper = mid - 1  # upper下移到中间值-1
                mid = math.ceil((upper + low) * 0.5)  # 重新计算中间值下标
            elif target > nums[mid]:
                low = mid + 1
                mid = math.ceil((upper + low) * 0.5)
        return [-1, -1]  # 搜索失败
```

## [#74. Search a 2D Matrix](https://leetcode-cn.com/problems/search-a-2d-matrix/)

### 思路

![img](binarysearch.assets/mat-20210606000057283.jpg)

上图所示为#74的一个输入事例，从中我们可以发现矩阵中的元素从左上到右下都是递增的，因此我们只需要将矩阵reshape成一个数组就可以使用#704的解题方式进行二分搜索了。

### 题解

https://leetcode-cn.com/problems/search-a-2d-matrix/solution/sou-suo-er-wei-ju-zhen-by-leetcode-solut-vxui/

```python
class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        def binarysearch(data, target):
            """
            二分法查找
            :param data:
            :param target:
            :return:
            """
            lower = 0
            upper = len(data) - 1
            mid = math.floor((lower + upper) * 0.5)
            found = False
            while lower <= upper:
                """
                进行二分查找
                注意用小于等于，当三个指针同时指向一个元素
                则找到了元素
                """
                if target < data[mid]:
                    upper = mid - 1
                    mid = math.floor((lower + upper) * 0.5)
                elif target > data[mid]:
                    lower = mid + 1
                    mid = math.floor((lower + upper) * 0.5)
                elif target == data[mid]:  # 有可能在移位之后存在相等的情况
                    return True, mid  # 在相等的情况下返回
            return found, mid  # 当移位之后仍然找不到匹配时返回

        first_row = []
        for i in range(len(matrix)):
            first_row.append(matrix[i][0])  # 添加第一行数据
        found, mid = binarysearch(first_row, target)  # 对每一行的第一列数据进行比较
        if found:
            return found
        else:
            found, _ = binarysearch(matrix[mid], target)  # 对该行剩下的数据进行比较
            return found
```

## [#240. Search a 2D Matrix II](https://leetcode-cn.com/problems/search-a-2d-matrix-ii/)

### 思路

![img](binarysearch.assets/searchgrid2-20210606000943835.jpg)

上图所示为本题的一个输入事例，从图中可知：

- 每一行元素从左到右递增
- 每一列元素从左到右递增

因此，我们可以分别对每一行每一列进行二分搜索，即可得出答案，一共需要搜索m + n次。一个改进的方法是只对行数或列数少的的一者进行搜索也可以遍历所有的元素，一共需要搜索min(m, n)次。其中，m为行数，n为列数。

在此也提及另外一种更容易理解的指针思路：观察矩阵左下或右上角，发现这两个元素刚好位于中间值，因此我们设置一个指针指向它，并与target进行比对，逐次移动指针，如果存在与target相等的数，则返回True，如果指针越界，则与target相等的元素不存在，返回False。

### 题解

https://leetcode-cn.com/problems/search-a-2d-matrix-ii/solution/sou-suo-er-wei-ju-zhen-ii-by-leetcode-2/

```python
class Solution:
    def searchMatrix(self, matrix, target: int):
        """
        二分查找法v2
        通过对每一行与每一列分别进行二分查找获得结果
        相比v1又花了代码
        :param matrix:
        :param target:
        :return:
        """

        def binarysearch(data, target):
            """
            正常的二分查找
            :param data: 数据
            :param target: 目标
            :return: 是否找到
            """
            lo = 0
            hi = len(data) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if data[mid] == target:
                    return True
                if data[mid] < target:
                    lo = mid + 1
                elif data[mid] > target:
                    hi = mid - 1

            return False

        if not matrix:  # 如果Matrix不存在
            return False
        found = False
        for i in range(min(len(matrix), len(matrix[0]))):  # 事实上只需要搜索较短的一条边即可遍历所有的数据
            found_hor = binarysearch(matrix[i], target)  # 搜索行（固定行下标）
            found_vec = binarysearch([matrix[x][i] for x in range(len(matrix))], target)  # 搜索列，固定列下标
            if found_hor or found_vec:
                found = True

        return found
```

在二分法中，值得注意的是官方题解中的二分法函数写法较为复杂，笔者认为可以在主函数中直接构建需要查找的数组更加合适，可以减少代码的复杂度。

```python
# 指针法
class Solution:
    def searchMatrix(self, matrix, target: int):
        """
        搜索矩阵
        仔细观察矩阵可以发现：
        右边的元素永远比左边的大
        下面的元素永远比上面的大
        因此可以从对角线入手，逐次移动指针
        Reference Solution: https://leetcode-cn.com/problems/search-a-2d-matrix-ii/solution/sou-suo-er-wei-ju-zhen-ii-by-leetcode-2/
        :param matrix:
        :param target:
        :return:
        """
        row = len(matrix) - 1  # 初始指针放在左下角
        col = 0
        while row >= 0 and col < len(matrix[0]):
            if matrix[row][col] == target:  # 找到target
                return True
            elif matrix[row][col] < target:  # 目前数字比target小，向右移动
                col += 1
            else:  # 目前数字比target大，向上移动
                row -= 1
        return False  # Default Case
```

有趣的是，虽然二分法看起来很快，但是实际运行时间与指针法相差无几。

## [#278. First Bad Version](https://leetcode-cn.com/problems/first-bad-version/)

### 思路

本题中给定一个递增的版本数组，要求查找其中出现的第一个坏版本。主要解题思路为使用二分查找法查找bad version的边界。对于每一个中间点mid，我们检查：是否符合版本mid是坏版本，且版本mid-1是好版本。以此便可以判断第一个坏版本

### 题解

```python
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        简单的二分法
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
        mid = (left + right) // 2
        while left < right:
            if not isBadVersion(mid - 1) and isBadVersion(mid):  # 判断出现第一个坏版本的依据是：前一个版本OK，但当前版本是坏版本
                return mid
            if isBadVersion(mid):  # 中间值坏
                right = mid - 1
                mid = (left + right) // 2
            else:
                left = mid + 1
                mid = (left + right) // 2
        return mid
```



## [#222. Count Complete Tree Nodes](https://leetcode-cn.com/problems/count-complete-tree-nodes/)

### 思路

这一题直接用DFS或者BFS就可以秒杀，但是这种方式并没有使用到题目中所给出的完全二叉树的条件，因此应该只算对了一半吧。

另一种方法则是对最下层的节点使用二分查找。

1. 我们需要确定该完全二叉树的高度，由完全二叉树的性质，我们可以通过循环遍历节点左孩子的方式来获取高度。在获取高度h后，我们便可以计算最下层节点的编号取值范围为$[2^h,2^{h+1}-1]$，并准备对这些节点进行二分查找。
2. 由节点编号的二进制我们可以知道从根节点访问该节点的路径，通过访问路径判断节点是否存在。
3. 使用二分查找的方式就可以找到节点边界，最后一节点的编号即为节点数量。

### 题解

https://leetcode-cn.com/problems/count-complete-tree-nodes/solution/wan-quan-er-cha-shu-de-jie-dian-ge-shu-by-leetco-2/

```python
class Solution:
    def countNodes(self, root) -> int:
        def calcTreeheight(root):
            """
            计算树高
            :param root:
            :return:
            """
            if not root:
                return 0
            count = 0
            while root.left:
                root = root.left
                count += 1
            return count

        def isNodeexist(node, node_id):
            """
            确定节点是否存在
            :param node:
            :param node_id:
            :return:
            """

            bin_code = [ch for ch in bin(node_id).split("b")[1]]

            for index in range(1, len(bin_code)):
                if not node:
                    return False
                if bin_code[index] == "0":
                    node = node.left
                elif bin_code[index] == "1":
                    node = node.right

            return True if node else False

        if not root:
            return 0
        height = calcTreeheight(root)
        lo = int(pow(2, height))
        hi = int(pow(2, height + 1)) - 1
        mid = (lo + hi) // 2  # 对mid赋初值防止undefined min
        while lo <= hi:
            mid = (lo + hi) // 2  # 更新mid中间值
            if isNodeexist(root, mid - 1) and not isNodeexist(root, mid):  # 如果树不是完全二叉树，则通过判断边界来确定节点数量
                return mid - 1
            if isNodeexist(root, mid):  # 如果监测到节点存在，则边界在mid右边
                lo = mid + 1
            elif not isNodeexist(root, mid):  # 如果检测到节点不存在，则边界在节点左边
                hi = mid - 1
        return mid  # 当满二叉树时，mid到最右边节点，直接return mid
```



## [#718. Maximum Length of Repeated Subarray](https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/)

### 思路

这一题虽然是放在二分专题里面但是我个人是用DP写的。

首先我们很容易就想到暴力解法：

通过两个for循环分别对应两个数组的指针，移动指针并尝试找到第一个相等的元素。当找到了第一个相等的元素之后，以该元素为sub-array头，同时向后寻找相同的元素（使用while循环）。在暴力解法中，我们嵌套了3层循环，因此时间复杂度为$O(n^3)$

因此我们引入了```dp[i][j]```来记录下标索引```[i][j]```之间的最长子**连续**序列长度。当两个子序列的下一位序列相等时，最小重复子序列长度是前一位的最小重复子序列长度+1，即```dp[i+1][j+1]=dp[i][j]+1```；而如果下一位不相等，这说明该连续子序列中断，所以```dp[i+1][j+1]=0```。

由于笔者还在学DP相关内容，在这里可能解释的不是很清楚，先挖个坑，有空一定填。

### 题解

https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/solution/zui-chang-zhong-fu-zi-shu-zu-by-leetcode-solution/

```python
class Solution:
    def findLength(self, nums1, nums2):
        """
        memorize function
        :param nums1:
        :param nums2:
        :return:
        """
        n, m = len(nums1), len(nums2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]  # 构建memo
        ans = 0
        for i in reversed(range(n)):
            for j in reversed(range(m)):
                # dp[i][j] = dp[i + 1][j + 1] + 1 if nums1[i] == nums2[j] else 0
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                    """
                    dp[i][j]存储了从当前index开始连续的最长子序列的长度
                    当nums[i + 1][j + 1]相等，且nums[i][j]相等时
                    最长子序列长度dp[i][j] = dp[i + 1][j + 1] + 1 
                    """
                else:
                    """
                    当nums[i + 1][j + 1]不相等，连续的最长子序列断开，所以长度为0
                    """
                    dp[i][j] = 0
                ans = max(ans, dp[i][j])
        return ans
```

## [#300. Longest Increasing Subsequence](https://leetcode-cn.com/problems/longest-increasing-subsequence/)

### 题解

（施工中）

### 思路

```python
class Solution:
    def lengthOfLIS(self, nums: list) -> int:
        if not nums:  # 如果数组不存在
            return 0
        dp = [1 for _ in range(len(nums))]  # dp初始化，在初始状态下没有最长子链所以dp=1
        for i in range(len(nums)):  # 遍历所有元素
            for j in range(i):
                """
                对nums[j]来说，nums[i]能链接在nums[j]后面的条件为
                nums[i] < nums[j]
                因此比较nums[j]的大小，如果nums[j] < nums[i]
                这dp[i] = dp[j] + 1
                """
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    """
                    1.  如果nums[1]和nums[0]能组成增长子串
                        并且nums[5]和nums[1]能组成增长子串，
                        那么明显有nums[0]-nums[1]-nums[5]这条增长子串
                    2.  例如在nums[5]中需要于nums[0]-nums[4]进行对比
                        nums[5] > nums[0]，因此dp[5] = dp[0] + 1 = 2
                        nums[5] > nums[1]，因此dp[5] = dp[1] + 1 = 3
                        nums[5] < nums[2]，跳过
                        nums[5] < nums[3]，跳过
                        nums[5] < nums[4]，跳过
                    3.  在逐步遍历中找到dp的最大子串
                        上面要用max的原因是因为nums[i - 1]所可以组成的子串不一定是长度最长的
                        因此我们使用max函数来确保nums[i]接到了最长的子串三
                    """
        return max(dp)
```

## [#658. Find K Closest Elements](https://leetcode-cn.com/problems/find-k-closest-elements/)

### 思路

本题解题思路同样首先使用二分查找定位目标元素的下标，我们需要寻找的目标为等于或刚好大于target的元素。

令目标元素的target为i，则结果数组的取值范围为$[i-k,i+k]$。

新建两个指针指向结果数组的左右两端，循环比较两个指针所指向的元素与target的差值并删除差值较大的元素，直到数组长度等于目标长度k时结束。

### 题解

```python
class Solution:
    def findClosestElements(self, arr: list, k: int, x: int) -> list:
        """
        思路：

        :param arr: 数组
        :param k: 区间长度
        :param x: 目标
        :return: 最靠近目标的k个数
        """
        lo = 0
        hi = len(arr) - 1
        mid = 0  # 先定义防止翻车
        while lo <= hi:  # 二分法查找稍比x大的元素
            mid = (lo + hi) // 2
            if arr[mid] == x:
                break
            if arr[mid - 1] < x <= arr[mid]:  # 需要注意的是，使用大于等于号。因为当x等于二分点元素的时候也能符合我们的条件
                break
            elif arr[mid] < x:
                lo = mid + 1
            elif arr[mid] > x:
                hi = mid - 1
        lo = mid - k if mid - k > 0 else 0  # 在确定了x的位置idx后，答案数组位于[idx-k, idx+k]的区间。这里要注意下标不要越界
        hi = mid + k if mid + k > len(arr) else len(arr)
        arr = arr[lo:hi + 1]  # 将区间外的元素删掉
        while len(arr) > k:  # 通过逐次移动左边以及右边的指针来逐渐逼近答案
            if abs(arr[0] - x) < abs(arr[-1] - x) or \
                    (abs(arr[0] - x) == abs(arr[-1] - x) and arr[0] < arr[-1]):  # 根据题目给出的判定条件判断
                del arr[-1]  # 左边小，删除右边
            else:
                del arr[0]
        return arr
```

## [#209. Minimum Size Subarray Sum](https://leetcode-cn.com/problems/minimum-size-subarray-sum/)

### 思路

本题可以使用滑动窗口（队列）方式来进行解题。当子序列和小于target时头指针入队；当子序列和大于target时保存当年序列长度，尾指针出队。当队列头指针超出队列下标，则数组已经遍历完成，程序结束。时间复杂度为O(n)

本题另一种题解前缀和 + 二分查找的方式，施工中。

### 题解

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: list) -> int:
        """
        双指针解法
        Reference Solution:
        https://leetcode-cn.com/problems/minimum-size-subarray-sum/solution/javade-jie-fa-ji-bai-liao-9985de-yong-hu-by-sdwwld/
        https://leetcode-cn.com/problems/minimum-size-subarray-sum/solution/monkti-jie-yong-zui-shao-de-yu-yan-he-da-txe4/
        :rtype: object
        :param target:
        :param nums:
        :return:
        """
        lo = 0  # 左指针开始为0
        cur_sum = 0  # 和初始值为0
        res = len(nums) + 1  # res初始值为数组长度+1，子数组长度最多也不会超过数组长度
        for hi in range(len(nums)):  # 队列头指针
            cur_sum += nums[hi]  # 计算当前子序列的长度
            while cur_sum >= target:  # 如果当前子序列的和超过了target
                res = min(res, hi - lo + 1)  # 更新最小子序列长度，+1是由于数组index从0开始
                cur_sum -= nums[lo]  # 队尾元素出栈，更新当前子序列的和
                lo += 1  # 队尾右移
        return res if res != len(nums) + 1 else 0
```

