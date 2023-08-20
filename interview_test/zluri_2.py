# Infinity Market is a popular ecommerce company that does orders of around 5 million per day. It has detected an increased number of fraudulent transactions by credit card numbers that are either stolen or non-existent. To tackle this, the Fraud team in the company has come up with a few early rules to flag potential fraudulent transactions. These are the rules that could potentially involve a fraud:


# 1. If a user has been using unique credit card numbers for more than last 5 transaction  attempts(5 different cards)

# 2. If a user places orders from more than 4 different countries on the same day.

# 3. If a user's last 3 transaction attempts failed


# You have two tables that record payment transaction attempts and orders placed:  (daily)  Batch 


# 1. Payment Transaction



# user_id 	| 	ip_address 	| 	payment_id	|  card_number	|  status 	| 	timestamp

# With credit as (
# Select user_id, card_number, dense_rank()over(order by timestamp desc) as transaction_time from payment
# )
# Select count (distinct card_number)as ttl_cards
# From credit
# Where transaction_time  in (1,2,3,4,5)
# Group by user_id,card_number
# having ttl_cards > 5

# Create table flagged_user (
# User_id varchar,
# Card_number varchar,
# Status varchar,
# Attempts int,
# last_run_Timestampz timestamp
# )

# status could be - successful or declined



# 2. Orders


# user_id		| 	ip_address 	| 	order_id 	| country 	| 	payment_id 	| status  | timestamp 	




# status could be - successful or declined
