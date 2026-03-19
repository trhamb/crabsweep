from fetcher import fetch_episode
from parser import grab_transcript, split_transcript, turn_to_string
from gpt import decipher_questions
from prompt import PROMPT_TEMPLATE
import datetime as dt
import os

def get_time():
    return dt.now().strftime("%Y-%m-%d %H:%M:%S")

def starting_episode():
    starting_episode = 1
    files = os.listdir("./episode_output")
    saved_numbers = set()
    for file in files:
        if file.endswith(".json"):
            stripped = file.replace(".json", "")

            try:
                number = int(stripped)
                saved_numbers.add(number)
            except ValueError:
                pass

    if not saved_numbers:
        return starting_episode
    else:
        starting_episode = max(saved_numbers) + 1

    return starting_episode


start = starting_episode()


def main():
    loop_start = start
    log_file = open("log.txt", "a", encoding="utf-8")

    while True:
        print("Working...")
        log_file.write(f"[{get_time()}] Working...")

        ep_ts = grab_transcript(fetch_episode(loop_start))

        if ep_ts is None:
            break

        payload = turn_to_string(split_transcript(ep_ts))

        prompt = PROMPT_TEMPLATE.replace("{transcript_text}", payload).replace(
            "{episode_number}", f"{loop_start}"
        )

        raw_output = decipher_questions(prompt)

        with open(f"episode_output/{loop_start}.json", "w", encoding="utf-8") as f:
            f.write(raw_output)

        print(f"Episode {loop_start} scraped")
        log_file.write(f"[{get_time()}] Episode {loop_start} scraped.")
        log_file.close()

        loop_start += 1


if __name__ == "__main__":
    main()
