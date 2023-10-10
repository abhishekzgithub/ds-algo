"""
100 columns
50 char
40 numeric
10 date


100gb redshift cluster
additional 5gb data
deletion of exisiting data


delete from <table> where( select * from old_table where date between 1970 and 1990)

insert into <table> 

bucket="xyz"
file="file.txt"


"""