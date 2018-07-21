
class Solution:
    def __init__(self):
        self.max_data = {}
        """
        给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

        示例:

        输入: [-2,1,-3,4,-1,2,1,-5,4],
        输出: 6
        解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
        进阶:

        如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。


        """

    def merger_helper(self, nums, low, hight):
        if low == hight:
            return nums[low]

        middle = (low + hight) // 2
        left_maxnum = self.merger_helper(nums, low, middle)
        right_maxnum = self.merger_helper(nums, middle + 1, hight)

        # 求字序列横跨两个边界的和，分成左边界限和右边界限的和
        left_border_sum = nums[middle]
        left_sum = nums[middle]
        for i in range(middle - 1, low - 1, -1):
            left_sum = nums[i] + left_sum
            if left_sum > left_border_sum:
                left_border_sum = left_sum

        right_border_sum = nums[middle + 1]
        right_sum = nums[middle + 1]
        for i in range(middle + 2, hight + 1):
            right_sum = right_sum + nums[i]
            if right_sum > right_border_sum:
                right_border_sum = right_sum
        border_sum = left_border_sum + right_border_sum
        print(left_maxnum, right_maxnum, border_sum)
        return max(left_maxnum, right_maxnum, border_sum)

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxsum = self.merger_helper(nums, 0, len(nums) - 1)
        return maxsum
