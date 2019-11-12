#! /usr/bin/env python3.6
import os 
import re
import csv 
###########################################
main_menu = ["1-Add Student","2-View All","3-View Student by ID","4-Delete Student by ID","5-Edit Student by ID"]
edit_menu = ["0-id","1-name","2-age","3-email","4-mobile","5-address"]
header_string = "ID     Name       age      email           mobile        address"
# Make a regular expression 
# for validating an Email 
email_regex = '\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+'
mob_regex = "01[0125][0-9]*"
students_list = []
dict_header = ["ID","name","age","email","mobile","address"]

###########################################
# student_dict1 = {
# 	"ID" : 1,
# 	"name":"eslam",
# 	"age":12,
# 	"email":"asd",
# 	"mobile":10,
# 	"address":"asdasd"
# }
# student_dict2 = {
# 	"ID" : 2,
# 	"name":"lasdm",
# 	"age":123,
# 	"email":"aljasd@",
# 	"mobile":9234,
# 	"address":"lkld"
# }
###########################################
# students_list.append(student_dict1)
# students_list.append(student_dict2)
counts = 0
###########################################
def clear_screen():os.system('clear')
###########################################
def draw_menu(i_list):
	for l in i_list:
		print(l)
###########################################
def get_menu(in_menu):
	x = input()
	if x.isdigit() :
		x = int(x) 
		if x >= 0 and x <= len(in_menu) :
			return x 
		else :
			input("Out of range , Press any key")
			return -1 
	else :
		input("Invalid Input , Press any key")
		return -1 



###########################################
def check_str(x):
	for i in x :
		if i.isdigit() and i != '':
			return  0
	return 1
###########################################
def check_email(x):      
	if(re.match(email_regex,x)) != None :
		return 1 
	else :
		return 0 

	# at_flag = 0
	# net_flag = 0
	# if x.rfind("@") >= 1:
	# 	at_flag = 1
	# if x.rfind(".net") >= 1 or x.rfind(".com") >= 1 :
	# 	net_flag = 1 
	# return at_flag and net_flag
###########################################
def check_num(x):
	for i in x :
		if not i.isdigit():
			return  0 
	return 1
###########################################
def check_mob(x):
	if 	re.match(mob_regex,str(x)) != None :
		return 1 
	else :
		return 0
	# if x[0:3] == '010' or  \
	#    x[0:3] == '011' or  \
	#    x[0:3] == '012' or  \
	#    x[0:3] == '015' and \
	#    len(x) >= 3 :
	# 		return 1 
	# else :
	# 	return 0
###########################################
def enter_name():
	while True:
		name = input("Enter student name :")
		if check_str(name) :
			print("Valid Name ")
			break
		else:
			print("Invalid Name ")
	return name 
###########################################
def enter_age():
	while True:
		age = input ("Enter student age :")
		if check_num(age) :
			if int(age) >= 0 and int(age) <= 150 :
				print("Valid age")
				break
			else :
				print("Invalid age")	
		else:
			print("Invalid age")
	return age 
###########################################
def enter_email():	
	while True:
		email = input ("Enter student email :")
		if check_email(email) :
			print("Valid email")
			break
		else:
			print("Invalid email")
	return email
###########################################
def enter_mobile():
	while True:
		mobile = input ("Enter student mobile :")
		if check_num(mobile) : 
			if check_mob(mobile):
				print("Valid mobile")
				break
			else:
				print("Invalid mobile number")
		else :
				print("Invalid  number")
	return mobile
###########################################
def enter_address():
	while True:		
		address = input ("Enter student address :")
		if check_str(address) :
			print("Valid address")
			break
		else:
			print("Invalid address")
	return address



###########################################
def add_student() :
	print("Add Student Informations :")
	print("student no. : ",counts)
	temp_dict = {
		"ID" 		: 	counts ,
		"name"		:	enter_name(),
		"age"		:	enter_age(),
		"email"		:	enter_email(),
		"mobile"	:	enter_mobile(),
		"address"	:	enter_address()
	}
	students_list.append(temp_dict)
	try :
		x = open("students.csv",'r')
		x.close()
	except:
		n = open("students.csv",'a')
		writer = csv.DictWriter(n, fieldnames=dict_header)
		writer.writeheader()
		n.close()

	with open("students.csv","a+") as f :
		writer = csv.DictWriter(f, fieldnames=dict_header)
		writer.writerow(temp_dict)

	# with open("students.txt",'a') as f :
	# 	in_str = [i for i in temp_dict.values()] 
	# 	f.write(str(in_str)+"\n")

###########################################
def view_student(dic,multi=0):
	if multi != 1 : print(header_string)
	print(\
		dic["ID"]	  ,"    ", \
		dic["name"]	  ,"    ",\
		dic["age"] 	  ,"    ",\
		dic["email"]  ,"         ",\
		dic["mobile"] ,"      ",\
		dic["address"])
###########################################



###########################################
##########################################
# def file_search_student_id(Id):
# 	my_dict = {}
# 	with open('students.csv', 'r') as csv_file:
# 		csv_reader = csv.DictReader(csv_file)
# 		for line in csv_reader:
# 			cu_id = dict(line.items())["ID"]
# 			if cu_id == Id:
# 				my_dict = dict(line.items())
# 				# print(my_dict)
# 				return my_dict
# 	return None 
###########################################
def file_search_student_key(key,Id):
	my_dict = {}
	try :
		with open('students.csv', 'r') as csv_file:
			csv_reader = csv.DictReader(csv_file)
			for line in csv_reader:
				# print(dict(line.items())[str(key)])
				cu_id = dict(line.items())[str(key)]
				if cu_id == str(Id):
					my_dict = dict(line.items())
					# print(my_dict)
					return my_dict
	except :
		print("Empty ..")
	return None 
###########################################
# def search_student_id(Id):
# 	for dicts in students_list :
# 		if dicts["ID"] == Id :
# 			return dicts 
# 			#view_student(dicts)
# 	else:
# 		return None
############################################
def search_student_key(key,val):
	for dicts in students_list :
		if dicts[key] == val :
			return dicts 
	else:
		return None
###########################################

###########################################
###############  V i e w ##################
###############   A l l  ##################
###########################################
def view_all_students():
	print(header_string)
	for dicts in students_list :
		view_student(dicts,1)
###########################################
def file_view_all_students():
	my_dict = {}
	print(header_string)
	try :
		with open('students.csv', 'r') as csv_file:
			csv_reader = csv.DictReader(csv_file)
			for line in csv_reader:
				my_dict = dict(line.items())
				view_student(my_dict,1)
	except :
		print("Empty .. ")
###########################################



###########################################
def display_student(key):
	x = input("Enter "+key+" : ")
	if key == "ID" or key == 'age' or key == 'mobile' :
		x = int(x)
	st = search_student_key(key,x)
	if st != None :
		view_student(st)
	else :
			print("Not found")
###########################################
def file_display_student(key):
	x = input("Enter "+key+" : ")
	if key == "ID" or key == 'age' or key == 'mobile' :
		x = int(x)
	st = file_search_student_key(key,x)
	if st != None :
		view_student(st)
	else :
			print("Not found")
###########################################


###########################################
def delete_student(key):
	x = input("Enter "+key+" : ")
	if key == "ID" or key == 'age' or key == 'mobile' :
		x = int(x)
	st = search_student_key(key,x)
	if st != None :
		students_list.remove(st)
	else :
		print("Not found")
###########################################
def file_delete_student(key):
	x = input("Enter "+key+" : ")

	I = "\d" 
	N = "\w"
	A = "\d"
	E = email_regex
	M = mob_regex 
	S = "\w"

	if key == "ID" :
		I = x 
	elif key == 'age' :
		A = x 
	elif key == 'mobile' :
		M = x
	elif key == 'name':
		N = x 
	elif key == 'address':
		S = x
	elif key == 'email':
		E = x 
	else :
		print("non key")
		return
		

	try :
		with open('students.csv', 'r') as csv_file:
			filedata = csv_file.read()
			se_str = '['+I+']+,['+N+']+,['+A+']+,'+E+','+M+',['+S+']+\n'
			input(se_str)
			if re.search(se_str,filedata) == None :
				input("out id")
				return 
			# input(filedata)
			filedata = re.sub(se_str,'',filedata)
			# input(filedata)
		with open('students.csv', 'w') as csv_file:
			csv_file.write(filedata)

	except Exception as e :
		print(e)
		input("Exception Error !!!")
		

###########################################
def edit_student(key):
	x = input("Enter "+key+" : ")
	if key == "ID" or key == 'age' or key == 'mobile' :
		x = int(x)
	st = search_student_key(key,x)
	if st == None :
		input("Not found")
		return 		
	
	clear_screen()
	while True :
		draw_menu(edit_menu)
		print()
		view_student(st)
		print("\nEnter no. of element to edit : ' Enter 0 to exit '")
		k = get_menu(edit_menu)
		
		if k == 1 :
			st["name"]    = enter_name()
		elif k == 2 :
			st["age"]     = enter_age()
		elif k == 3 :
			st["email"]   = enter_email() 
		elif k == 4 :
			st["mobile"]  = enter_mobile() 
		elif k == 5 :
			st["address"] = enter_address() 
		elif k == 0 :
			break 
		else :
			print("Invalid input")
		clear_screen()
##########################################
def file_edit_student(key):
	
	x = input("Enter "+key+" : ")

	I = "\d" 
	N = "\w"
	A = "\d"
	E = email_regex
	M = mob_regex 
	S = "\w"

	if key == "ID" :
		I = x 
	elif key == 'age' :
		A = x 
	elif key == 'mobile' :
		M = x
	elif key == 'name':
		N = x 
	elif key == 'address':
		S = x
	elif key == 'email':
		E = x 
	else :
		print("non key")
		return
		
	se_str = '['+I+']+,['+N+']+,['+A+']+,'+E+','+M+',['+S+']+\n'
	# input(se_str)
	try :
		with open('students.csv', 'r') as csv_file:
			filedata = csv_file.read()
			# input(filedata)
			clear_screen()
			if re.search(se_str,filedata) == None :
				input("out id delete func")
				return 
			
			# input("ok")
			
			while True :
				m = re.search(se_str,filedata)
				# input(m.group(0))
				li = list(str(m.group(0)).strip("\n").split(','))
				I = li[0]
				N = li[1]
				A = li[2]
				E = li[3]
				M = li[4]
				S = li[5]

				clear_screen()
				draw_menu(edit_menu)
				print("\nEnter no. of element to edit : ' Enter 0 to exit '")
				print()
				print(li)
				print()
				k = get_menu(edit_menu)
				
				if k == 1 :
					N    = enter_name()
				elif k == 2 :
					A     = enter_age()
				elif k == 3 :
					E  = enter_email() 
				elif k == 4 :
					M  = enter_mobile() 
				elif k == 5 :
					S = enter_address() 
				elif k == 0 :
					break 
				else :
					input("Invalid input")
					# clear_screen()
					continue 
				
		ch_str = I+','+N+','+A+','+E+','+M+','+S+'\n'
		filedata = re.sub(se_str,ch_str,filedata)
		input(filedata)
		with open("students.csv",'w') as f :
			cs_f = csv.write(filedata)
	
	except :
		print("Error in file , Delete func")

	
###########################################
def grapping():
	my_dict = {}
	try :
		with open('students.csv', 'r') as csv_file:
			csv_reader = csv.DictReader(csv_file)
			for line in csv_reader:
				my_dict = dict(line.items())
				students_list.append(my_dict)
				global counts 
				counts +=  1 
				
	except Exception as e :
		print(e)
		input("Empty .. ")
###########################################


grapping()
clear_screen()
k = 0 

while True:
	draw_menu(main_menu)
	print("\nEnter no. : ' Enter 0 to exit this main_menu '")
	k = get_menu(main_menu)
	clear_screen()
	
	if k == 3 or k == 4 or k == 5 :
		draw_menu(edit_menu)
		print("\nEnter type of searching : '9 for exit'")
		s = get_menu(edit_menu)
		clear_screen()
		search_key = dict_header[s] 
		# print(search_key)

	if k == 1 :
		
		counts += 1 
		add_student()

	elif k == 2 :
		file_view_all_students()
		input("press any key to exit")
	
	elif k == 3 :
		file_display_student(search_key)
		input("press any key to exit")

	elif k == 4 :
		file_delete_student(search_key)
		counts -= 1 

	elif k == 5 :
		file_edit_student(search_key)

	elif k == 0 :
		clear_screen()
		break

	else :
		continue 
	clear_screen()


# f.close()