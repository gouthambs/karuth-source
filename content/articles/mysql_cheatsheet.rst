MySQL Cheatsheet
################

:date: 2014-12-09
:tags: programming, linux, database, mysql
:slug: mysql-cheatsheet
:author: Gouthaman Balaraman
:description: Some notes on administering MySQL database

Here are some notes and commands on MySQL administration 

- Create a database::

    CREATE DATABASE mydatabase;
    
- Creating a user for the database::

    CREATE USER 'testuser'@localhost IDENTIFIED BY 'password';
    
- Granting ``testuser`` all privileges on a table::

    GRANT ALL PRIVILEGES ON mydatabase.* TO 'testuser'@localhost;

- Show a list of databases::

    SHOW DATABASES;
  
- Pick a database to use::

    USE mydatabase;
    
- Show a list of tables after selecting a database::

    SHOW TABLES;
    
- Updating a column with a constant value::

    UPDATE table1 SET column_a='value_a', column_b='value_b' WHERE query_id='1';
  
- Deleting rows that satisfy a criterion::

    DELETE FROM table1 WHERE query_id='1';
  
- Resetting the primary key value after any deletes that were performed::

    ALTER TABLE table1 AUTO_INCREMENT=1;
    
- Disabling safe update mode, and turning back on::

    SET SQL_SAFE_UPDATES = 0;
    DELETE FROM table1 WHERE query_id='1';
    SET SQL_SAFE_UPDATES = 1;
    
  Use the above with caution.
  


  
