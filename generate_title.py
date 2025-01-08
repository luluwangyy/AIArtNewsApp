#generate the title


import replicate
import os
import sys
import json

# Set your API token



def generate_title(description):
    for event in replicate.stream(
        "mistralai/mistral-7b-v0.1",
        input={
            "top_k": 0,
            "top_p": 0.95,
            "prompt": f"Only write one eye-catching title of a news article about a new art show around an artwork that has this description {description} ",
            "max_tokens": 512,
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
    description = sys.argv[1]
    
    replicate_api_key = sys.argv[2]

    # Set API key
    os.environ["REPLICATE_API_TOKEN"] = replicate_api_key

   
    generate_title(description)
    