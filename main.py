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
		self.geometry("1600x920")

		# Creating a dictionary of frames to swap between frames.
		self.frames={}

		#updating the frames dictionary with all the frames that are created in the project. 
		for frm in (Main ,Home, LogIn, SignUp, EventLists, AddEvents, DeleteEvent,ViewEvent, AddParticipants, ViewParticipants, RemoveParticipants):
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

		
		button1.grid(row = 2, column = 2, padx=20, pady =20)
		button2.grid(row = 3, column = 2, padx=20, pady =20)
		# button3.grid(row = 4, column = 2, padx=20, pady =20)
		# button4.grid(row = 5, column = 2, padx=20, pady =20)
		# button5.grid(row = 6, column = 2, padx=20, pady =20)
		# button6.grid(row = 7, column = 2, padx=20, pady =20)
		# button7.grid(row = 8, column = 2, padx=20, pady =20)
		# button8.grid(row = 9, column = 2, padx=20, pady =20)
		# button9.grid(row = 10, column = 2, padx=20, pady =20)		


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

		button1=Button(self,text="Back",command=lambda:controller.show_frame(Home))
		button1.grid(row =4, column = 5, padx=20, pady =20)

		self.tree=Treeview( self, columns=('#1'))
		self.tree.heading('#1',text='event name')

		self.tree.column('#1',stretch=YES,anchor=CENTER)
		self.tree.grid(row=2, column=1 ,padx=300,pady=10,columnspan=3, sticky='nsew')

		self.tree['show']='headings'
		self.treeview=self.tree

		events=show_events()

		for i in events:
			self.tree.insert("",'end',values=i)


class AddEvents(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.controller=controller

		button1=Button(self,text="Back",command=lambda:controller.show_frame(Home))
		button1.grid(row =2, column = 1, padx=20, pady =20)

		self.event_label=Label(self, text="Event Name")
		self.event=Text(self, height=1, width=30)
		self.event_label.grid(row=4, column=1, padx=10, pady=10)
		self.event.grid(row = 4, column = 2, padx = 10, pady = 10)

		button2=Button(self,text="Add Event",command=self.add_event)
		button2.grid(row = 8, column = 1, padx = 60, pady = 20)

	def add_event(self):

		if len(self.event.get('1.0','end-1c')) == 0:
			self.popup=messagebox.showwarning('warning','Add any event')
		else:
			self.evnt=self.event.get("1.0","end-1c")

			self.event.delete("1.0","end")

			add_events(self.evnt)


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
		self.event=Text(self, height=1, width=30)
		self.amount=Text(self, height=1, width=30)
		self.ph_no=Text(self, height=1, width=30)

		self.fullname_label.grid(row=4, column=1, padx=10, pady=10)
		self.email_label.grid(row=5, column=1, padx=10, pady=10)
		self.event_label.grid(row=6, column=1, padx=10, pady=10)
		self.amount_label.grid(row=7, column=1, padx=10, pady=10)
		self.ph_no_label.grid(row=8, column=1, padx=10, pady=10)

		self.fullname.grid(row=4, column=2, padx=10, pady=10)
		self.email.grid(row=5, column=2, padx=10, pady=10)
		self.event.grid(row=6, column=2, padx=10, pady=10)
		self.amount.grid(row=7, column=2, padx=10, pady=10)
		self.ph_no.grid(row=8, column=2, padx=10, pady=10)

		button2=Button(self,text="Add Participant",command=self.add_par)
		button2.grid(row =9, column = 1, padx=60, pady =20)


	def add_par(self):

		if len(self.fullname.get('1.0','end-1c')) == 0:
			self.popup=messagebox.showwarning('warning','Enter Full Name')

		elif len(self.email.get('1.0','end-1c')) == 0:
			self.popup=messagebox.showwarning('warning','Enter Email ID')

		elif len(self.event.get('1.0','end-1c')) == 0:
			self.popup=messagebox.showwarning('warning','Enter Event Name')

		elif len(self.amount.get('1.0','end-1c')) == 0:
			self.popup=messagebox.showwarning('warning','Enter Amount')

		elif len(self.ph_no.get('1.0','end-1c')) == 0:
			self.popup=messagebox.showwarning('warning','Enter Phone Number')

		else:
			self.sup=self.fullname.get("1.0","end-1c")
			self.pd=self.email.get("1.0","end-1c")
			self.evnt=self.event.get("1.0","end-1c")
			self.amt=self.amount.get("1.0","end-1c")
			self.pno=self.ph_no.get("1.0","end-1c")

			self.amount.delete("1.0","end")
			self.event.delete("1.0","end")
			self.fullname.delete("1.0","end")
			self.email.delete("1.0","end")
			self.ph_no.delete("1.0","end")

			add_participants(self.sup,self.evnt,self.amt ,self.pno)
			# signup(self.sup,self.pd, self.fn, self.eid)


class ViewParticipants(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.controller=controller

		button1=Button(self,text="Back",command=lambda:controller.show_frame(Home))
		button1.grid(row =2, column = 1, padx=20, pady =20)


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