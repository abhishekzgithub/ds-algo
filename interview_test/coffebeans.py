"""
Sales table - client id, date, revenue, spend, product_id : sortkey date desc, dist_key (client_id,product_id)%1024
Customer table - clientId, client name, cost_center(region)
Product table - clientId, product id, product name


Reports : 
        1. Get total profit for a client 
        2. Get total profit for a client for a specific date
        3. Get total profit for a client for a specific date range(Week, month, year, custom range)


select sum(revenue-spend)
from salesTable        
group by clientid

partition by and distkey
watermark and window
materialised and table
"""