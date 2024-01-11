import pandas as pd
data = pd.read_csv('./DATA.CSV')

while True:
	state = input('some state: \t').lower()
	#state = scrn.textinput('U.S. States','What is another state name?: ').lower()
	if state in ( v.lower() for v in data.state.to_list()):
		#if state in (i.lower() for i in data):
		print(state.title())
		print([data.x.to_list()],data.y.to_list())
		print([v.lower() for v in data.state.to_list()].index(state))
		#break;