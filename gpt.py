from openai import OpenAI

client = OpenAI()

response = client.responses.create(
	model="gpt-5.4",
	input="Respond to this prompt so I can see it works!"
)

print(response.output_text)