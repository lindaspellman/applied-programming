# %%
# Review of SQLite and Learning More About It
# import pandas and sqlite3 modules
import pandas as pd
import sqlite3 as s 
# import plotnine as pn

# The purpose of this project is to work with a "book" table of the "library" database

# library TABLE: library_id, library_name, 
# A library can have many books and many borrowers
# borrower TABLE: borrower_id, first_name, last_name
# A borrower can have many books 
# book TABLE: book_id, author_first, author_last, summary, page_number, borrower_last_issued, issue_duration

# connect to library database
con = s.connect('c:\sqlite\db\library.db')

# %%
# create book table
df = pd.read_sql_query("""

CREATE TABLE book
    ( book_id, title, author_first, author_last, summary, page_count, borrower_last_issued, issue_duration)

""", con)

# %%
# insert data into book table 
book_data = pd.read_sql_query("""

INSERT INTO book
    ( 1, "Harry Potter and the Sorceror's Stone", "JK", "Rowling", "A young boy learns he's a wizard and attends his first year at a magical boarding school.", ) 
""", con)

# %%
drop_table = pd.read_sql_query("""

DROP TABLE book

""", con) 

# %%
"""
# To access the sqlite command line tool, navigate to your c:\sqlite folder with 
# "cd c:\sqlite" 
# and type in 
# "sqlite3" 
# This should bring up the sqlite prompt. 

To open a specific database
sqlite> .open c:\sqlite\db\chinook.db

# to open a specific database at the same time you are entering the sqlite command-line terminal
>sqlite3 c:\sqlite\db\chinook.db
SQLite version 3.13.0 2016-05-18 10:57:30
Enter ".help" for usage hints.
sqlite>

# If you start a session with a database name that does not exist, the sqlite3 tool will create the database file.
# for example
>sqlite3 c:\sqlite\db\sales.db
SQLite version 3.29.0 2019-07-10 17:32:03
Enter ".help" for usage hints.
sqlite>
# sales.db did not exist but now does

# To show all available commands and their purpose
.help

# To show all databases in the current connection
.databases

# To show all tables
.table

# To add an additional database in the current connection
sqlite> ATTACH DATABASE "c:\sqlite\db\chinook.db" AS chinook;

# To exit the sqlite3 program
.exit 
"""
# %%
