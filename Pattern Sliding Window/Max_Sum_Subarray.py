#https://practice.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1#:~:text=Given%20an%20array%20of%20integers,%3D700%2C%20which%20is%20maximum.

class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        # code here 
        max_sum = 0
        l = 0
        r = 0
        sum_value = 0
        for r in range(N):
            sum_value = sum_value + Arr[r]
            if r-l >=K:
                sum_value = sum_value - Arr[l]
                l = l+1
            #print(sum_value)
            if sum_value > max_sum:
                max_sum = sum_value
        return max_sum
      
