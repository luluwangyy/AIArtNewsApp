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
                    "content": f"Create a title for an art news article about an artwork with the following description: {description}. The title should be attractive,  evocative, and no more than 12 words. Do not include quotes around the title in your response."
                }
            ],
            temperature=0.7
        )
        response_text = response['choices'][0]['message']['content'].strip()
        return response_text
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def main():
    try:
        if len(sys.argv) != 3:
            print(json.dumps({"error": "Usage: python generate_title.py <description> <openai_api_key>"}))
            sys.exit(1)

        description = sys.argv[1]
        openai_api_key = sys.argv[2]

        # Set OpenAI API key
        openai.api_key = openai_api_key

        result = generate_title(description)
        
        if isinstance(result, dict) and "error" in result:
            print(json.dumps(result))
        else:
            print(json.dumps({"title": result}))

    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)

if __name__ == "__main__":
    main()


