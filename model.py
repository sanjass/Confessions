from peewee import *
import datetime

db=MySQLDatabase('conf',user='root', passwd='***')

class Confession(Model):
	id=PrimaryKeyField()
	text=TextField()
	post_date=DateTimeField(default=datetime.datetime.now)

	class Meta:
		database=db

def create_tb():
	db.connect()
	db.create_tables([Confession])
	db.close()
	
