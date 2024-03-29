#https://leetcode.com/problems/squares-of-a-sorted-array/

def sortedSquares(self, nums):
    """
    not using .sort() because then time complexity O(n-log-n)
    and also not using append but creating a new array
    space com = O(n)
    time com = O(n) auxillary (locally declared variables) space
    """
    
    ans = [0] * len(nums)
    trav_p = len(nums) - 1
    lr = 0
    rr = len(nums) - 1
    ls = nums[lr] ** 2 #last element from left
    rs = nums[rr] ** 2 #last element from right
    while trav_p >= 0:
        if ls > rs: #sorting
            ans[trav_p] = ls
            lr += 1
            ls = nums[lr] ** 2 #putting largest element at the end
        else:
            ans[trav_p] = rs
            rr -= 1
            rs = nums[rr] ** 2
        trav_p -= 1
    return ans
