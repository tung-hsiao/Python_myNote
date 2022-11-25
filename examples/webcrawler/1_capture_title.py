
# refer to 
# https://www.youtube.com/watch?v=9Z9xKWfNo7k
# self-learning purpose only

import urllib.request as req
url = "https://www.ptt.cc/bbs/movie/index.html"

# build a request object with Request Headers info
request = req.Request(url, header={
	"User-Agent" : "xxxxxxxxxxxxxxx capture from the user's web browser xxxxxxxxxxxxxxx"
	})

with req.urlopen(request) as response:
	data = response.read().decode("utf-8")

# parse html raw data
import bs4
root = bs4.BeautifulSoup(data, "html.parser")

# print(root.title.string)

# titles = root.find("div", class_="title")  # search div flag with class="title"
# print(titles.a.string)

titles = root.find_all("div", class_="title")  # search all the div flag with class="title"
#print(titles)
for title in titles:
	if titles.a != None:        # if flag don't contain a, (deleted), print the title
		print(title.a.string)