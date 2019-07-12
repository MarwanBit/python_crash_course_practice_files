import ast


list_1 = [
			{'Job Function':{"Total views" : 3595.0}},
			{'Seniority':{"Total views" : 3515.0}},
			{'Industry':{"Total views" : 3232.0}},
			{'Company Size':{"Total views" : 2944.0}},
			{'Location':{"Total views" : 2824.0}}
		]

sorted(list_1,key=lambda i:list(list(i.values())[0].values()),reverse=True)

for i in list_1:
	print('\n' + str(i))