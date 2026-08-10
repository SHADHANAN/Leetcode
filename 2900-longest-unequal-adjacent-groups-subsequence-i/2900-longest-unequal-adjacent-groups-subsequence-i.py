class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        dp=[words[0]]
        for i in range(1,len(words)):
            if(groups[i]!=groups[i-1]):
                dp.append(words[i])
        return dp