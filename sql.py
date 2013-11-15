# helpers for dealing with sql database manipulation
import pymysql


# method for connecting to the database
# returns the connection
def connect(database):

	# create conncetion to supplied database
	con = pymysql.connect(host="localhost",user="root",passwd="bookeds",db=database)

	return con



# method for running a function
# on every result from a query
# takes function to apply, the sql query
# and the cursor for the database
def apply_search(fun,sql,cur):

	# execute the query
	cur.execute(sql)

	# now go through the result and execute function
	data = cur.fetchall()
	for row in data:
		fun(row)


