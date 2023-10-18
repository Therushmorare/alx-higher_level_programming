-- creates a table called first_table.

-- create the table.
CREATE TABLE IF NOT EXISTS second_table (id INT,
       name VARCHAR(256),
       score INT);

-- insert into the table	with 4 ids.
INSERT INTO second_table (id, name, score) VALUES
       (1, "John", 10),
       (2, "Alex", 3),
       (3, "Bob", 14),
       (4, "George", 8);
