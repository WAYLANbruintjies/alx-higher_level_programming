-- Lists the number of records with the same score in table
SELECT score, COUNT(1) AS number FROM second_table
GROUP BY score
ORDER BY score DESC;
