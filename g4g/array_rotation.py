#https://www.geeksforgeeks.org/array-rotation/
"""
Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements. 
sample : [1,2,3,4,5,6,7]
input : 2
output: [3,4,5,6,7,1,2]
"""
class MyRotate(object):

    def rotate(self,arr, d ,n):
        temp = arr[:d]
        for x in range(d):
            for i in range(n-1):
                arr[i]=arr[i+1]
        arr[-d:]=temp
        return (arr)
    def run(self):
        arr=[1,2,3,4,5,6]
        d=2
        n=len(arr)
        print(self.rotate(arr,d,n))

class JugglingRotate(object):
    #todo
    def gcd(self, a,b):
        if b==0:
            return a
        else:
            return self.gcd(b, a%b)
        
    def rotate(self,arr, d ,n):
        h = self.gcd(n,d)
        #print(h)
        for i in range(d):
            temp=arr[i]
            arr[i]=arr[i+h]
            arr[i+h]=temp
        return arr

    def run(self):
        arr=[1,2,3,4,5,6]
        d=2
        n=len(arr)
        print(self.rotate(arr,d,n))

MyRotate().run()
JugglingRotate().run()