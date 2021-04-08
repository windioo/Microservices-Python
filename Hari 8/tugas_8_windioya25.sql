USE `classicmodels`;

select a.orderNumber AS Order_Number, a.orderDate as Order_Date, 
b.customerName as Customer_Name, b.city as City,b.country as Country, 
c.quantityOrdered as Quantity_Ordered,
d.productName as Product_Name
from orders a
inner join customers b on a.customerNumber = b.customerNumber
inner join orderdetails c on a.orderNumber = c.orderNumber
inner join products d on c.productCode = d.productCode
where d.productName = "1992 Ferrari 360 Spider red" and a.orderDate between "2004-8-1" and "2004-12-1"