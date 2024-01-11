import turtle
import pandas as pd

scrn = turtle.Screen()
scrn.title('Us States Qu8z')
img = './UsStates.gif'
turtle.addshape(img)
turtle.shape(img)

t = turtle.Turtle()
t.hideturtle()
t.penup()
#
#with open('./UsStates.csv') as f:
#	listOfS = f.readlines()

#def update():
#	t.clear()
#	t.write(f'{listOfS[1]}',False,'center',('Courier',13,'normal'))

#def l9g(x,y):
#	with open('./cor.txt','a') as cor:
#		cor.write(f"{listOfS.pop(1).strip()},{x},{y}\n")
#		update();
#update()
#scrn.onscreenclick(l9g)


data = pd.read_csv('./DATA.CSV')
#stat = data.state.to_list()
#cor = [data.x.to_list(),data.y.to_list()]
tmp0 = None
ttle = 'U.S. States'
corrects = []

while len(corrects) <= 50:
	state = scrn.textinput(ttle,'What is another state name?: '.title())
	if state == 'Exit': break
	tmp0 = data[data.state == state]
	if len(tmp0) != 0 and state not in corrects:
		t.goto((float(tmp0.x),float(tmp0.y)))
		t.write(state,False,'center',('Courier',10,'normal'))
		corrects.append(state)
	ttle = (f'{len(corrects)} of 50 states correct')

#missed = data.state.to_list()
#for c in corrects:
	#missed.remove(c)
missed=[stt for stt in data.state.to_list() if stt not in corrects]
pd.DataFrame(missed).to_csv('missed.csv')
