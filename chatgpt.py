key = "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"
from openai import OpenAI
client = OpenAI(api_key=key)

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": input("Enter a question: ")}
  ]
)
print(response.choices[0].message.content
      )