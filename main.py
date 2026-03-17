from fetcher import fetch_episode
from parser import grab_transcript, split_transcript, turn_to_string
from gpt import decipher_questions

# Get the transcript
payload = turn_to_string(split_transcript(grab_transcript(fetch_episode(1))))
