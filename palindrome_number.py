class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        rev_x = x[::-1] 

        if x == rev_x:
            return True
        else:
            return False
