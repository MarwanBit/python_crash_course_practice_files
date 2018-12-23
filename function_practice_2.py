#This function returns a city and the country it's located in
def city_country(city, country):
	''' Here concetation is used to combine the strings,
		then the value of the combined strings is returned
		to the function call which can then be printed later'''
	city_country_pair = str(city) + ", " + str(country)
	return city_country_pair


#This function creates detailed information about an Album
def album(album_name, artist_name, track_list = []):
	if track_list:
		album_name = {
					"album name" : album_name,
					"artist name" : artist_name,
					"tracklist" : str(track_list),
					}
	else:
		album_name = {
					"album name" : album_name,
					"artist name" : artist_name,
					}
	
	return album_name
	

	



