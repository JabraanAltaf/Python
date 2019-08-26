from bs4 import BeautifulSoup
import requests

# webpage to be scraped
url = "https://www.imdb.com/search/title/?groups=top_250&sort=user_rating"
response = requests.get(url)

# Beautiful Soup takes params -> response as text and parser type
soup = BeautifulSoup(response.text)

# Selecting the HTML values needed
movies = soup.select('.lister-item-header')
ratings = soup.select('.ratings-bar strong')

# variable for index of ratings for a movie
index = 0

# Printing out the top 50 movies including it's IMDB rating
for movie in movies:
     print(movie.select_one('.lister-item-index').getText() + movie.find('a').getText())
     print("Rating: " + ratings[index].getText())
     index += 1
