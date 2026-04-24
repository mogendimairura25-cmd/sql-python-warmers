SELECT product, SUM(sales)
FROM sales
GROUP BY product;