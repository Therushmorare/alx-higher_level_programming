-- lists attributes with the same score in db

-- list the records
SELECT score, count(*) AS number FROM second_table
GROUP BY score DESC;
