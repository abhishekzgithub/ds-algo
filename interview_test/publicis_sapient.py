"""
Give a timeseries data and userid
. find the session where the user is inactive for 30 minutes
. the user is logged in for 2 hours and a new session is generated
Find the user active per day
Find how much time it has spent.

timestamp           userid
2023-01-01 1:05:00  u1
2023-01-01 2:05:00  u1
2023-01-12 1:05:00  u2
2023-01-01 1:05:00  u1
2023-01-12 1:35:00  u2

approaches needs to explore:
read text file and convert it to datafrmae by removing the unnecessary parts
group by dates
revisit pyspark window
    to_date of sql
    extract_date of sql
save to parquet
"""