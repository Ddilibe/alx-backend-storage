-- Script that ranks countries origins of bands
-- Ordered by the number of unique fans
SELECT DISTINCT 
	origin,
	SUM(fans) AS `nb_fans` 
FROM metal_bands GROUP BY origin ORDER BY nb_fans DESC;
