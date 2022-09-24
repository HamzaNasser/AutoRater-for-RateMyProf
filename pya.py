
import webbrowser
import pyautogui as py
import time
import random
import pyperclip
user = input("Enter the porf ID: ").strip()
webbrowser.open('https://www.ratemyprofessors.com/ShowRatings.jsp?tid='+user) #(the id for the prof) 
time.sleep(4)
py.click(949,696)

def ratemyprofessors():



	rev0 = ["!!", "!", ".", ".....!", '!!!!!!!','_','?',',',"!!!!!", "...!"] #to be added randomly to the comment sectino wiht the list below to pass the repatitve comment 

	rev = ["good prof", "great", "...", "and so on"] #comments to be added
	time.sleep(2)


	time.sleep(3)

	py.click(949,696)

	
	time.sleep(random.randint(1,4))

	py.click(314, 775)

	time.sleep(random.randint(1,4))

	py.click(552, 821)

	

	py.typewrite(courses[random.randint(0,len(courses)-1)]) # Typing a random course name from the list
	time.sleep(random.randint(1,4))

	py.click(798, 830)

	for i in range(5):
		py.click(1907, 1020) # Scrolling down 


	time.sleep(random.randint(1,4))

	py.click(525, 403)

	py.click(855, 504)

	py.click(885, 597)

	py.click(748, 693)

	py.click(725, 796)
	time.sleep(random.randint(1,4))

	for i in range(10):
		py.click(1907, 1020) #scrlling



	time.sleep(random.randint(1,4))
	py.click(421, 441)

	newrev = rev[random.randint(0,len(rev)-1)] + (rev0[random.randint(0,len(rev0)-1)])

	py.typewrite(newrev)
	time.sleep(random.randint(1,4))



	for i in range(5):
		py.click(1907, 1020)

	time.sleep(random.randint(1,4))

	py.click(596, 469)
	time.sleep(1)

	py.click(383, 612)
	time.sleep(1)
	py.click(520, 709)


	time.sleep(random.randint(1,4))

	py.click(244,621)

	time.sleep(random.randint(1,4))

	py.click(330,426)
	time.sleep(random.randint(1,4))

	py.write("..Prof name ...", interval=0.5) # typing the prof name 

	time.sleep(2)

	py.click(293, 483)

	time.sleep(10)



def newMail():
	time.sleep(2)
	webbrowser.open('https://www.mohmal.com/en') # temp email website to make a quick random email after a few ratings
	time.sleep(1)
	py.click(900,516) # click on a random eamil button
	time.sleep(1)
	py.click(941,223) # copy the email
	time.sleep(1)
	

	py.click(193,17) # back to old tab 

	py.click(744,683) #email

	py.hotkey('ctrl','a')
	py.hotkey('ctrl', 'v')


	py.click(660,800) #Confemail

	py.hotkey('ctrl', 'v')
	time.sleep(1)


	for i in range(6):
		time.sleep(0.15)
		py.click(1907, 1020)

	py.click(550, 196) # pass

	py.typewrite("qweQ1995") # Entring creds

	time.sleep(1)


	py.click(621,344)

	py.typewrite("qweQ1995")

	py.click(510,448) #fname
	time.sleep(1)

	py.typewrite("AewfBC")
	time.sleep(1)

	py.click(500,552)

	time.sleep(1)

	py.typewrite("CBadfA")


	for i in range(5):

		py.click(1907, 1020)

	time.sleep(1)



	py.click(548,217) #agree
	time.sleep(1)


	py.click(484,332) # agree
	time.sleep(1)


	py.click(710, 605) # singuup
	time.sleep(1)

	py.click(526,19) #back to email
	time.sleep(1)
	py.click(949,431) #Refresh the page
	time.sleep(5)
	py.click(564,544) #conf email
	time.sleep(3)


	py.click(729,833) #clicking on the link
	time.sleep(1)
	py.click(932,19) #exit the tap


	py.click(635,19)
	time.sleep(1)

	py.click(255,605) #login email
	time.sleep(2)
	py.hotkey('ctrl', 'v')

	time.sleep(1)
	py.click(360,700) #pwd
	py.typewrite("qweQ1995")

	time.sleep(2)


	py.click(303,781) #login
	time.sleep(1)







def signOutAndUp():

	py.click(1673,129) # profile

	time.sleep(1)

	py.click(1573,366) # logout

	time.sleep(1)

	py.click(1889,366)

	time.sleep(1)

	py.click(1830,118) # profile
	time.sleep(2)


count = 0
while count < 100:
	ratemyprofessors()
	print(count)
	count=+1


