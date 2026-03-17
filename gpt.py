from openai import OpenAI
from fetcher import fetch_episode
from parser import grab_transcript, split_transcript, turn_to_string


# Submit it over to ChatGPT with the prompt.
def decipher_questions(prompt):
    client = OpenAI()
    response = client.responses.create(model="gpt-5.4", input=prompt)
    return response.output_text


# raw_output = decipher_questions(prompt)

# with open("episode_output/episode-001.json", "w", encoding="utf-8") as f:
#     f.write(raw_output)
