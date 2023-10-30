"""
Table
A	    B
id      id
------------
1	    NULL
1	    1
NULL	1
1	    NULL
NULL	NULL
----
select a.*
from A a full outer join B b on a.id=b.id

A
--
1
1
NULL
1
NULL

----
select a.*
from A a right join B b on a.id=b.id

A       
NULL    
1       
1       
1       
1       
1       
1       
NULL    
NULL    


-----
select a.*
from A a left join B b on a.id=b.id


1
1
1
1
NULL
1
1
NULL


--------
select a.*
from A a join B b on a.id=b.id
---
1   
1   
1   
1   
NULL    
NULL    
NULL    
1   
1   
NULL    
NULL    
NULL    



1   1
1   1
1   1
1   1
NULL    NULL
NULL    NULL
NULL    NULL
1   1
1   1
NULL    NULL
NULL    NULL
NULL    NULL


Table
A	        B
Arun	    Run
Abhishek	Abhi
 	        Shek
            
             
"""
from collections import defaultdict
def func(list_a,list_b):
    sequence_matcher=defaultdict(list)
    for ele in list_a:
        for y in list_b:
            ele=ele.lower()
            y=y.lower()
            if y in ele:
                sequence_matcher[ele].append(1-(len(set(ele)-set(y))/len(ele)))
    return sequence_matcher

list_a=["Arun","Abhishek"]
list_b=["def","ghi","xyz"]
#print(func(list_a,list_b))


def reverse(val):
    start=0
    end=len(val)-1
    while start<end:
        val[start],val[end]=val[end],val[start]
        start+=1
        end-=1
    return val

abc=["a","b","c","d","e","f"]

print(reverse(abc))
#print(abc[::-1])
