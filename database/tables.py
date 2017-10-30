from peewee import *


"""
	TODO: put credentials in config file, use ConfigParser 
		  or something similar to parse them
"""
db = MySQLDatabase(
	'autoconnect', host='localhost', port=3306, user='root', password='')

class Base(Model):
	class Meta:
		database = db
	id = IntegerField(primary_key=True)
	created_on = DateTimeField(constraints=[SQL("DEFAULT (datetime('now'))")])


db.connect()

if __name__ == '__main__':
	db.create_tables([]) # TODO: update with table names

