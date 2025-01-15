#User function Template for python3

class Solution:
    def count(self,A,B,N): 
        # code here
        def count_divisors(num):
            count = 0
            for i in range(1, int(num**0.5) + 1):
                if num % i == 0:
                    count += 1
                    if i != num // i:
                        count += 1
            return count

        count = 0
        for num in range(A, B + 1):
            if count_divisors(num) == N:
                count += 1
    
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B,N = (input().split())
        A = int(A)
        B = int(B)
        N = int(N)
        ob = Solution()
        print(ob.count(A,B,N))
        print("~")
# } Driver Code Ends