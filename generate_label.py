import os
import sys
import json
import openai
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def generate_label(description):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": f"Write a concise label for the artwork described as: {description}. Format: Title, Year: 2024, Medium, Dimensions, Collection, Location."
                }
            ],
            temperature=0.6
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        logger.error(f"Error generating label: {str(e)}")
        return {"error": str(e)}

def main():
    try:
        if len(sys.argv) != 3:
            print(json.dumps({"error": "Usage: python generate_label.py <description> <openai_api_key>"}))
            sys.exit(1)

        description = sys.argv[1]
        openai_api_key = sys.argv[2]

        # Set OpenAI API key
        openai.api_key = openai_api_key

        result = generate_label(description)
        
        if isinstance(result, dict) and "error" in result:
            print(json.dumps(result))
        else:
            print(json.dumps({"title": result}))

    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)

if __name__ == "__main__":
    main()