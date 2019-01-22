from models import User, EventList, ParticipantList

def signup(f_username, f_password, f_fullname, f_email):
	# fullname = input("Enter Full Name: ")
	# username = input("Enter username: ")
	# password = input("Enter password: ")
	# email_id = input("Enter email id: ")
	fullname = f_fullname
	username = f_username
	password = f_password
	email_id = f_email
	print("Created New Sign Up")

	user = User.create(fullname=fullname, username=username, password=password, email_id=email_id)


def login(f_username, f_password):
	# username = input("Enter username: ")
	# password = input("Enter password: ")

	username = f_username
	password = f_password

	print(User.username)

	for person in User.select():
		print(person)
		if username == person.username:
			print(1)
		else:
			print("invalid username")

	for person in User.select().where(User.username == username):
		if password == person.password:
			print("Logged In")
			return True
		else:
			print("Invalid Password")
			return False


def add_events(eventname,coor_name,cood_no,fee,time,description):
	# count = int(input("Enter how many events to add: "))
	# for i in range(count):
	# event = EventList.create(event_name=input("Enter event: "))
	event = EventList.create(event_name=eventname,
			fees=fee,
			coordinator_name=coor_name,
			coordinator_no=cood_no,
			event_timings=time,description=description)

def select(event_name):
	query=EventList.select().where(EventList.event_name==event_name)
	# event=list(query)
	event_list=[]
	for event in query:
		print(event.event_name,event.fees)
		event_list.append(event.event_name)
		event_list.append(event.coordinator_name)
		event_list.append(event.coordinator_no)
		event_list.append(event.fees)
		event_list.append(event.description)

	return event_list	
	# return query

def show_events():

	# query=EventList.select()
	# topping=list(query)
	# return topping

	datalist=[]

	for event in EventList.select():
		print(event.event_name)

		datalist.append([event.event_name,event.coordinator_name,event.coordinator_no,event.fees])
		# datalist.append(event.coordinator_name)
		# datalist.append(event.coordinator_no)
		# datalist.append(event.fees)

	return datalist	

def show_event_name():

	datalist=[]

	for event in EventList.select():

		datalist.append(event.event_name)

	return datalist	

def get_fees(event_name):

	query=EventList.select().where(EventList.event_name==event_name)

	event_fees=[]

	for event in query:

		event_fees.append(event.fees)

	return event_fees	


	


def remove_events(eventname):
	# event_name = input("Enter event name to remove: ")
	# event=EventList.get(EventList.event_name=eventname)
	# query=EventList.select().where(EventList.event_name=eventname).get()

	# query.delete_instance()
	# n=query.execute()
	# print(n)
	pass

def add_participants(participant_name,event,amount,ph_no):
	# participant_name = input("Enter the participant name: \n")
	# event = input("Enter the choice event name from the below events:\n\
	# 	1. CS 1.6\n\
	# 	2. GoogleIt\n\
	# 	3. Treasure Hunt\n")
	# amount = int(input("Enter the ticket price: "))
	# ph_no = int(input("Enter participant's phone number: "))

	participant = ParticipantList.create(name=participant_name, event_name=event, price=amount, ph_no=ph_no)


def view_participants():
	
	part_list=[]

	for part in ParticipantList.select():
		part_list.append([part.name,part.event_name,part.price,part.ph_no])

	return part_list	

		# print(event.name, event.event_name, event.price, sep=" - ")

def remove_participants(part):
	ParticipantList.delete_instance(part)
	


if __name__ == '__main__':
	ch = input("log in - 1,\n\
	sign up - 2, \n\
	view participants - 3, \n\
	Add events - 4 \n\
	Show events - 5: \n\
	Remove events - 6: ")

	if ch == "1":
		login()
	elif ch == "2":
		signup()
	elif ch == "3":
		view_participants()
	elif ch == "4":
		add_events()
	elif ch == '5':
		show_events()
	elif ch == '6':
		remove_events()
