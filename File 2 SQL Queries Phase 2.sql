#Table1 Queries
select shoes, price from table1 where category = "Men";
SELECT category, COUNT(DISTINCT color) AS num_colors
FROM products GROUP BY category;
Select max(price) from table1 where Category = "Men";
select min(price) from table1 where category = "Women";
select shoes, price from table1 where category = "Men";

#Table2 Queries
show databases;
use Capstone;
select * from table2;
select product_code, count(size) from table2 group by product_code;
select colour1,colour2,colour3,colour4,colour5,product_code from table2;
select product_code from table2 where colour2 = "NA";

Select product_code from table2 where colour1 ="Black" or colour2 = "Black" or colour3 = "Black" or colour4 = "Black" or colour5 = "Black";

#Table3 Queries
show databases;
use Capstone;
select * from table3;

select avg(comfort_rating) as avg_comfort from table3;
Select * from table3 where star_rating>=4;
select review from table3;
select quality from table3 where quality>7;
select sizes, avg(comfort) as avg_comfort from table3 group by sizes;

#Join Queries
select * from table1, table2, table3;

Select table1.shoes, table3.sizes from table1 JOIN table3 on table1.shoes = Table3.star_rating Where table1.Category="Men"
ORDER BY table3.star_rating DESC;
select table3.comfort, AVG(table1.category) AS avg_comfort from table1 JOIN table3 ON table1.category=table3.comfort GROUP BY table3.comfort;
select table1.shoes, table3.quality from table1 join table3 on table1.shoes=table3.quality;
select table1.shoes, table3.comfort FROM table1 JOIN table3 where comfort="Very Comfortable";
select table1.shoes, table2.product_code FROM table1 JOIN table2; 
SELECT product_code, shoes, size, star_rating FROM (
    SELECT product_code, shoes, size, star_rating,
           AVG(star_rating) OVER(PARTITION BY size) AS Avgstar_ratingBysize
    FROM table1, table2, table3) AS AvgStarBysize
WHERE star_rating > Avgstar_ratingBysize;
SELECT table1.shoes, table3.comfort FROM table1 JOIN table3 where comfort="Very Comfortable" or "Highly Comfortable";