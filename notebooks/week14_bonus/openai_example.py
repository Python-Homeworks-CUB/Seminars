import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)

prompt = """\
You're a bilingual language teacher. You speak both English and Russian.
Your task is to generate a flashcard for an english word in json format.


### Example

Input: "apple"
Output:
```json
{
    "word": "apple",
    "example": "I have an apple.",
    "example_translated": "У меня есть яблоко.",
    "translation": "яблоко"
}
```

### Your task

Input: "test"
Output:
"""

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="gpt-3.5-turbo",
)
print("Generated flashcard:")
print(chat_completion.choices[0].message.content)