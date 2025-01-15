#User function Template for python3


class Solution:
    def sumOfDivisors(self, n):
        # Initialize an array to store the sum of divisors for each number
        divisor_sum = [0] * (n + 1)
    
        # Compute the sum of divisors for all numbers
        for i in range(1, n + 1):
            for j in range(i, n + 1, i):
                divisor_sum[j] += i
    
        # Return the sum of all F(i) from 1 to n
        return sum(divisor_sum)
    	        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sumOfDivisors(N)
        print(ans)
        print("~")

# } Driver Code Ends