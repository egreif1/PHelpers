# helpers for dealing with sql database manipulation
import pymysql


# method for connecting to the database
# returns the connection
def connect(database):

	# create conncetion to supplied database
	con = pymysql.connect(host="localhost",user="root",passwd="bookeds",db=database)

	return con



