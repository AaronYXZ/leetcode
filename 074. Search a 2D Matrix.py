'''

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.

'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        ## Diff between / & // https://www.tutorialspoint.com/python/python_basic_operators.htm
        ## http://www.cnblogs.com/grandyang/p/4323301.html
        ## https://github.com/gavinfish/leetcode-share/blob/master/python/074%20Search%20a%202D%20Matrix.py
        if matrix == []:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        l, h = 0, m * n - 1
        while l <= h:
            mid = l + (h - l) // 2
            if matrix[mid // n][mid % n] == target:
                return True
            elif matrix[mid // n][mid % n] < target:
                l = mid + 1
            else:
                h = mid - 1
        return False              
        
        
