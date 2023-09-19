"""
Chandra shekhar Meena9:31 PM
Large number of files with large data

Device_Id Segment
1 a,b,c
2 b,d
3 e,a,c
4 o,d,e
5 p


segment_a segment_b
1           1
0           2
3           0
0           0
0           0

def helper_fn(row):
    if "b" in row:
        return "b"
    elif "c" in row:
        return "c"
    elif "d" in row:
        return "d"
    else:
        return None





Large number of files with large data

Device_Id Platform
1 ios
2 android,ios
3 android
4 android,ios
5 ios

Small File

Segments
b
c
d

b c d
1 1
2 
segment device_id
b       1,2
c       1,3
d       4

a. Output the Ids per segment wise, only for the segments present in Segments file
b. Output the Ids count per segment wise, only for the segments present in Segments file
c. output one Device_Id, one segment, one platform per row, only for the segments present in Segments file
L1 Tech Round - Abhishek
"""

# from pyspark.sql import SparkSession

# sc=SparkSession.sparkContext.builder.app("local").getOrCreate()

# # abc1={"Device_Id" Segment
# # 1 a,b,c
# # 2 b,d
# # 3 e,a,c
# # 4 o,d,e
# # 5 p}

# Device_Id Segment
# 1 a,b,c
# 2 b,d
# 3 e,a,c
# 4 o,d,e
# 5 p
from pyspark.sql import functions as F
spark=None
arrayData = [
        (1,['a','b','c']),
        (2,['b','d']),
        (3,['e','a','c']),
        (4,["o","d","e"]),
        (5,['p'])]

df = spark.createDataFrame(data=arrayData, schema = ['deviceId','segment'])
df.show()

df1=df.select(df.deviceId,F.explode(df.segment))
df1.show()
df1.groupBy("col").agg(F.collect_list("deviceId")).show()

"""
+--------+---------+
|deviceId|  segment|
+--------+---------+
|       1|[a, b, c]|
|       2|   [b, d]|
|       3|[e, a, c]|
|       4|[o, d, e]|
|       5|      [p]|
+--------+---------+

+--------+---+
|deviceId|col|
+--------+---+
|       1|  a|
|       1|  b|
|       1|  c|
|       2|  b|
|       2|  d|
|       3|  e|
|       3|  a|
|       3|  c|
|       4|  o|
|       4|  d|
|       4|  e|
|       5|  p|
+--------+---+

+---+----------------------+
|col|collect_list(deviceId)|
+---+----------------------+
|  c|                [1, 3]|
|  b|                [1, 2]|
|  a|                [1, 3]|
|  d|                [2, 4]|
|  e|                [3, 4]|
|  o|                   [4]|
|  p|                   [5]|
+---+----------------------+

"""

"""

Given a string s, find the length of the longest substring without repeating characters.
Example 1:
Input: s = "abcadeacbb"
Output: 5
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
def longest_substring(inp_str):
    max_length=0
    index_dict={}
    i=0
    for j in range(len(inp_str)):
        if inp_str[j] in index_dict and i<=len(inp_str):
            i=index_dict[inp_str[j]]+1
        else:
            max_length=max(j-i+1,max_length)
        index_dict[inp_str[j]]=j
    return max_length

print(longest_substring("pwwkew"))
print(longest_substring("bbbbb"))
print(longest_substring("abcadeacbb"))
print(longest_substring("abcabcbb"))


