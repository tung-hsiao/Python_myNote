
# refer to 
# https://www.youtube.com/watch?v=9Z9xKWfNo7k
# self-learning purpose only

import urllib.request as req
url = "https://www.ptt.cc/bbs/Gossiping/index.html"

# build a request object with Request Headers info
request = req.Request(url, header={
	"cookie" : "over18=1"
	"User-Agent" : "xxxxxxxxxxxxxxx capture from the user's web browser xxxxxxxxxxxxxxx"
	})

with req.urlopen(request) as response:
	data = response.read().decode("utf-8")

# parse html raw data
import bs4
root = bs4.BeautifulSoup(data, "html.parser")
titles = root.find_all("div", class_="title")  # search all the div flag with class="title"
for title in titles:
	if titles.a != None:        # if flag don't contain a, (deleted), print the title
		print(title.a.string)