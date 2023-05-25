class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        pre = strs[0]    
        for i in range(1, len(strs)):
            while pre != strs[i][:len(pre)]:
                pre = pre[:-1]
                if i == "":
                    return ""
        return pre
