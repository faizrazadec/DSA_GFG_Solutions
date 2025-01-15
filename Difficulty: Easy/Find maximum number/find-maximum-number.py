#User function Template for python3

class Solution:
    def findMax(self, N):
        # code here
        digits = list(N)

        # Sort the list of characters in descending order
        digits.sort(reverse=True)
    
        # Join the sorted list back into a string
        max_number = ''.join(digits)
    
        return max_number


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=input()
        
        ob = Solution()
        print(ob.findMax(N))
        print("~")
# } Driver Code Ends