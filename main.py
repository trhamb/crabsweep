from fetcher import fetch_episode
from parser import grab_transcript, split_transcript, turn_to_string
from gpt import decipher_questions
from prompt import PROMPT_TEMPLATE


def main():
    for i in range(1, 20):
        print("Working...")
        payload = turn_to_string(split_transcript(grab_transcript(fetch_episode(i))))

        prompt = PROMPT_TEMPLATE.replace("{transcript_text}", payload).replace(
            "{episode_number}", f"{i}"
        )

        raw_output = decipher_questions(prompt)

        with open(f"episode_output/{i}.json", "w", encoding="utf-8") as f:
            f.write(raw_output)

        print(f"Episode {i} scraped.")


if __name__ == "__main__":
    main()
