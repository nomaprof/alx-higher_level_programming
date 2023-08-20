-- a script that displays the maximum tempeatures each state has recorded
SELECT state, max(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
