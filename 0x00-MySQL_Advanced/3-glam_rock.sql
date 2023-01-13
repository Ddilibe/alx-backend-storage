-- Script that lsits all bands with Glam Rock
-- As their main style ranked by their longevity
SELECT band_name, 
	(IFNULL(split, 2022) - formed) AS lifespan 
FROM metal_bands 
WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;

