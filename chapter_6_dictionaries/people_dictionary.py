people_dictionary ={
	"Albert Einstein" : {
		"Occupation" : "Scientist",
		"Nationality" : "German",
		"Accomplishments" : ["Theory of Relativity",
		"Nobel Prize"]
	},
	"Lupe Fiasco" : {
		"Occupation" : "Rapper",
		"Nationality" : "American",
		"Accomplishments" : ["Greatest Rapper", "Lyricist"]
	}
}

print(people_dictionary["Lupe Fiasco"]["Accomplishments"][1])

for k in people_dictionary.keys():
	print(k)

for v in people_dictionary.values():
	print(v)
