

from openai import OpenAI

# client = OpenAI()
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key= "sk-BDIdgPs7a8U59PSozY_xyjXEjCH8obrS5S231TnOZ1T3BlbkFJEizG6ROgXjKMx3alBmBc6ilKAqChNac5bu8FHul2cA",
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a vertual assistant, name jarvis skilled in genral tasks like alexa and google cloud."},
    {"role": "user", "content": "What is coding"}

  ]
)

print(completion.choices[0].message)