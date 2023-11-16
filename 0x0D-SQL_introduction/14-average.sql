-- script that computes the score average of all records
-- in the table second_table of the database hbtn_0c_0 in your MySQL server.
-- ALTER TABLE second_table ADD COLUMN average FLOAT;

-- Upsate the average score as a new record.
UPDATE second_table set average = (SELECT AVG(score) FROM second_table);
