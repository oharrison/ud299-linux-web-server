#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys

if __name__ == '__main__':
    con = None
    try:
        # Establish connection to our database
        con = psycopg2.connect("dbname='testdb' user='vagrant' password='secret'")
        cursor = con.cursor()

        # Create a Cars table with id, name, and price fields
        cursor.execute("CREATE TABLE Cars(Id INTEGER PRIMARY KEY, Name VARCHAR(20), Price INT)")
        
        # Insert these records into the Cars table
        cursor.execute("INSERT INTO Cars VALUES(1,'Audi',10243)")
        cursor.execute("INSERT INTO Cars VALUES(2,'Mercedes', 28763)")
        cursor.execute("INSERT INTO Cars VALUES(3,'Skoda', 62432)")
        cursor.execute("INSERT INTO Cars VALUES(4,'Volvo', 67234)")
        cursor.execute("INSERT INTO Cars VALUES(5,'Bentley',45000)")
        cursor.execute("INSERT INTO Cars VALUES(6,'Citroen',24000)")
        cursor.execute("INSERT INTO Cars VALUES(7,'Hummer',40032)")
        cursor.execute("INSERT INTO Cars VALUES(8,'Volkswagen',21603)")
        
        # Commit operations to our database
        con.commit()
    
    except psycopg2.DatabaseError, e:
        # Rollback our database if any error arises
        if con:
            con.rollback()
        print 'Error %s' % e    
        sys.exit(1)
    finally:
        # Finish up by closing the connection to our database
        if con:
            con.close()
