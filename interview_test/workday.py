"""

src	dest	dist
blr	hyd	500
del	mum	700
mum	del	700
kol	del	800
hyd	blr	500

SELECT *
FROM Distance t1
WHERE NOT EXISTS
 (
   SELECT * FROM Distance t2
   WHERE t1.destination = t2.source
     AND t1.source = t2.destination
     AND t1.destination > t2.destination
 );
"""