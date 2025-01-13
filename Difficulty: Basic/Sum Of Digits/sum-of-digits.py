#User function Template for python3

class Solution:
    def sumOfDigits (self, n):
        # code here
        # if 1 <= n <= 10^5:
        total_sum = 0
        for i in str(n):
            total_sum += int(i)
        return total_sum

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.sumOfDigits(N))
        print("~")

# } Driver Code Ends