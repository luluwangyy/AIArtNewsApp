# this generates the artist bio



import replicate
import os
import sys
import json

# Set your API token

from dotenv import load_dotenv
load_dotenv()
os.environ["REPLICATE_API_TOKEN"] = os.getenv('REPLICATE_API_TOKEN')

def generate_bio(name, bio):
    for event in replicate.stream(
        "mistralai/mixtral-8x7b-instruct-v0.1",
        input={
            "top_k": 50,
            "top_p": 0.9,
            "prompt": f"Write an artist bio about a visual artist whose name is {name} and whose key identity is {bio} in a coherent 5-sentence paragraph. The pronoun must be they/their/them. The output must starts with the artist name",
            "temperature": 0.6,
            "system_prompt": "You are a very helpful, respectful and honest assistant.",
            "length_penalty": 1,
            "max_new_tokens": 1024,
            "prompt_template": "<s>[INST] {prompt} [/INST] ",
            "presence_penalty": 0
        },
    ):
        print(str(event), end="")

if __name__ == "__main__":
    name = sys.argv[1]
    bio = sys.argv[2]
    #bio = "a girl from china and is queer"
    generate_bio(name,bio)
    