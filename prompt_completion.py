import os

from groq import Groq

print(os.environ.get("GROQ_API_KEY"))

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


def get_completion(prompt, model="llama3-8b-8192"):
    messages = [{"role": "user", "content": prompt}]
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model,
        temperature=0
    )

    response = chat_completion.choices[0].message.content
    print(response)
    return response


def get_all(prompt):
    print("")


def get_all1(prompt):
    print("gemma-7b-it".upper())
    get_completion(prompt, "gemma-7b-it")
    print("llama3-70b-8192".upper())
    get_completion(prompt, "llama3-70b-8192")
    print("llama3-8b-8192".upper())
    get_completion(prompt, "llama3-8b-8192")
    print("mixtral-8x7b-32768".upper())
    get_completion(prompt, "mixtral-8x7b-32768")
