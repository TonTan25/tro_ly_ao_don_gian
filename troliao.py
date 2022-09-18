import pyttsx3
import speech_recognition
from datetime import datetime, date
from random2 import randint
from random import randint
from decimal import*
from fractions import *




robot_mouth = pyttsx3.init()
robot_brain = ""

print("Goodmorning MY Master")
robot_mouth.say("Goodmorning My Master")
robot_mouth.runAndWait()
print("press enter to exit, if you want close this program")
print("_________________________________________________")

while True:
	you = input("what do you want ? :")
	if "read" in you:
		print("Can I have read :")
		while True:
			text = input()
		
			if text == "esc":
				robot_mouth.say("esc")
				print("oke" + "\n" + "___________________")
				break
			else:
				print("___________________" + "\n")
				voices = robot_mouth.getProperty('voices')
				robot_mouth.setProperty('voice', voices[1].id)
				def speak(audio):
					robot_mouth.say(audio)
					robot_mouth.runAndWait()
				speak(str(text))
	elif "ask" in you:
		print("yes !!" + "\n" + "I do not mind " + "\n" + "Ask me your questions " + "\n" + " I'll answer")
		robot_mouth.say("yes !!" + "\n" + "I do not mind " + "\n" + "Ask me your questions " + "\n" + " I'll answer")
		robot_mouth.runAndWait()
		while True:

			you = input("input:")
			print("Robot : >>> loading")
			

			if you == "A":
				robot_brain = " Fuck you and what did you said "

			elif "good morning" in you:
				robot_brain = " Yes !!" + "\n" + "A good day for you"

			elif "tran duc bo" in you:
				robot_brain = "mèo méo meo meow"
				
			elif "good" in you:
				robot_brain = " thank you"
			elif you == "":
				robot_brain = "Hmm! Yeah !" + "\n" + "you want I kill you or fuck you"

			elif "hello" in you:
				robot_brain = "Hello KING of VRA city" + "\n" +"bla bla ... baka nomal"

			elif you == "hi":	
				robot_brain = randint(0,1)
				if robot_brain == 0:
					robot_brain = "Goodmorning and goodbye"
				else:
					robot_brain = "hi con cac"
			elif "fuck you"in you:
				robot_brain = " Yeah !!" + "\n" + "come here and fuck me now"
			elif "cut" in you:
				robot_brain = " c" + " o" +  " n" +  " c" +  " a" +  " c" + "\n" + "con cac"
			elif "today"in you:
				if "is" in you:
					today = date.today()
					robot_brain =today.strftime("%B %d, %Y")
				elif "do" in you:
					robot_brain = "Why you ask me"
			elif "sister" in you:
				if "older" in you:
					robot_brain = "A-ra A-ra , my brother"
				elif "young" in you:
					robot_brain = "Onii-chan, Baka, Hentai"
				else:
					robot_brain = "Do you want who I am?"

			elif "time" in you:
				now = datetime.now()
				robot_brain = now.strftime("%H hours %M minutes %S seconds")
			
			elif "how" and "exit" in you:
				robot_brain = "if you good bye me, I'll bye you and exit"
			elif "what" in you:
				if "animal" and "like" in you:
					robot_brain = "I like cat and puss in boots"
				elif "thing" and "love" in you:
					robot_brain = randint(0,1)
					if robot_brain == 0:
						robot_brain = " the pussy"
					elif robot_brain == 1:
						robot_brain = " the dick"
				elif "thing" and "hate" in you:
					robot_brain = "I don't hate anything" + "\n" + "because Everything has its own value "
			elif "pi" in you:
				robot_mouth.say("do you want know")
				
				if "100" in you:
					print("100 digits after the comma")
					robot_mouth.say("100 digits after the comma")
					robot_brain = "3,14159 26535 89793 23846 26433 83279 50288 41971 69399 37510 58209 74944 59230 78164 06286 20899 86280 34825 34211 70679"
				elif "10" in you:
					robot_brain = "3,14159 26535"
				else:
					robot_brain = "3,14"
			elif "money" in you:
				print("don't use '.' or ',' in the number. ")
				print("Transfer money from USD to VND / or / VND to USD")
				robot_mouth.say("Transfer money from USD to VND / or / VND to USD")
				robot_mouth.runAndWait()
				while True:
					print("your choice is : ")
					print("-----------------")
					you = input()
					# chuyển đổi tiền từ usd sang vnd.
					if "USD to" in you:
						print("input your money:")
						usd = input()
						vnd = int(usd) * 22300
						robot_brain = " VND = " + str(vnd) + " VND"
						print(" VND = " + str(vnd) + " VND")
						robot_mouth.say(robot_brain)
						robot_mouth.runAndWait()
					elif "VND to" in you:
						print("input your money:")
						vnd = input()
						usd = int(vnd) / 22300
						robot_brain = " USD = " + str(usd) + " $" 
						print(" USD = " + str(usd) + " $" )
						robot_mouth.say(robot_brain)
						robot_mouth.runAndWait()
					else:
						robot_brain = "I can't do it because I cannot"
						break

			elif "king" in you:
				if "your" in you:
					robot_brain = "you"
				elif "world" in you:
					robot_brain = "error" + "\n" +"I'm not omnipotent software" +"\n" + "can I do other thing for you?"
				else :
					robot_brain = "error" + "\n" +"hahahaha haha" + "\n" + "error"
					print(robot_brain)
					robot_mouth.say(robot_brain)
					robot_mouth.runAndWait()
					break
			elif "who" in you:
				if "I" in you:
					print("You are my Master")
					print("I'm your child")
					robot_mouth.say("You are my Master")
					robot_mouth.say("I'm your child")
					robot_mouth.runAndWait()
				
					while True:
						you = input()
						if "oke" in you:
							a = " I love you"
							print(a)
							robot_mouth.say(a)
							robot_mouth.runAndWait()
							break
						elif "get away" in you:
							b = "Okay " + "\n" + " I crying"
							print(b)
							robot_mouth.say(b)
							robot_mouth.runAndWait()
							break
						elif you == "fuck you":
							c = "FUCK YOU too"
							print(c)
							robot_mouth.say(c)
							robot_mouth.runAndWait()
							break
						elif you ==  ":3":
							break
						else :
							print("what do you want ?")
							robot_mouth.say("What do you want ?")
							robot_mouth.runAndWait()
				elif "you" in you :
					print("I am . . . " + "\n" + "\n" + "who am I?" + "\n" + "\n" + "\n" + "would you mind give me a name?")
					robot_mouth.say("I am . . . " + "\n" + "\n" + "who am I?" + "\n" + "\n" + "\n" + "would you mind give me a name?")
					robot_mouth.runAndWait()
					a = input()
					b = "sorry" + "\n" + " let's me introduce myself again " +"\n" + "I am " + str(a)
					print(str(b))
					voices = robot_mouth.getProperty('voices')
					robot_mouth.setProperty('voice', voices[1].id)
					def speak(audio):
						robot_mouth.say(audio)
						robot_mouth.runAndWait()
					speak(str(b))
				else:
					robot_brain = "Who's " + "\n" + "\n" + "\n" +"\n" +"\n" + "Who"

			if you == ["what the fuck" , "what", "WTF","what the hell"]:
				robot_brain == "its joke :)" + "\n" + "Do you think funny??"
			elif "Tuan Anh" in you :
				robot_brain = " he is a friend of Master"

			elif "Tan" in you :
				robot_brain = " he is my Master"
			elif "president"in you:
				if "america" in you:
					robot_brain = " America's president is Dumna Trump"

				elif "viet nam" in you:
					robot_brain = " Viet Nam don't have president"
					
				else :
					robot_brain = "seach in google " + "\n" + "I don't know" + "\n" + " don't ask me"

			elif you == ":3":
				robot_brain = "I am smiling too"
			elif you == ":)":
				print("Okay" + "\n" + "Do you want any thing more?")
				robot_mouth.say("Okay" + "\n" + "Do you want any thing more?")
				robot_mouth.runAndWait()
				you = input()
				if "no" in you:
					print("Hmmm" + "\n" + "Robot: >>> loading")
					robot_mouth.say("Hmmm" + "\n" + "Robot: >>> loading")
					robot_mouth.runAndWait()
					break
				else:
					robot_brain = "what's your question?"
			elif "thu tuong" in you :
				if "viet nam" in you:
					robot_brain = "Nguyen Phu Trong"
				else :
					robot_brain = "I don't know"
			elif "lol" in you:
				robot_brain = "Hmm " + "\n" + " >>> " + "\n" + " League of Legends"
			elif "bye" in you:
				robot_brain = "Bye Master"
				print("bye Master")
				voices = robot_mouth.getProperty('voices')
				robot_mouth.setProperty('voice', voices[1].id)
				def speak(audio):
					robot_mouth.say(audio)
					robot_mouth.runAndWait()
				speak(robot_brain)
				break

			elif "random" in you:
				 #gán giá trị cho robot_brain bằng 1 giá trị được random.
				if "from 0 to 100" in you:	
					robot_brain = randint(0,100)
					print("number is : " )
				elif "from 0 to 10" in you:
					robot_brain = randint(0,10)
					print("number is : " )
				elif "?" in you :
					robot_brain = "Go a Way" + "\n" + "error"
				else:
					print("input your number if you want to random")
					print("-------------------")
					print("a = "); a = input()
					print("b = "); b = input()
					robot_brain = randint(int(a),int(b))
			elif you == "     " :
				robot_brain = randint(0,5)
				if robot_brain == 0:
					robot_brain = " you are my king"
				elif robot_brain == 1:
					robot_brain = "you are my daddy"
				elif robot_brain == 2:
					robot_brain = "you are my bro"
				elif robot_brain == 3:
					robot_brain = "you are my Master"
				elif robot_brain == 4:
					robot_brain = "you are my mammy"
				else:
					robot_brain = " Hmm I don't understand, I don't have information in brain "	
			
			print(robot_brain)
			voices = robot_mouth.getProperty('voices')
			robot_mouth.setProperty('voice', voices[1].id)
			def speak(audio):
				robot_mouth.say(robot_brain)
				robot_mouth.runAndWait()
			speak(robot_brain)
	elif "li" in you:

		li = ['tran duc bo', 3, 'trung hai', 'quang trung','tran thi thanh tam',22,44,'Anh khong doi qua','trầm cmn cảm',]
		print(li)
		while True:
			print("--------------------")
			you = input("nhập yêu cầu của bạn :")
			if "del" in you:
				print("nhập vị trí cần xóa :")
				you = input()
				del li[int(you)]
			elif "add" in you:
				a = input("chọn vị trí trong list :")
				b = input("nhập cái bạn muốn nhập :")
				li.insert(int(a),str(b))
			elif you == "exit" :
				print("bye")
				print("_________________________________________________")
				robot_mouth.say("bye and I don't want see you again ")
				robot_mouth.runAndWait()
				break
			else:
				a = input("nhập tự do")
				li.append(a)


			print(li) 
	elif "u" and "m" in you:
		print("so" + "\n" + "How are you to day?")
		robot_mouth.say("so" + "\n" + "How are you to day?")
		robot_mouth.runAndWait()
		while True:
			you = input("input:")

			if "yes" in you:
				robot_brain = "Oh yeah !!" + "Good a happy for you, Master"
			elif "oke" in you:
				robot_brain = "Oh yeah !!" + "Good a happy for you, Master"
			elif "fine" in you:
				print("Oh yeah !!" + "Good a happy for you, Master")
				robot_mouth.say("Oh yeah !!" + "Good a happy for you, Master")
				robot_mouth.runAndWait()
				break
			elif "u" and "m" in you:
				print("Are you really OKE?")
				robot_mouth.say("Are you really OKE")
				robot_mouth.runAndWait()
				
				while True:
					you = input()
					if "no" in you:
						print("what's the cause made you sad ? ")
						robot_mouth.say("what's the cause made you sad ?")
						robot_mouth.runAndWait()
						break
					else :
						print("OKEY")
						robot_mouth.say("OKEY")
						robot_mouth.runAndWait()
						break
			elif "no" in you :
				print("you have to go to the doctor " + "\n" + " if you do not it, you'll meet dangerous")
				robot_mouth.say("you have to go to the doctor " + "\n" + " if you do not it, you'll meet dangerous")
				robot_mouth.runAndWait()
				break
			elif "exit" in you:
				if "how" in you:
				
					robot_brain = " you write 'exit' to exit for this"
				else:
					print("_________________________________________________")
					break

			else:
				robot_brain = "hum hum" + "\n" + "I don't care "
			

			print(robot_brain)
			robot_mouth.say(robot_brain)
			robot_mouth.runAndWait()	
			print("_________________________________________________")
			
	elif "how" and "exit" in you:
		print("you press enter to exit " + "\n" + "and press enter until exit completely")
		robot_mouth.say("you press enter to exit " + "and press enter until exit completely")
		robot_mouth.runAndWait()
	elif "speak" in you:
		print("I speak it, :")
		while True:
			robot_brain = input("O :")
			if robot_brain == "stop now" :
				print("oke")
				robot_mouth.say("OKEY")
				robot_mouth.runAndWait()
				break
			
			else:
				print(robot_brain)
				voices = robot_mouth.getProperty('voices')
				robot_mouth.setProperty('voice', voices[1].id)
				def speak(audio):
					robot_mouth.say(robot_brain)
					robot_mouth.runAndWait()
				speak(robot_brain)
				print("_________________________________________________")
	elif you == "/" :
		print("division (/) ")
		while True:
			you = input("______________:")
			if you == "stop":
				break	
			else: 	
				print(" nhập giá trị của a;b và thỏa mãn điều kiện a luôn phải bé hơn của b")
				a = input()
				b = input()

				print("--------------")
				print("a = " + str(a))
				print("b = " + str(b))
				print("--------------")
				print("RRRRRRRRRRRRRRRRRR"+ "\n" +"---------------------")
				robot_brain = randint(int(a),int(b))
				print(robot_brain)
				w = type(robot_brain)
				print(w)


				print("1 vài phần có liên quan :")
				print("nhập số chữ số được hiện thị sau dấu ',' :")
				d = input()
				getcontext().prec = int(d)
				q = Decimal(b)/Decimal(a)
				print(q)
				print(type(q))
				e = Fraction(int(b),int(a))
				print(e)
				print(type(e))
				print("------------------")
				c = complex(int(a),int(b))
				print(c)
				print(c.real)
				print(c.imag)
				print(type(c))
	else:
		print("this is the end")
		robot_mouth.say("this is the end")
		robot_mouth.runAndWait()
		print("_________________________________________________")
		break 