class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        c=0
        for i in nums:
            c^=i
        a=c^k
        x=0
        for i in range(32):
            if a&(1<<i)>0:
                x+=1
        return x
                
        