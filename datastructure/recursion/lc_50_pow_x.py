class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==1:
            return x
        if n==0:
             return 1
        if n<0:
            return 1.0/self.myPow(x,-1*n)
        elif n>0:
            if n%2==1:# odd
                return x*self.myPow(x*x,(n-1)//2)
            else:# even
                return self.myPow(x*x,n//2)
    def myPow(self, x, n):
        if n == 0:
            return 1

        # Handle case where, n < 0.
        if n < 0:
            n = -1 * n
            x = 1.0 / x

        # Perform Binary Exponentiation.
        result = 1
        while n != 0:
            # If 'n' is odd we multiply result with 'x' and reduce 'n' by '1'.
            if n % 2 == 1:
                result *= x
                n -= 1
            # We square 'x' and reduce 'n' by half, x^n => (x^2)^(n/2).
            x *= x
            n //= 2
        return result

x=2
n=-2
# x=0.44528
# n=0

x=0.00001
n=2147483647
x=3
n=5
print(Solution().myPow(x,n))