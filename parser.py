from bs4 import BeautifulSoup


def grab_transcript(page):
    soup = BeautifulSoup(page, "lxml")
    attributes = {"class": "transcript-data"}
    transcript = soup.find("div", attributes)

    if transcript is None:
        return None
    else:
        return transcript


def split_transcript(t):
    output = []
    quotes = t.find_all("q")
    for q in quotes:
        output.append(q.get_text())
    return output


def turn_to_string(t):
    return "\n".join(t)
