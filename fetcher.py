import requests

def fetch_url(ep_num):

	headers = {
		'User-Agent': 'Mozilla/5.0'
	}

	url = f"https://lateralcast.com/episodes/{ep_num}"

	r = requests.get(url, headers=headers)

	print(f"Response status: {r.status_code}")
	print(r.text)


fetch_url(1)

