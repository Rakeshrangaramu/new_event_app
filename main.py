# Importing tkinter module and its functions
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

# Importing the image library
from PIL import Image, ImageTk

# Importing functions of views to link front-end and back-end
# from views import login, signup, add_events, show_events, show_events, add_participants, view_participants, remove_participants
from views import *

# Font Type
LARGE_FONT=("Verdana",20)


"""
The base class for the whole project. 
This contains all the different frames to change the view of the page. 
There are multiple containers that are defined below.
"""
class Event(Tk):
	

	def __init__(self,*args,**kwargs):

		Tk.__init__(self,*args,**kwargs)

		Tk.configure(self)
		
		container=Frame(self)

		# creating a container grid
		container.grid()
		container.grid_rowconfigure(0,weight=1)
		container.grid_columnconfigure(0,weight=1)
		
		# Geometry of the initial window
		self.geometry("600x400")

		# Creating a dictionary of frames to swap between frames.
		self.frames={}

		#updating the frames dictionary with all the frames that are created in the project. 
		for frm in FRAMES:
			frame=frm(parent=container,controller=self)
			self.frames[frm]=frame
			frame.grid(row=0,column=0,sticky="nsew")
		
		self.show_frame(Main)

	#displaying the required frame
	def show_frame(self,cont):
		frame=self.frames[cont]
		frame.tkraise()


class Home(Frame):
	
	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.controller=controller

		label = Label(self, text="Home", font=LARGE_FONT )
		label.grid(row=2, column=2, padx=10,pady=10)
		
		# button1=Button(self,text="Log In",command=lambda:controller.show_frame(LogIn))
		# button2=Button(self,text="Sign Up",command=lambda:controller.show_frame(SignUp))
		button3=Button(self,text="List of Events",command=lambda:controller.show_frame(EventLists))
		button4=Button(self,text="Add Events",command=lambda:controller.show_frame(AddEvents))
		button5=Button(self,text="Delete Event",command=lambda:controller.show_frame(DeleteEvent))
		button6=Button(self,text="View Event",command=lambda:controller.show_frame(ViewEvent))
		button7=Button(self,text="Add Participant",command=lambda:controller.show_frame(AddParticipants))
		button8=Button(self,text="View Participants",command=lambda:controller.show_frame(ViewParticipants))
		button9=Button(self,text="Remove Participant",command=lambda:controller.show_frame(RemoveParticipants))
		button10=Button(self,text="logout",command=lambda:controller.show_frame(Main))

		
		# button1.grid(row = 2, column = 2, padx=20, pady =20)
		# button2.grid(row = 3, column = 2, padx=20, pady =20)
		button3.grid(row = 4, column = 2, padx=20, pady =20)
		button4.grid(row = 5, column = 2, padx=20, pady =20)
		button5.grid(row = 6, column = 2, padx=20, pady =20)
		button6.grid(row = 7, column = 2, padx=20, pady =20)
		button7.grid(row = 8, column = 2, padx=20, pady =20)
		button8.grid(row = 9, column = 2, padx=20, pady =20)
		button9.grid(row = 10, column = 2, padx=20, pady =20)
		button10.grid(row = 11, column = 2, padx=20, pady =20)

class Main(Frame):
	
	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.controller=controller

		label = Label(self, text="Event", font=LARGE_FONT )
		label.grid(row=2, column=2, padx=10,pady=10)
		
		button1=Button(self,text="Log In",command=lambda:controller.show_frame(LogIn))
		button2=Button(self,text="Sign Up",command=lambda:controller.show_frame(SignUp))
		# button3=Button(self,text="List of Events",command=lambda:controller.show_frame(EventLists))
		# button4=Button(self,text="Add Events",command=lambda:controller.show_frame(AddEvents))
		# button5=Button(self,text="Delete Event",command=lambda:controller.show_frame(DeleteEvent))
		# button6=Button(self,text="View Event",command=lambda:controller.show_frame(ViewEvent))
		# button7=Button(self,text="Add Participant",command=lambda:controller.show_frame(AddParticipants))
		# button8=Button(self,text="View Participants",command=lambda:controller.show_frame(ViewParticipants))
		# button9=Button(self,text="Remove Participant",command=lambda:controller.show_frame(RemoveParticipants))

		button3=Button(self,text="List of Events",command=lambda:controller.show_frame(EventLists))
		button1.grid(row = 2, column = 2, padx=20, pady =20)
		button2.grid(row = 3, column = 2, padx=20, pady =20)
		# button3.grid(row = 4, column = 2, padx=20, pady =20)
		# button4.grid(row = 5, column = 2, padx=20, pady =20)
		# button5.grid(row = 6, column = 2, padx=20, pady =20)
		# button6.grid(row = 7, column = 2, padx=20, pady =20)
		# button7.grid(row = 8, column = 2, padx=20, pady =20)
		# button8.grid(row = 9, column = 2, padx=20, pady =20)
		# button9.grid(row = 10, column = 2, padx=20, pady =20)		
		button3.grid(row = 4, column = 2, padx=20, pady =20)

class LogIn(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.controller=controller

		self.log_in_label=Label(self,text="Username")
		self.password_label=Label(self,text="Password")

		self.log_in=Text(self,height=1,width=30)
		self.password=Text(self,height=1,width=30)

		button1=Button(self,text="Back",command=lambda:controller.show_frame(Main))
		button1.grid(row =2, column = 1, padx=20, pady =20)

		self.log_in_label.grid(row=3,column=1,padx=10,pady=10)
		self.password_label.grid(row=4,column=1,padx=10,pady=10)

		self.log_in.grid(row=3,column=2,padx=10,pady=10)
		self.password.grid(row=4,column=2,padx=10,pady=10)

		button2=Button(self,text="Log In",command=self.Log_In)
		button2.grid(row =8, column = 1, padx=60, pady =20)

	def Log_In(self):

		# if len(self.log_in.get('1.0','end-1c')) == 0:
		# 	self.popup=messagebox.showwarning('warning','Enter Username')

		# elif len(self.password.get('1.0','end-1c')) == 0:
		# 	self.popup=messagebox.showwarning('warning','Enter Password')

		# else:
		self.lin=self.log_in.get("1.0","end-1c")
		self.pd=self.password.get("1.0","end-1c")

		self.log_in.delete("1.0","end")
		self.password.delete("1.0","end")

		
		check=login(self.lin,self.pd)

		if check==True:
			self.controller.show_frame(Home)
		else:
			self.controller.show_frame(LogIn)
			

class SignUp(Frame):

	def __init__(self,parent,controller):
		Frame.__init__(self,parent)
		self.controller=controller

		button1=Button(self,text="Back",command=lambda:controller.show_frame(Main))
		button1.grid(row =2, column = 1, padx=20, pady =20)

		self.fullname_label=Label(self, text="Full Name")
		self.email_label=Label(self, text="Email ID")
		self.sign_up_label=Label(self, text="Username")
		self.password_label=Label(self, text="Password")

		self.fullname=Text(self, height=1, width=30)
		self.email=Text(self, height=1, width=30)
		self.sign_up=Text(self, height=1, width=30)
		self.password=Text(self, height=1, width=30)

		self.fullname_label.grid(row=4, column=1, padx=10, pady=10)
		self.email_label.grid(row=5, column=1, padx=10, pady=10)
		self.sign_up_label.grid(row=6, column=1, padx=10, pady=10)
		self.password_label.grid(row=7, column=1, padx=10, pady=10)

		self.fullname.grid(row=4, column=2, padx=10, pady=10)
		self.email.grid(row=5, column=2, padx=10, pady=10)
		self.sign_up.grid(row=6, column=2, padx=10, pady=10)
		self.password.grid(row=7, column=2, padx=10, pady=10)

		button2=Button(self,text="Sign Up",command=self.Sign_Up)
		button2.grid(row =8, column = 1, padx=60, pady =20)


	def Sign_Up(self):

		self.fn=self.fullname.get("1.0","end-1c")
		self.eid=self.email.get("1.0","end-1c")
		self.sup=self.sign_up.get("1.0","end-1c")
		self.pd=self.password.get("1.0","end-1c")

		self.fullname.delete("1.0","end")
		self.email.delete("1.0","end")
		self.sign_up.delete("1.0","end")
		self.password.delete("1.0","end")

		signup(self.sup,self.pd, self.fn, self.eid)

		self.controller.show_frame(Home)
	



class EventLists(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.controller=controller

		self.button1=Button(self,text="Back",command=lambda:controller.show_frame(Home))
		self.button1.grid(row =8, column = 5, padx=20, pady =20)

		self.button2=Button(self,text="select",command=self.select_event)
		self.button2.grid(row =9, column = 5, padx=20, pady =20)


		self.tree=Treeview( self, columns=('#1','#2','#3','#4'))
		
		self.tree.heading('#1',text='event name')

		self.tree.heading('#2',text='coord name')

		self.tree.heading('#3',text='coord Number')

		self.tree.heading('#4',text='fees')


		self.tree.column('#1',stretch=YES,anchor=CENTER)
		self.tree.column('#2',stretch=YES,anchor=CENTER)
		self.tree.column('#3',stretch=YES,anchor=CENTER)
		self.tree.column('#4',stretch=YES,anchor=CENTER)

		self.tree.grid(row=2, column=2 ,padx=30,pady=10,columnspan=3, sticky='nsew')

		self.tree['show']='headings'
		self.treeview=self.tree

		# events=[]
		events=show_events()
		print(events)
		
		for i in events:

			self.tree.insert("",'end',values=i)

		# coordinators=[]
		# coordinators=show_coordinator_name()

		# for i in coordinators:
		# 	self.tree.insert('','end',values=i)


	def select_event(self):

		self.curItem = self.tree.focus()
		print (self.tree.item(self.curItem))
		self.dict_item=self.tree.item(self.curItem)
		print(type(self.dict_item))
		self.product_list=[]
		self.product_list=self.dict_item.get('values')
		print(self.product_list)

		self.event_name=self.product_list[0]

		datalist=[]
		datalist=select(self.event_name)
		print(datalist)
		
		self.eventname=datalist[0]
		self.coodinatorname=datalist[1]
		self.coodinatorno=datalist[2]
		self.fees=datalist[3]
		self.description=datalist[4]

		messagebox.showinfo("description",self.description)

		# ve = ViewEvent(self, Event)
		# ve.details(self.eventname, self.coodinatorname, self.coodinatorno, self.fees)

		# self.controller.show_frame(ViewEvent)

	def add_events(self,evnt,cood,cood_no,fee):
		
		print(evnt,cood,cood_no,fee)

		self.tree.insert('',"end",values=(evnt,cood,cood_no,fee))





class AddEvents(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.controller=controller

		button1=Button(self,text="Back",command=lambda:controller.show_frame(Home))
		button1.grid(row =2, column = 1, padx=20, pady =20)

		self.event_label=Label(self, text="Event Name")
		self.event=Text(self, height=1, width=30)

		self.coordinator_label=Label(self, text="coordinator Name")
		self.coordinator=Text(self, height=1, width=30)

		self.coordinator_no_label=Label(self, text="coordinator Number")
		self.coordinator_no=Text(self, height=1, width=30)

		self.fees_label=Label(self, text="fees")
		self.fees=Text(self, height=1, width=30)

		self.timing_label=Label(self, text="Event time")
		self.time=Text(self, height=1, width=30)

		self.description_label=Label(self, text="description")
		self.description=Text(self, height=3, width=30)


		self.event_label.grid(row=4, column=1, padx=10, pady=10)
		self.event.grid(row = 4, column = 2, padx = 10, pady = 10)

		self.coordinator_label.grid(row=5, column=1, padx=10, pady=10)
		self.coordinator.grid(row = 5, column = 2, padx = 10, pady = 10)

		self.coordinator_no_label.grid(row=6, column=1, padx=10, pady=10)
		self.coordinator_no.grid(row = 6, column = 2, padx = 10, pady = 10)

		self.fees_label.grid(row=7, column=1, padx=10, pady=10)
		self.fees.grid(row = 7, column = 2, padx = 10, pady = 10)

		self.timing_label.grid(row=8, column=1, padx=10, pady=10)
		self.time.grid(row = 8, column = 2, padx = 10, pady = 10)

		self.description_label.grid(row=9, column=1, padx=10, pady=10)
		self.description.grid(row = 9, column = 2, padx = 10, pady = 10)

		button2=Button(self,text="Add Event",command=self.add_event)
		button2.grid(row = 9, column = 1, padx = 60, pady = 20)

	def add_event(self):

		if len(self.event.get('1.0','end-1c')) == 0:
			self.popup=messagebox.showwarning('warning','Add any event')
		else:
			self.evnt=self.event.get("1.0","end-1c")
			self.cood=self.coordinator.get("1.0","end-1c")
			self.cood_no=self.coordinator_no.get("1.0","end-1c")
			self.fee=self.fees.get("1.0","end-1c")
			self.evnt_time=self.time.get("1.0","end-1c")
			self.desc=self.description.get("1.0","end-1c")

			self.event.delete("1.0","end")
			self.coordinator.delete("1.0","end")
			self.coordinator_no.delete("1.0","end")
			self.fees.delete("1.0","end")
			self.time.delete("1.0","end")
			self.description.delete("1.0","end")



			add_events(self.evnt, self.cood,self.cood_no,self.fee,self.evnt_time,self.desc)

			el=EventLists(self,AddEvents)
			el.add_events(self.evnt, self.cood,self.cood_no,self.fee)


class DeleteEvent(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.controller=controller

		button1=Button(self,text="Back",command=lambda:controller.show_frame(Home))
		button1.grid(row =2, column = 1, padx=20, pady =20)

		self.event_label=Label(self, text="Event Name")
		self.event=Text(self, height=1, width=30)
		self.event_label.grid(row=4, column=1, padx=10, pady=10)
		self.event.grid(row = 4, column = 2, padx = 10, pady = 10)

		button2=Button(self,text="Delete Event",command=self.del_event)
		button2.grid(row = 8, column = 1, padx = 60, pady = 20)

	def del_event(self):

		if len(self.event.get('1.0','end-1c')) == 0:
			self.popup=messagebox.showwarning('warning','Add any event')
		else:
			self.evnt=self.event.get("1.0","end-1c")

			self.event.delete("1.0","end")

			remove_events(self.evnt)


class ViewEvent(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.controller=controller

		button1=Button(self,text="Back",command=lambda:controller.show_frame(Home))
		button1.grid(row =2, column = 1, padx=20, pady =20)

		self.tree1=Treeview( self, columns=('#1','#2','#3', '#4'))
		self.tree1.heading('#1',text='name')
		self.tree1.heading('#2',text='coordinatorname')
		self.tree1.heading('#3',text='coordinatorno')
		self.tree1.heading('#4',text='Price')

		self.tree1.column('#1',stretch=YES,anchor=CENTER)
		self.tree1.column('#2',stretch=YES,anchor=CENTER)
		self.tree1.column('#3', stretch=YES,anchor=CENTER)
		self.tree1.column('#4', stretch=YES,anchor=CENTER)
		self.tree1.grid(row=2, column=2 ,padx=10,pady=10,columnspan=2, sticky='nsew')
		self.tree1['show']='headings'
		# self.tree.bind('<Button-1>', self.select_item)

		self.name=''
		self.coodname=''
		self.coodno=''
		self.fee=''

		# self.tree.insert('', 'end', values=(self.name,self.coodname,self.coodno,self.fee))


	def details(self,eventname,coordinatorname,coordinatorno,fees):

		print(eventname,coordinatorname,coordinatorno,fees)

		self.name=eventname
		self.coodname=coordinatorname
		self.coodno=coordinatorno
		self.fee=fees
		# print(self.coodname)

		# self.add(self.name)

		self.tree1.insert("", 'end', values=(self.name,self.coodname,self.coodno,self.fee))
		# self.tree.insert("", 'end', values=(coordinatorname,coordinatorno,fees))
		# self.tree.insert('', 'end', values=(1,2,3,4))

	# def add(self,eventname):

	# 	print(eventname)
	# 	self.tree1.insert("","end",values=(eventname))



class AddParticipants(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.controller=controller
		
		button1=Button(self,text="Back",command=lambda:controller.show_frame(Home))
		button1.grid(row =2, column = 1, padx=20, pady =20)

		self.fullname_label=Label(self, text="Full Name")
		self.email_label=Label(self, text="Email ID")
		self.event_label=Label(self, text="Event")
		self.amount_label=Label(self, text="Amount")
		self.ph_no_label=Label(self, text="Phone Number")

		self.fullname=Text(self, height=1, width=30)
		self.email=Text(self, height=1, width=30)
		# self.event=Text(self, height=1, width=30)
		self.amount=Text(self, height=1, width=30)
		self.ph_no=Text(self, height=1, width=30)

		option=['']
		event_names=show_event_name()

		for r in event_names:
			option.append(r)

		options = list(set(option))		#to obtain only unique events 
		self.variable = StringVar(self)
		self.variable.set(options[0])		#Setting the default event
		self.select = OptionMenu(self, self.variable,*options,command=self.get_value).grid(row =6,column =2,padx=10,pady=10)
		

		self.fullname_label.grid(row=4, column=1, padx=10, pady=10)
		self.email_label.grid(row=5, column=1, padx=10, pady=10)
		self.event_label.grid(row=6, column=1, padx=10, pady=10)
		self.amount_label.grid(row=7, column=1, padx=10, pady=10)
		self.ph_no_label.grid(row=8, column=1, padx=10, pady=10)

		self.fullname.grid(row=4, column=2, padx=10, pady=10)
		self.email.grid(row=5, column=2, padx=10, pady=10)
		# self.event.grid(row=6, column=2, padx=10, pady=10)
		self.amount.grid(row=7, column=2, padx=10, pady=10)
		self.ph_no.grid(row=8, column=2, padx=10, pady=10)

		button2=Button(self,text="Add Participant",command=self.add_par)
		button2.grid(row =9, column = 1, padx=60, pady =20)


	def add_par(self):

		if len(self.fullname.get('1.0','end-1c')) == 0:
			self.popup=messagebox.showwarning('warning','Enter Full Name')

		elif len(self.email.get('1.0','end-1c')) == 0:
			self.popup=messagebox.showwarning('warning','Enter Email ID')

		# elif len(self.event.get('1.0','end-1c')) == 0:
		# 	self.popup=messagebox.showwarning('warning','Enter Event Name')

		elif len(self.amount.get('1.0','end-1c')) == 0:
			self.popup=messagebox.showwarning('warning','Enter Amount')

		elif len(self.ph_no.get('1.0','end-1c')) == 0:
			self.popup=messagebox.showwarning('warning','Enter Phone Number')

		else:
			self.sup=self.fullname.get("1.0","end-1c")
			self.pd=self.email.get("1.0","end-1c")
			self.evnt=self.name
			self.amt=self.amount.get("1.0","end-1c")
			self.pno=self.ph_no.get("1.0","end-1c")

			self.amount.delete("1.0","end")
			# self.event.delete("1.0","end")
			self.fullname.delete("1.0","end")
			self.email.delete("1.0","end")
			self.ph_no.delete("1.0","end")

			add_participants(self.sup,self.evnt,self.amt ,self.pno)
			# signup(self.sup,self.pd, self.fn, self.eid)

	
	def get_value(self,value):

		self.amount.delete("1.0","end")
		self.name=value

		self.fee=get_fees(self.name)

		self.amount.insert('end',self.fee)
			

class ViewParticipants(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.controller=controller

		button1=Button(self,text="Back",command=lambda:controller.show_frame(Home))
		button1.grid(row =5, column = 1, padx=20, pady =20)

		self.tree1=Treeview( self, columns=('#1','#2','#3', '#4'))
		self.tree1.heading('#1',text='name')
		self.tree1.heading('#2',text='event name')
		self.tree1.heading('#3',text='Price')
		self.tree1.heading('#4',text='Phone')

		self.tree1.column('#1',stretch=YES,anchor=CENTER)
		self.tree1.column('#2',stretch=YES,anchor=CENTER)
		self.tree1.column('#3', stretch=YES,anchor=CENTER)
		self.tree1.column('#4', stretch=YES,anchor=CENTER)
		self.tree1.grid(row=2, column=2 ,padx=10,pady=10,columnspan=2, sticky='nsew')
		self.tree1['show']='headings'
		
		participants=view_participants()

		for i in participants:

			self.tree1.insert("",'end',values=i)


class RemoveParticipants(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.controller=controller

		button1=Button(self,text="Back",command=lambda:controller.show_frame(Home))
		button1.grid(row =2, column = 1, padx=20, pady =20)

		self.participant_label=Label(self, text="Event Name")
		self.participant=Text(self, height=1, width=30)
		self.participant_label.grid(row=4, column=1, padx=10, pady=10)
		self.participant.grid(row = 4, column = 2, padx = 10, pady = 10)

		button2=Button(self,text="Delete Event",command=self.del_participant)
		button2.grid(row = 8, column = 1, padx = 60, pady = 20)

	def del_participant(self):

		if len(self.participant.get('1.0','end-1c')) == 0:
			self.popup=messagebox.showwarning('warning','Type a participant name')
		else:
			self.pcpnt=self.participant.get("1.0","end-1c")

			self.participant.delete("1.0","end")

			remove_participants(self.pcpnt)


FRAMES = (Main,
 Home,
 LogIn,
 SignUp,
 EventLists,
 AddEvents,
 DeleteEvent,
 ViewEvent,
 AddParticipants,
 ViewParticipants,
 RemoveParticipants
 )
app=Event()
app.mainloop()		







# def close_window():
# 	window.destroy()
# 	exit()

# window = tk.Tk()
# window.title("Event Management App")
# window.geometry("840x780+10+10")

# window.configure(background="white")
# tk.Label(window, text="Username:", bg="white", fg="black", font="none 12").grid(row=28, column=4, sticky="N")
# textentry = tk.Entry(window, width=30, bg="#bdc3c7")
# textentry.grid(row=28, column=5, sticky="N")

# tk.Label(window, text="Password:", bg="white", fg="black", font="none 12").grid(row=30, column=4, sticky="N")
# textentry = tk.Entry(window, width=30, bg="#bdc3c7")
# textentry.grid(row=30, column=5, sticky="N")
# tk.Button(window, text="Log In", width=14, command=login).grid(row=32, column=5, sticky="N")

# tk.Label(window, text="If have not yet signed up,", bg="white", fg="black", font="none 11").grid(row=34, column=5, sticky="N")
# tk.Label(window, text="Sign Up by clicking the button below.", bg="white", fg="black", font="none 11").grid(row=35, column=5, sticky="N")

# tk.Button(window, text="Sign Up", width=14, command=signup).grid(row=38, column=5, sticky="N")

# window.mainloop()