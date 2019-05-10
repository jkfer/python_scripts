#!/usr/bin/python

# Sample script model to scrape data from webpage and insert into MySQL DB
# Planning for other project
# movies db and the table 'top_100' is already defined in the backend
# add - error handling 


import requests
import bs4
import MySQLdb


# URL for page of top movies sorted  by ratings
URL_2018 = 'https://www.imdb.com/list/ls058813655/?sort=user_rating,desc&st_dt=&mode=detail&page=1'


# get all HTML tags containing movie_info
r = requests.get(URL_2018)
s = bs4.BeautifulSoup(r.content, 'html.parser')


# filter only the div tag containing movie info
MOVIE_INFO = s.findAll('div', attrs={'class': 'lister-item-content'})


movie_in = []


# get movie info from the div tag 
def get_movInfo():
	for item in MOVIE_INFO:
		title = item.a.text
		ID = item.span.text.strip('.')

		for tag in item.findAll('div', attrs={'class': 'ipl-rating-star small'}):
			rating = tag.findAll('span', attrs={'class': 'ipl-rating-star__rating'})[0].text 
	
		plot_sum = item.find('p', attrs={'class': ''}).text.strip()
		movie_in.append([ID, title, rating, plot_sum])



# insert info into DB
def insert_to_DB():
	src = MySQLdb.connect(user='root', passwd='123456', host='mysql', db='movies')
	c = src.cursor()
	
	query = "INSERT INTO top_100 (id, name, rating, plot_summary) VALUES ('%s', '%s', '%s', '%s');"

	for detail in movie_in:
		ID = detail[0]
		title = detail[1]
		rating = detail[2]
		plot_sum = detail[3]


		# handling of special charachters inmovie title and plot summary
		new_title = str(MySQLdb.escape_string(title))
		new_plot_sum = str(MySQLdb.escape_string(plot_sum))
	
		print(query % (ID, new_title, rating, new_plot_sum))
		c.execute(query % (ID, new_title, rating, new_plot_sum))

	
	src.commit()
	c.close()
	src.close()                                                                



if __name__ == '__main__':
	get_movInfo()
	insert_to_DB()

