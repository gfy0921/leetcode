#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿的个数
#
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def sink(i, j):
            if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j] == '1':
                grid[i][j] = '0'
                sink(i+1, j)
                sink(i-1, j)
                sink(i, j+1)
                sink(i, j-1)
                return 1
            return 0
        sum = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                sum += sink(i, j)
        return sum



