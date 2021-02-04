import os
from art import *
from colored import bg, fg, attr
import time
import FossaLang
os.system('clear')

func = FossaLang.Functions()

class Descriptions:
	show = '''
		Takes one needed input which can be any datatype. Outputs the parameter into the shell.

		Takes 4 optional inputs:
		time: how long to show the text before clearing it


		size:
		style:
		font: 


	'''

class Built_In_Functions:
	def show(text, show_time=None):
		print(text)
		try:
			time.sleep(show_time)
			os.system('clear')
		except:
			pass



func.func('show', 1, 4, Descriptions.show, Built_In_Functions.show)
os.system('clear')
Built_In_Functions.show('text')

line = 1
while True:
	command = input('>>> ')

	if 'func' == command[:5] and '!' in command:
		#Assuming that the the command is a function:
		#EXAMPLE FUNCTION: func funcname : parameter1, parameter2, parameter3
		command = command[4:]
		print(command)
		basic_func_parts = command.split('!')
		func_info = func.find_func(basic_func_parts[0])
		if func_info == False:
			print(bg('red') + 'Line ' + str(line) + ':\nfunction not found' + attr('reset'))
			break


	line += 1

