-- A script that updates the score of Bob to 10 in the table second_table
UPDATE second_table
SET score = 10
WHERE score = 14
ORDER BY score DESC;
