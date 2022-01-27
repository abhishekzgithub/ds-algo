"""The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.
Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) 
that occur more than once in a DNA molecule. You may return the answer in any order.

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

"""

class Solution(object):
    @classmethod
    def findRepeatedDnaSequences(cls, s):
        """
        :type s: str
        :rtype: List[str]
        """
        window=10
        result={}
        output=[]
        count=0
        print(len(s))
        if len(s)<window:
            return [s]
        for ix in range(0,len(s)-window+1):
            substring=s[ix:ix+window]
            sorted_substring=substring
            if sorted_substring not in result:
                result[sorted_substring]=0
            else:
                result[sorted_substring]+=1
        #print(result)
        for key, value in result.items():
            if (value)>0 and value>=1:
                print("val",key)
                output.append(key)
        return output


s="AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
s="AAAAAAAAAAA"
#output=["AAAAAAAAAA"]
print("result",Solution.findRepeatedDnaSequences(s))