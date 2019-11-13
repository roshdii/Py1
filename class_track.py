#! /usr/bin/env python3.6
import csv 
import os 
import re 


#01273145549
#fb/arahman.hamdy

closing_______line = "-----------------"
dict_header = ["sid","sname","sage","semail","smobile"]

class MENU : 
	def __init__(self,menu_list):
		self.inlist = menu_list 
	
	def edit(self,menu_li):
		self.inlist = menu_li

	def draw(self):
		print(closing_______line)
		idx = 1
		for i in self.inlist:
			print(str(idx)+"- "+i)
			idx+= 1
		print(closing_______line)

	def get(self):
		print("Enter no. or 'identical' Name of item to choose [0 to exit menu ]")
		print(closing_______line)
		x = input("-> ")
		# print(str(type(x)) == "<class 'str'>")
		if x.isdigit() : 
			x = int(x) 
			if x >= 0 and x <= len(self.inlist) :
				#print("i/p = ",x,)
				print("Selected Element :-> ",self.inlist[x-1])
				print(closing_______line)
				return x
			else :
				input("out of range input ")
				return -1 

		elif str(type(x)) == "<class 'str'>":
			idx = 1 
			for i in self.inlist :
				# print("idx= ",idx,"item= ",i)
				if i == x :
					#print("i/p = ",x,"idx=",str(idx),)
					print("Selected Element :-> ",self.inlist[idx-1])
					print(closing_______line)
					return str(x)
				idx += 1 
		else :
			input("Invalid input for menu items") 
			return -1 

		

class Track:
	track_count = 0 
	track_list = []
	selected_track = 0 
	track_list_obj = MENU(track_list) 

	def __init__(self,tname,isop = True ):
		self.name = tname
		self.students = []
		self.st_count = 0
		self.is_open = isop
		Track.track_count += 1 

	def add_student(self,sid=None,**kwargs):
		print("Add student in ",self.name) 
		#comes from user without sid 
		if self.is_open == False : 
			input("track "+self.name+" is not open !!") 
			return
		if sid == None :
			# input("none sid")
			for st in self.students :
				# print(st)
				# print(kwargs)
				if len(kwargs) > 0 and st.name == kwargs["sname"] :
					input("student "+st.name+" found before ")
					return  
			
			print("New data input from user")
			self.st_count +=  1
			sid = self.st_count
			temp_dic = {
					"sid":sid,
					"sname":input("Enter Student Name : "),
					"sage":input("Enter Student Age : "),
					"semail":input("Enter Student Email : "),
					"smobile":input("Enter Student Mob. : ")
			}
			input(str(temp_dic))
			with open("db/"+self.name+"_Track.csv",'a') as tra_file :
				tra_writer = csv.DictWriter(tra_file,fieldnames=dict_header)
				tra_writer.writerow(temp_dic)
				input("copied to the db [Press enter to continue ]")
		
		
			s1 = Student(**temp_dic)
			self.students.append(s1) 

		else :
			#comes from file with sid 
			# sid = self.st_count
			# input(sid)

			s1 = Student(sid=sid,**kwargs)

			self.st_count +=  1
			self.students.append(s1) 

		# input("append to list ")

	def edit_student(self,sid):
		print("Edit Student of ",self.name,"with id= ",str(sid))
		for i in self.students:
			if int(i.id) == int(sid) :
				# print(i.name)
				i.name = input("Current Name: "+i.name+"  -> Enter new name : ")
				i.age = input("Current Age: "+str(i.age)+"  -> Enter new age : ")
				i.email = input("Current Email: "+i.email+"  -> Enter new email : ")
				i.mobile = input("Current Mob.: "+str(i.monbile)+"  -> Enter new monbile : ")
				print("Done Editing")
				return 1

		input("Not found [Press enter to exit ]")
		return 0

	def remove_student(self,sid):
		print("Remove Student of ",self.name," with id = ",str(sid))
		# print(int(sid))
		for i in self.students:
			# print(sid,i.id,i.name)
			if int(i.id) == int(sid) :
				# print(i.name)
				self.students.remove(i)
				self.st_count -= 1 
				print("Done Removing")
				return 1

		input("Not found [Press enter to exit]")
		return 0
	
	# @classmethod
	def recursive_update_file(self):
		with open(self.name+"_Track.csv",'w+') as tra_file:
			txt_writer = csv.DictWriter(tra_file,fieldnames=dict_header)
			txt_writer.writeheader()
			for st in self.students :
				# print(st.name)
				temp_dic = {
						"sid":st.id ,
						"sname":st.name,
						"sage":st.age,
						"semail":st.email,
						"smobile":st.mobile
				}
				input(temp_dic)	
				txt_writer.writerow(temp_dic)

	def display_student(self,st_obj):
		print("ID: ",st_obj.id,end="")
		print(" , NAME: ",st_obj.name,end="")
		print(" , AGE: ",st_obj.age,end="")
		print(" , EMAIL: ",st_obj.email,end="")
		print(" , MOB: ",st_obj.mobile,end="")
		print("\n",end="")

	def view_student(self,sid):
		print("View Student of ",self.name,"with id= ",str(sid))
		for i in self.students:
			if i.id == sid :
				# print(i.name)
				self.display_student(i)
				input("Done Viewing [PPress enter to exit]")
				return 1

		input("Not found [Press enter to exit]")
		return 0

	def view_all(self):
		print("View all students of ",self.name,"no. = ",self.st_count)
		for st in self.students:
			self.display_student(st)
		input("Done listing , [Pres any key to exit]")

	@classmethod 
	def create_track(cls,ttname):
		print("Creating Track : ",ttname )
		# create new obj of track 
		for t in cls.track_list:
			# print(t.name," :::: " ,ttname)
			if t.name == ttname :
				input("Track is already exist !! [Press enter to continue ]")
				cls.selected_track = t
				return t
		# print(ttname,"not exist and will create it now")
		tt = cls(ttname) 
		#append to list of tracks objects 
		cls.track_list.append(tt)
		#edit menu obj if new one added to the list 
		cls.track_list_obj.edit([t.name for t in cls.track_list])
		cls.track_count += 1
		cls.selected_track = tt 

		try :
			# check file is exist 
			x = open("db/"+ttname+"_Track.csv",'r')
			x.close()
		except:
			# create new file if not exist 
			n = open("db/"+ttname+"_Track.csv",'a')
			writer = csv.DictWriter(n, fieldnames=dict_header)
			writer.writeheader()
			n.close()
		return tt

	@classmethod 
	def select_track(cls,ttname):
		if ttname.isdigit() : 
			ttname = int(ttname)
			if ttname <= len(cls.track_list):
				i = cls.track_list[ttname-1]
				ttname = cls.track_list[ttname-1].name
			else :
				input("Out of range [Press enter to exit]")
				return 0 
		else :
			for i in cls.track_list :
				if i.name == ttname : 
					break 
			else :
				input("Not found [Press enter to exit]")
				return 0

		cls.selected_track = i 
		# input("Select Track method is : "+ttname+" with no. students = "+str(i.st_count))
		return cls.selected_track

	@classmethod 
	def delete_track(cls,ttname):
		if ttname.isdigit() : 
			ttname = int(ttname)
			if ttname <= len(cls.track_list):
				i = cls.track_list[ttname-1]
			else :
				return 0 
		else :
			for i in cls.track_list :
				if i.name == ttname : 
					break 
			else :  
				input("Not found [PPress enter to exit]")
				return 0

		if input("Are you sure to delete "+str(i.name) +" Track which has no. students = "+str(i.st_count)+" [Y/N] : ") == "Y" :
			cls.track_list.remove(i) 
			cls.track_list_obj.edit([t.name for t in cls.track_list])
			os.remove("db/"+i.name+"_Track.csv")
			cls.track_count -= 1
			input("Deleting Track "+i.name+" is Done [Press enter to continue ]")
			return 1
		else :
			return 0

	@classmethod 
	def get_tracks_from_files(cls):
		print("Get tracks list from directory : db")
		dir_list = os.listdir("db")
		for file_name in dir_list :
			if re.match("^[\w\d _]*_Track.csv$",file_name) != None :
				file_name = file_name.replace("_Track.csv","")
				print("trackfilename : ",file_name)
				temp_track_obj = cls.create_track(file_name)

	@classmethod 
	def get_students_from_tracks_files(cls):
		for track_ in cls.track_list :
			print("get students from ",track_.name,"csv Files")
			try : 
				with open("db/"+track_.name+"_Track.csv",'r') as tr_file :
					txt_reader = csv.DictReader(tr_file)
					for line in txt_reader :
						st1 = dict(line)
						# input(st1)
						track_.add_student(**st1)
						
			except Exception as e :
				input("Exception in track file reading : "+track_.name+str(e)+" [Press enter to exit]")

class Student:

	def __init__(self,sid,sname="",sage=0,semail="",smobile=0):
		self.id = sid
		# if sname == "" : sname = input("Enter Student Name : ")
		self.name = sname 
		# if sage == 0 : sage = input("Enter Student Age : ")
		self.age = sage
		# if semail == "" : semail = input("Enter Student Email : ")
		self.email = semail
		# if smobile == 0 : smobile = input("Enter Student Mob. : ")
		self.mobile = smobile

""" MAIN  """
def clear_screen():os.system('clear')

def main():
	
	Track.get_tracks_from_files()
	Track.get_students_from_tracks_files()

	# mech_track  = Track.create_track("mech40")
	# st1 = {"sname":"eslam","sage":13,"semail":"esla","smobile":101}
	# mech_track.add_student(**st1)
	# print("no of students :"+str(mech_track.st_count))

	# st1 = {"sname":"mo","sage":43,"semail":"asda","smobile":999}
	# mech_track.add_student(**st1)
	# print("no of students :"+str(mech_track.st_count))
	# # print(help(mech_track))
	
	# mech_track.view_all()

	# mech_track.remove_student(2)
	# mech_track.view_all()
	# st1 = {"sname":"gohar","sage":90,"semail":"ooo","smobile":902}

	# mech_track.add_student(**st1)
	# mech_track.view_all()
	
	# mech_track.view_student(2)
	# print("no of students :"+str(mech_track.st_count))
	# # mech_track.edit_student(2)
	# # mech_track.view_all()

	# print("total track number = ",Track.track_count)

	# embedd_track = Track.create_track("Emb")
	# embedd_track.add_student(**st1)
	# embedd_track.view_all()
	# print("emeb track counter  ",embedd_track.st_count)

	# print("total track number = ",Track.track_count)

	# Track.select_track("Emb")
	# print("Selected Track :",Track.selected_track.name)

	####################################################
	####################### STARTING ###################
	####################################################

	main_menu_list = ["Create Track","Select Track","Delete Track"]
	main_menu_obj = MENU(main_menu_list)
	student_menu_list = ["ADD Student","Edit Student","Remove Student","View Student","View All"]
	student_menu_obj = MENU(student_menu_list)

	while True :
		clear_screen()
		print("Main Menu : ")
		main_menu_obj.draw()
		main_menu_ret = main_menu_obj.get()
	

		clear_screen()

		if main_menu_ret == 1 or main_menu_ret == main_menu_list[0]:
			x = input("Enter Track Name to create : ")
			Track.create_track(x)
		elif main_menu_ret == 2 or main_menu_ret == main_menu_list[1]: 
			pass
		elif main_menu_ret == 3 or main_menu_ret == main_menu_list[2]:
			while True :
				clear_screen()
				print("Delete Track Menu : ")
				Track.track_list_obj.draw()
				# x = input("Enter Track Name ")
				x = Track.track_list_obj.get()
				# try : 
				if x == 0 : break 
				# except :
				# 	continue

				Track.delete_track(str(x))
				
		elif main_menu_ret == 0 :
			break 
		else :
			print("out of index")

		

		if main_menu_ret == 2  :
			while True : 
				clear_screen()
				print("Select Track Menu : ")
				Track.track_list_obj.draw()
				x = Track.track_list_obj.get()
				# print(x)
				try : 
					if x == 0 : break
				except :
					pass

				if Track.select_track(str(x)) != 0 :
					while True :
						clear_screen()
						print("--> Selected Track is :  ",Track.selected_track.name," No. of students : ",str(Track.selected_track.st_count))						
						student_menu_obj.draw()
						student_menu_ret = student_menu_obj.get()
						
						# student_menu_ret = int(student_menu_ret)
						
						if student_menu_ret == 1 or student_menu_ret == student_menu_list[0] :
							Track.selected_track.add_student()
						elif student_menu_ret == 2  or student_menu_ret == student_menu_list[1]:
							no = input("Enter student id : ")
							if no.isdigit() == False  : continue 
							Track.selected_track.edit_student(int(no))
							Track.selected_track.recursive_update_file()
						elif student_menu_ret == 3  or student_menu_ret == student_menu_list[2]: 
							no = input("Enter student id : ")
							if no.isdigit() == False  : continue 
							Track.selected_track.remove_student(int(no))
							Track.selected_track.recursive_update_file()
						elif student_menu_ret == 4  or student_menu_ret == student_menu_list[3]:
							no = input("Enter student id : ")
							if no.isdigit() == False  : continue 
							Track.selected_track.view_student(int(no))
						elif student_menu_ret == 5  or student_menu_ret == student_menu_list[4]:
							clear_screen()
							Track.selected_track.view_all()
						elif student_menu_ret == 0 :
							break 
						else :
							print("out of index")

if __name__ == "__main__":
	main()
