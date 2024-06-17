import time
import rpyc
import sqlite3

class Database:
    def __init__(self, name):
        self._conn = sqlite3.connect(name)
        self._cursor = self._conn.cursor()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        self.connection.commit()
        return self._cursor.lastrowid

    def addition(self, row, table):
        query = "replace into {}  (message, status) values (?, ?)".format(table)
        rownumber= self.execute(query, (row["message"], row["status"]))
        return rownumber

    def updation(self, row, table):
        query= "UPDATE {} SET message = ? , status = ? WHERE cid = ?".format(table)
        rownumber = self.execute(query, (row["message"], row["status"], row["cid"]))
        return rownumber

    def viewresults(self, pid, table):
        query= "SELECT cid, message, status FROM {} WHERE cid = ?".format(table)
        self.execute(query, (pid,))
        fetrslt = self._cursor.fetchall()
        return fetrslt

class ServerMain(rpyc.Service):
    def exposed_add(self, i, j):
        return i + j

    def exposed_asyncadd(self, i, j):
        databaseconnection = Database("addition_Computations.db")
        row = {}
        print("Additional Computational row is Saved in a table")
        row["message"] = 0
        row["status"] = "Processing"
        rownumber =databaseconnection.addition(row, "additionresults")
        time.sleep(5)
        additionresult = i + j
        row = {}
        row["cid"] = rownumber
        row["message"] = additionresult
        row["status"] = "Completed"
        recordnumber=databaseconnection.updation(row, "additionresults")
        return recordnumber

 

    def exposed_sort(self, B):
        return sorted(B)

    def exposed_asyncsort(self, t):
        row = {}
        databseconnection = Database("sorted_Computations.db")
        print("Sorted Computational row is Saved in a table")
        row["message"] = ""
        row["status"] = "Processing"
        recordnumber =databseconnection.addition(row, "sortedresults")
        time.sleep(5)
        unsortingdata = list(t)
        sortresult = sorted(unsortingdata)
        response = ','.join(map(str, sortresult))
        row = {}
        row["cid"] = recordnumber
        row["message"] = response
        row["status"] = "Completed"
        recordnumber = databseconnection.updation(row, "sortedresults")
        return recordnumber

    def exposed_fetch_res(self, cid, databseconnection, tableName):
        databseconnection= Database(databseconnection)
        res = databseconnection.viewresults(cid, tableName)
        return res

t = rpyc.ThreadedServer(ServerMain, port=14789)
t.start()