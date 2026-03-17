from openai import OpenAI


# Submit it over to ChatGPT with the prompt.
def decipher_questions(prompt):
    client = OpenAI()
    response = client.responses.create(model="gpt-5.4", input=prompt)
    return response.output_text
