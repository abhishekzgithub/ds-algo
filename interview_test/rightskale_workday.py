"""
input="abhishek"
ouput=""
"""
vowel_dict={
"a":0,
"e":0,
"i":0,
"o":0,
"u":0

}

def vowe_count(inp):
    for ele in inp:
        if ele in vowel_dict:#.get(,None):
            vowel_dict[ele]+=1
    return vowel_dict
input1="abhishek"
print(vowe_count(input1))

"""
	A	B		A					
	1	1		1		1	1		
	1	1		1		1	1		from
	0	0		0		0	0		where
	0	null		null		0	null		group by
	2					2	null		having
	null					null	null		select
									order by
-----------------------
A	B
1	1
1	1
0	0
0	null
2
null
                                    
inner join:
A	B
0	0
0	0
1	1
1	1
1	1
1	1

left join:
A	B
0	0
0	0
1	1
1	1
1	1
1	1
2	null
null null
	
right join
A	B
0	0
0	0
1	1
1	1
1	1
1	1
null null

left outer join
A	B
0	0
0	0
1	1
1	1
1	1
1	1
2	null
null null

# difference between merge , join, concat
merge:
joins the data on multiple indexes

JOIN:
it joins the data on single index

CONCAT:
With concatenation, your datasets are 
just stitched together along an axis — 
either the row axis or column axis.
                                    									
input	Abhishek kumar								
output	a.k.								
									
	ltrim(x,1)								
	confirmed dim								
	degenerate dim								
									
	prophecy								
	ads								
	redshift								
	snaplogic								
	s3								
	redshift								
	python								
	datawarehouse								
	optimization								
	how datawarehouse work								
	cte								
	etl related projects								
	install talend								
	chinmay sahane								
	virtusa								


"""