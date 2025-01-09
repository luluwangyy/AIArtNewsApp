#generate the title
# This generates the first image

import os
import sys
import json
import replicate
import openai
from dotenv import load_dotenv

def generate_title(description):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": f"Only write one eye-catching title of a news article about a new art show around an artwork that has this description {description} "
                }
            ],
            temperature=0.5
        )
        response_text = response['choices'][0]['message']['content'].strip()
        return response_text
    except Exception as e:
        print(f"An error occurred: {e}")
        return []




if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python generate_title.py <description> <openai_api_key>")
        sys.exit(1)

    description = sys.argv[1]
    openai_api_key = sys.argv[2]


    # Set API keys
    openai.api_key = openai_api_key

    
    final_title = generate_title(description)
    
   
    print(final_title)






