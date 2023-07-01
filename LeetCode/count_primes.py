class Solution:
    def countPrimes(self, n: int) -> int:
        if (n<2):
            return(0)
        isPrime = [True] * n
        isPrime[0] = isPrime[1] = False
        
        for i in range(2,int(math.ceil(pow(n,1/2)))):
            if(isPrime[i]):
                for multiple_of_i in range(i*i,n,i):
                    isPrime[multiple_of_i] = False
                    
                    
        return sum(isPrime)
