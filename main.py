from fetcher import fetch_episode
from parser import grab_transcript, split_transcript, turn_to_string
from gpt import decipher_questions
from prompt import PROMPT_TEMPLATE
import os


def check_existing():
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

    return saved_numbers


def main():
    while True:
        print("Working...")
        next_episode = max(check_existing()) + 1
        ep_ts = grab_transcript(fetch_episode(next_episode))

        if ep_ts is None:
            break

        payload = turn_to_string(split_transcript(ep_ts))

        prompt = PROMPT_TEMPLATE.replace("{transcript_text}", payload).replace(
            "{episode_number}", f"{next_episode}"
        )

        raw_output = decipher_questions(prompt)

        with open(f"episode_output/{i}.json", "w", encoding="utf-8") as f:
            f.write(raw_output)

        print(f"Episode {next_episode} scraped")


# def main():
#     for i in range(20, 81):
#         print("Working...")
#         payload = turn_to_string(split_transcript(grab_transcript(fetch_episode(i))))

#         prompt = PROMPT_TEMPLATE.replace("{transcript_text}", payload).replace(
#             "{episode_number}", f"{i}"
#         )

#         raw_output = decipher_questions(prompt)

#         with open(f"episode_output/{i}.json", "w", encoding="utf-8") as f:
#             f.write(raw_output)

#         print(f"Episode {i} scraped.")


# if __name__ == "__main__":
#     main()
