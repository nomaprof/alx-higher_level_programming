-- a script for computing the average temperature of various states in America
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP by city ORDER BY avg_temp DESC;
