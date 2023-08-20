# create table Orders
#    (
#    OrderId int NOT NULL AUTO_INCREMENT PRIMARY KEY,
#    CustomerId int,
#    OrderDate DATE
#    );

#     create table OrderDetails
#    (
#    OrderId int NOT NULL,

#    ProductId int,

#    UnitPrice int,

#     Quantity int

#    );


# insert into Orders values ('10248',             3,            '1996-07-04');

# insert into Orders values ('10249',             1,            '1996-07-05');

# insert into Orders values ('10253',             2,            '1996-07-10');

# insert into Orders values ('10274',             3,            '1996-08-06');

# insert into Orders values ('10275',             4,            '1996-08-07');

# insert into Orders values ('10296',             5,            '1996-09-03');

 

# insert into OrderDetails values (10248,   11,          14,          12);

# insert into OrderDetails values (10248,   42,          9,            10);

# insert into OrderDetails values (10248,   72,          34,          5);

# insert into OrderDetails values (10249,   14,          18,          9);

# insert into OrderDetails values (10249,   51,          42,          40);

# insert into OrderDetails values (10253,   31,          10,          20);

# insert into OrderDetails values (10253,   39,          14,          42);

# insert into OrderDetails values (10253,   49,          16,          40);

# insert into OrderDetails values (10274,   71,          17,          20);

# insert into OrderDetails values (10274,   72,          27,          7);

# insert into OrderDetails values (10275,   24,          3,            12);

# insert into OrderDetails values (10275,   59,          44,          6);

# insert into OrderDetails values (10296,   11,          16,          12);

# insert into OrderDetails values (10296,   16,          13,          30);

# insert into OrderDetails values (10296,   69,          28,          15);


# Please Write a query to get the customer with the highest total order value for each year-month.

 

# The result should include the columns year, month, customerid, total_monthly_order_value. See the output under the sample data tables below for the correct data format to use. Be sure to match the format exactly. The output should be ordered by year and month in ascending order.