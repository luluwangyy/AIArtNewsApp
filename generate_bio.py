import replicate
import os
import sys
import json

def generate_bio(name, bio):
    for event in replicate.stream(
          "mistralai/mistral-7b-v0.1",
        input={
            "top_k": 0,
            "top_p": 0.95,
            "prompt": f"Write an artist bio about a visual artist whose name is {name} and whose key identity is {bio} in a coherent 5-sentence paragraph. The pronoun must be they/their/them. The output must starts with the artist name",
            "temperature": 0.6,
            "temperature": 0.7,
            "length_penalty": 1,
            "max_new_tokens": 150,
            "prompt_template": "<s>[INST] {prompt} [/INST] ",
            "presence_penalty": 0,
            "log_performance_metrics": False
        },
       
    ):
        print(str(event), end="")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python generate_bio.py <name> <bio> <replicate_api_key>")
        sys.exit(1)

    name = sys.argv[1]
    bio = sys.argv[2]
    replicate_api_key = sys.argv[3]

    # Set API key
    os.environ["REPLICATE_API_TOKEN"] = replicate_api_key

    generate_bio(name, bio)
