from tkinter import *

class Questionnaire(Frame):
	# GUI Setup
	
	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.createProgSelect()
		
		
	def createProgSelect(self):
		# Create widgets to select a degree programme from a list
		lblProg = Label(self, text='Degree Programme:', font=('MS', 8,'bold'))
		lblProg.grid(row=0, column=0, columnspan=2, sticky=NE)
		
		self.listProg = Listbox(self, height= 3)
		scroll = Scrollbar(self, command= self.listProg.yview)
		self.listProg.configure(yscrollcommand=scroll.set)
		
		self.listProg.grid(row=0, column=2, columnspan=2, sticky=NE)
		scroll.grid(row=0, column=4, sticky=W)
		
		for item in ["CS", "CS with", "BIS", "SE", "Joints",""]:
			self.listProg.insert(END, item)
		self.listProg.selection_set(END) 
				
		
root = Tk()
root.title("Teamwork Questionnaire")
app = Questionnaire(root)
root.mainloop()