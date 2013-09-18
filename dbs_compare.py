import MySQLdb as mdb
con = mdb.connect('localhost', 'root', 'password')
with con:
    cur = con.cursor()
    query = "SELECT T1.column1 FROM db1.table1 T1 "+\
    "WHERE T1.column1 NOT IN (SELECT T2.column2 FROM db2.table2 T2) "+\
    "UNION " +\
    "SELECT T2.column2 FROM db2.table2 T2 " +\
    "WHERE T2.column2 NOT IN (SELECT T1.column1 FROM db1.table1 T1)"    
    cur.execute(query)
    if cur.rowcount > 0:
                print "Not Equal"
                for i in range(cur.rowcount):
                                row = cur.fetchone()
                                print row[0]
    else:
                print "Equal"
