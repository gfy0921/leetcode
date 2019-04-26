#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#
# https://leetcode-cn.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (35.24%)
# Total Accepted:    12K
# Total Submissions: 34K
# Testcase Example:  '[1,2,0]'
#
# 给定一个未排序的整数数组，找出其中没有出现的最小的正整数。
# 
# 示例 1:
# 
# 输入: [1,2,0]
# 输出: 3
# 
# 
# 示例 2:
# 
# 输入: [3,4,-1,1]
# 输出: 2
# 
# 
# 示例 3:
# 
# 输入: [7,8,9,11,12]
# 输出: 1
# 
# 
# 说明:
# 
# 你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。
# 
#
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 1
        
        for i in range(len(nums)):
            while nums[i] > 0 and nums[i] < len(nums) and nums[nums[i] -1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        for i in range(len(nums)):
            if  nums[i] != i+1:
                return i+1
        return len(nums) + 1


