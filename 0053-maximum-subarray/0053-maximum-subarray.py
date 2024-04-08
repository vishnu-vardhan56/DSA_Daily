class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
        max_sum = -sys.maxsize-1
        cur_sum = 0
        for i in range(len(arr)):
            cur_sum += arr[i]
            if (arr[i] > cur_sum):
                cur_sum = arr[i]
            if (cur_sum > max_sum):
                max_sum = cur_sum
                
        return (max_sum)
        
