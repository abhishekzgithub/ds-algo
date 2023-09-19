"""
Mphasis

https://stackoverflow.com/questions/60715057/what-is-the-solution-for-this-sql-complex-interview-question
Input	
network: 	 
Source	Destination	Distance
Bangalore	Hyderabad	400
Hyderabad	Bangalore	400
Mumbai	Delhi	400
Delhi	Mumbai	400
Chennai	Pune	400
Pune	Chennai	400

 Output	 	 
Source	Destination	Distance
Bangalore	Hyderabad	400
Mumbai	Delhi	400
Chennai	Pune	400

select n1.source, n1.destination, n1.distance
from network as n1 , network as n2
where n1.source=n2.destination
and n2.source!=n1.destination

"""


S1= "Hello"; S2= "World" #, o/p - "HWeolrllod"

i=0
j=0
output=""
while i< len(S1) and j<len(S2):
    output+=str(S1[i])+str(S2[j])
    i+=1
    j+=1

while i<len(S1):
    output+=str(S1[i])
    i+=1

while j<len(S2):
    output+=str(S1[j])
    j+=1
print(output)