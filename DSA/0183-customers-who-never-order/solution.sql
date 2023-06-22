select name Customers from customers where id not in 
(select customerid from orders)
