class Solution(object):
    
    def factorial(self, z):
        if z==1 or z==0:
            return 1
        else:
            return z* self.factorial(z-1)
    def binomial_coefficient(self,n,k):
        a= (self.factorial(n)) / (self.factorial(k) * self.factorial(n-k))
        return a
    def binomial(self,n,k):
        return 1 if k==0 else (0 if n==0 else self.binomial(n-1, k) + self.binomial(n-1, k-1))
    
    def _getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        a=[]
        b=[]
        #rowIndex+=1
        for i in range(rowIndex):
            for j in range(rowIndex-i):
                binomial_value = self.binomial(rowIndex-i-1,j)    
                a.append(binomial_value)
            b.append(a)
            a=[]
        return b# b[-rowIndex]
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        a=[]
        b=[]
        #rowIndex+=1
        for i in range(rowIndex+1):
            #for j in range(rowIndex-i):
            binomial_value = self.binomial_coefficient(rowIndex,i)
            a.append(binomial_value)
            #b.append(a)
            #a=[]
        return a# b[-rowIndex]

print(Solution()._getRow(3))