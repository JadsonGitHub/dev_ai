from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

""" codigo doc oficial:

response = client.responses.create(
    model="gpt-5-nano",
    input="Write a one-sentence bedtime story about a unicorn."
)
print(response.output_text)"""

completion = client.chat.completions.create(
    model="gpt-5-nano",
    max_tokens=200,
    temperature=0.5,
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {
            "role": "user",
            "content": "White a haiku about recursion in programming",
        },
    ],
)

print(completion.choices[0].message)
print(completion.choices[0].message.content)
