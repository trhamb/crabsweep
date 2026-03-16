import requests

def fetch_episode(ep_num):

	headers = {
		'User-Agent': 'Mozilla/5.0'
	}

	url = f"https://lateralcast.com/episodes/{ep_num}"
	r = requests.get(url, headers=headers)
	return r.text
