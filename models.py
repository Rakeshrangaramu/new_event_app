from peewee import *

db = SqliteDatabase('event_app_db')

class User(Model):
	fullname = CharField()
	username = CharField()
	password = CharField()
	email_id = CharField()

	class Meta:
		database = db


class EventList(Model):
	event_name = CharField()
	description = TextField(null=True,default=000)
	fees = IntegerField(null=True)
	coordinator_name = CharField(null=True)
	coordinator_no = IntegerField(null=True)
	event_timings = CharField(null=True)

	class Meta:
		database = db


class ParticipantList(Model):
	# list_of_events = ForeignKeyField(EventList, backref="events")
	name = CharField()
	event_name = CharField()
	price = IntegerField()
	ph_no = IntegerField()

	class Meta:
		database = db

db.connect()
db.create_tables([User, ParticipantList, EventList])