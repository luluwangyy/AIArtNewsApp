import os
import sys
import json
import logging
import openai

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def generate_bio(name, bio):
    try:
        #print('starting generating bio haha')
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": f"Write an artist bio about a visual artist named {name} whose identity is described as {bio}. Use they/them pronouns and create a coherent 5-sentence paragraph."
                }
            ],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        logger.error(f"Error generating bio: {str(e)}")
        return {"error": str(e)}

def main():
    #print ('start generating bio1')
    try:
        if len(sys.argv) != 4:
            print(json.dumps({"error": "Usage: python generate_bio.py <name> <bio> <openai_api_key>"}))
            sys.exit(1)

        name = sys.argv[1]
        bio = sys.argv[2]
        openai_api_key = sys.argv[3]

        # Set OpenAI API key
        openai.api_key = openai_api_key

        generated_bio = generate_bio(name, bio)
       #print(generated_bio)
        
        # Check if the result is an error dictionary
        if isinstance(generated_bio, dict) and "error" in generated_bio:
            print(json.dumps(generated_bio))
        else:
            # Format the output as JSON
            output = {
                "bio": generated_bio
            }
            print(json.dumps(output))
            
    except Exception as e:
        error_output = {
            "error": str(e)
        }
        print(json.dumps(error_output))
        sys.exit(1)

if __name__ == "__main__":
    main()