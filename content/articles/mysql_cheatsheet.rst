MySQL Cheatsheet
################

:date: 2014-12-09
:tags: programming, linux, database, mysql
:slug: mysql-cheatsheet
:author: Gouthaman Balaraman
:description: Some notes on administering MySQL database

Here are some notes and commands on MySQL administration 

- Show a list of databases::

    show databases;
  
- Pick a database to use::

    use mydatabase;
    
- Show a list of tables after selecting a database::

    show tables;
    
- Updating a column with a constant value::

    UPDATE table1 SET column_a='value_a', column_b='value_b' WHERE query_id='1';
  
- Deleting rows that satisfy a criterion::

    DELETE FROM table1 WHERE query_id='1';
  
- Resetting the primary key value after any deletes that were performed::

    ALTER TABLE table1 AUTO_INCREMENT=1;
    

  
