"""
event
sponsor
visitor
product
interaction


dim:
sponsor
["id"]


intermediate_sponsor_visitor
sponsor visitor ratings

visitor
["id"]


select * 
from sponsor s  
 join intermediate_sponsor_visitor as int on s.id=int.sponsor
 join visitor v on v.id=int.visitor

visitor can interact with multiple sponsor to get the score
 get cumulative engagement score of visitor in an event
 event:
 [id]

 interaction:
 [id,eventid,visitorid,datetime,score]

 select sum(i.score) over(partition by i.visitorid)
 from event e left join interaction i  
 on i.eventid=e.id
 
 #group by i.id

# where s.visitorid =v.visitorid
# or v.sponsorid=s.sponsorid

product

fact:
event
interaction

"""

abc=[0,0,0,1,1,0,0,1,1,2,2]

def dutch_flag(nums):
    """
    focus on mid
    """
    i,mid,j=0,0,len(nums)-1
    while mid<j:
        if nums[mid]==0:
            nums[i],nums[mid]=nums[mid],nums[i]
            i+=1
            mid+=1
        elif nums[mid]==1:
            mid+=1
        else:
            nums[mid],nums[j]=nums[j],nums[mid]
            j-=1
    return nums

print(dutch_flag(abc))

def count_frequency(abc):
    freq={}
    for ele in abc:
        if ele in freq:
            freq[ele]+=1
        else:
            freq[ele]=0
    print(freq)

count_frequency(abc)
