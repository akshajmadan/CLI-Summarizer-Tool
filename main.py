from dotenv import load_dotenv
load_dotenv()
import os

from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

with open("myfile.txt", "r") as file:
    file_contents = file.read()

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Please summarize the following text:\n\n" + file_contents,
        }
    ],
    
    model="openai/gpt-oss-120b",
)

print(chat_completion.choices[0].message.content)