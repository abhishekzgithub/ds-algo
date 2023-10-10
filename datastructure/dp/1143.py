"""
video links: https://www.youtube.com/watch?v=sSno9rV8Rhg&ab_channel=AbdulBari

1143. Longest Common Subsequence
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
"""

class Solution(object):

    def lcs_recur(self,index1,index2,string1,string2,result):
        """
        recursion
        if index1==len(string1) || index2==len(string2)
            return 0
        elif string1[index1]==string2[index2]:
            return 1+lcs(index1+1,index2+1)
        else:
            return max(lcs(index1+1,index2),lcs(index1,index2+1))
        """
        if index1==len(string1) or index2==len(string2):
            return 0
        elif string1[index1]==string2[index2]:
            result.append(string1[index1])
            return 1+self.lcs_recur(index1+1,index2+1,string1,string2,result)
        else:
            return max(self.lcs_recur(index1+1,index2,string1,string2,result)
                        ,self.lcs_recur(index1,index2+1,string1,string2,result))

    def lcs_recur_memo(self,index1,index2,string1,string2,result,memo_matrix):
        """
        memoisation recursion
        we start with end index and keep decreasing till 0
        if found, the add 1 to the cell or max ,based on the recursion
        One needs to understand the recursion first.
        then use tabular memoization

        if index1==0 || index2==0
            return 0
        elif string1[index1-1]==string2[index2-1]:
            return 1+lcs(index1+1,index2+1)
        else:
            return max(lcs(index1+1,index2),lcs(index1,index2+1))
        """
        try:
            if index1==0 or index2==0:#index1==len(string1) or index2==len(string2):
                return 0

            if memo_matrix[index2][index1]!=-1:
                return memo_matrix[index2][index1]
            
            elif string1[index1-1]==string2[index2-1]:
                result.append(string1[index1-1])
                memo_matrix[index2][index1]= 1+self.lcs_recur_memo(index1-1,index2-1,string1,string2,result,memo_matrix)
                #return memo_matrix[index2][index1]
            else:
                memo_matrix[index2][index1]= max(self.lcs_recur_memo(index1-1,index2,string1,string2,result,memo_matrix)
                            ,self.lcs_recur_memo(index1,index2-1,string1,string2,result,memo_matrix))
            return memo_matrix[index2][index1]
        except:
            print("Error")
            print(index1,index2)

    def lcs_recur_tabular(self,index1,index2,string1,string2,result,memo_matrix):
        """
        tabulation recursion
        we start with end index and keep decreasing till 0
        if found, the add 1 to the cell or max ,based on the recursion
        One needs to understand the recursion first.
        then use tabular memoization

        if index1==0 || index2==0
            return 0
        elif string1[index1-1]==string2[index2-1]:
            return 1+lcs(index1+1,index2+1)
        else:
            return max(lcs(index1+1,index2),lcs(index1,index2+1))
        """
        for col in range(len(string1)-1,-1,-1):
            for row in range(len(string2)-1,-1,-1):
                print(memo_matrix[row][col])
                if string1[col]==string2[row]:
                    memo_matrix[row][col]=1+memo_matrix[row+1][col+1]
                else:
                    memo_matrix[row][col]=max(memo_matrix[row+1][col],memo_matrix[row][col+1])
        return memo_matrix[0][0]
    
    def lcs_recur_tabular(self,index1,index2,string1,string2,result,memo_matrix):
        """
        tabulation recursion
        we start with end index and keep decreasing till 0
        if found, the add 1 to the cell or max ,based on the recursion
        One needs to understand the recursion first.
        then use tabular memoization

        if index1==0 || index2==0
            return 0
        elif string1[index1-1]==string2[index2-1]:
            return 1+lcs(index1+1,index2+1)
        else:
            return max(lcs(index1+1,index2),lcs(index1,index2+1))
        """
        for row in range(1,len(memo_matrix)):
            for col in range(1,len(memo_matrix[0])):
                if string1[col-1]==string2[row-1]:
                    memo_matrix[row][col]=1+memo_matrix[row-1][col-1]
                else:
                    memo_matrix[row][col]=max(memo_matrix[row-1][col],memo_matrix[row][col-1])
        return memo_matrix[index2][index1]

        
    
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        string1=list(text1)
        string2=list(text2)
        result=[]
        #longest_cs= self.lcs_recur(index1=0,index2=0,string1=string1,string2=string2,result=result)
        #print(result[:longest_cs],longest_cs)

        memo_matrix=[[-1 for _ in range(len(text1)+1) ] for _ in range(len(text2)+1)]
        #print(memo_matrix)
        string1=text1
        string2=text2
        result=[]
        #longest_cs = self.lcs_recur_memo(index1=len(text1),index2=len(text2),string1=string1,string2=string2,result=result,memo_matrix=memo_matrix)
        #print(longest_cs,memo_matrix,"\n------",result[::-1])
        string1=text1
        string2=text2
        result=[]
        memo_matrix=[[0 for _ in range(len(text1)+1) ] for _ in range(len(text2)+1)]
        longest_cs = self.lcs_recur_tabular(index1=len(text1),index2=len(text2),string1=string1,string2=string2,result=result,memo_matrix=memo_matrix)
        print(longest_cs,memo_matrix,"\n------",result[::-1])
        return

#text2 = "ace";text1 = "abcde"; #3
#text1 = "abc"; text2 = "def" #0
# text1 = "abc"; text2 = "abc" #3
text1 ="pmjghexybyrgzczy"; text2 ="hafcdqbgncrcbihkd"
print(Solution().longestCommonSubsequence(text1,text2))