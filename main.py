#pylint:disable=E1125
import pandas

#day_data = []
#with open('./day-Weather.csv') as data:
#	day_data = data.readlines()

#with open('./day-Weather.csv') as data:
#	day_data = csv.reader(data)
#	temp = []
#	for d in day_data:
#		if d[1] != 'temp':
#			temp.append(int(d[1]))
#	print(temp)

day_data=pandas.read_csv('./day-Weather.csv')

#print(day_data['temp'])
#print(day_data)

#print(f"Temperature average {round(sum(day_data['temp'].to_list())/len(day_data['temp']))}")

#print(f"max {day_data['temp'].max()}, {day_data['temp'].cummax()}")

#print(f"{day_data[day_data.temp == day_data['temp'].max()]}")

print(f"the mondays temp is {(int(day_data[day_data.day == 'Monday '].temp) * 1.8) + 32} F")

#create new data feame from dict and lists amd ssve it as csv files