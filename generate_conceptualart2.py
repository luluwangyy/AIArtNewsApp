#this generates the first image

#npm install express@4npm cache clean --force 
#npm install express@4           
#sudo chown -R 501:20 "/Users/luluwang/.npm  
#npm install express@4  

#pip install replicate --break-system-packages
import os
import sys
import json
import replicate

import openai
from dotenv import load_dotenv
load_dotenv()


openai.api_key = os.getenv('OPENAI_API_KEY')

# Setup your OpenAI API key from the environment variables




def generate_conceptual_idea(theme, imagery,reference_conceptual,reference_visual):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                "role": "user",
              "content": f"Please write a visual description of a conceptual artwork inspired by the concept of '{imagery}' within the theme of '{theme}'. It should be inspired by the artist statement of  '{reference_conceptual}' and the  visual style of '{reference_visual}'."
                }
            ],
            temperature=0.5
        )
        # print("API Response:", response)  # Print the full API response for debugging
        response_text = response['choices'][0]['message']['content'].strip()
        return response_text
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def generate_conceptualArtist_reference(theme):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"please ONLY give me a name of an artwork of a conceptual artist that is related to the theme of {theme}"}
            ],
            temperature=0.5
        )
        # print("API Response:", response)  # Print the full API response for debugging
        response_text = response['choices'][0]['message']['content'].strip()
        return response_text
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def generate_visualArtist_reference(imagery):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"please ONLY give me the name of an artwork of a visual artist has depict {imagery}"}
            ],
            temperature=0.5
        )
        # print("API Response:", response)  # Print the full API response for debugging
        response_text = response['choices'][0]['message']['content'].strip()
        return response_text
    except Exception as e:
        print(f"An error occurred: {e}")
        return []



# Set your API token
replicate.api_key = os.getenv('REPLICATE_API_TOKEN')


def generate_image_re(prompt):
    description_art = f"A realistic photo that capture an artwork in an exhibition. No words in the picture. The artwork : {prompt}. "
    output = replicate.run(
        "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
        input={"prompt": description_art}
    )
    print(json.dumps(output))

if __name__ == "__main__":
    theme = sys.argv[1]
    imagery = sys.argv[2]
   #print ("theme in python", theme)
    #print ("imagery in python", imagery)
    reference_conceptual = generate_conceptualArtist_reference(theme)
    reference_visual = generate_visualArtist_reference(imagery)
    final_idea = generate_conceptual_idea (theme, imagery,reference_conceptual,reference_visual)

    
    generate_image_re(final_idea)
    print(final_idea)
    
