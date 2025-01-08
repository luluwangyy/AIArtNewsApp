# This generates the first image

import os
import sys
import json
import replicate
import openai
from dotenv import load_dotenv

def generate_conceptual_idea(theme, imagery, reference_conceptual, reference_visual):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": f"Please write a visual description of a conceptual artwork inspired by the concept of '{imagery}' within the theme of '{theme}'. It should be inspired by the artist statement of '{reference_conceptual}' and the visual style of '{reference_visual}'."
                }
            ],
            temperature=0.5
        )
        response_text = response['choices'][0]['message']['content'].strip()
        return response_text
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def generate_conceptual_artist_reference(theme):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Please ONLY give me the name of an artwork of a conceptual artist that is related to the theme of {theme}"}
            ],
            temperature=0.5
        )
        response_text = response['choices'][0]['message']['content'].strip()
        return response_text
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def generate_visual_artist_reference(imagery):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Please ONLY give me the name of an artwork of a visual artist that has depicted {imagery}"}
            ],
            temperature=0.5
        )
        response_text = response['choices'][0]['message']['content'].strip()
        return response_text
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def generate_image(description):
    description_art = f"A realistic photo that captures an artwork in an exhibition. No words in the picture. The artwork: {description}."
    response = openai.Image.create(
        model="dall-e-3",
        prompt=description_art,
        n=1,
        size="1024x1024"
    )
    image_url = response.data[0]['url']
    print(json.dumps(image_url))

def generate_image_re(prompt):
    description_art = f"A realistic photo that captures an installation in an exhibition. No words in the picture. The artwork: {prompt}."
    output = replicate.run(
        "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
        input={"prompt": description_art}
    )
    return output[0] if output else None  # Return the first URL

def main():
    try:
        if len(sys.argv) != 5:
            print(json.dumps({"error": "Usage: python generate_conceptualart.py <theme> <imagery> <replicate_api_key> <openai_api_key>"}))
            sys.exit(1)

        theme = sys.argv[1]
        imagery = sys.argv[2]
        replicate_api_key = sys.argv[3]
        openai_api_key = sys.argv[4]

        # Set API keys
        os.environ["REPLICATE_API_TOKEN"] = replicate_api_key
        openai.api_key = openai_api_key
        
        reference_conceptual = generate_conceptual_artist_reference(theme)
        reference_visual = generate_visual_artist_reference(imagery)
        description = generate_conceptual_idea(theme, imagery, reference_conceptual, reference_visual)
        
        image_url = generate_image_re(description)
        title = f"Conceptual Art inspired by {theme}"

        # Format the output as a JSON object
        output = {
            "url": image_url,
            "title": title,
            "description": description
        }
        
        # Print as JSON string
        print(json.dumps(output))
        
    except Exception as e:
        error_output = {
            "error": str(e)
        }
        print(json.dumps(error_output))
        sys.exit(1)

if __name__ == "__main__":
    main()
