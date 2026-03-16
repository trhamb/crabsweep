from bs4 import BeautifulSoup
from fetcher import fetch_episode

page_data = fetch_episode(1)

def grab_transcript(page):
	# Run HTML through BeautifulSoup and grab
	# the transcript-data div contents.
	soup = BeautifulSoup(page, "lxml")
	attributes = {"class": "transcript-data"}
	transcript = soup.find("div", attributes)
	return transcript

def split_transcript(t):
	output = []
	quotes = t.find_all("q")
	for q in quotes:
		output.append(q.get_text())
	return output

for line in split_transcript(grab_transcript(page_data)):
	print(line)
