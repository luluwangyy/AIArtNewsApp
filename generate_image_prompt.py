import sys
import json
import openai
import base64

def get_openai_response(prompt, api_key):
    """
    Get a response from OpenAI's API.
    """
    openai.api_key = api_key
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an art curator and conceptual art expert."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
            max_tokens=500
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error calling OpenAI API: {e}", file=sys.stderr)
        return None

def main():
    if len(sys.argv) < 4:
        print("Usage: python3 generate_image_prompt.py \"<concept_base64>\" \"<material>\" \"<openai_api_key>\"")
        sys.exit(1)

    # Decode the base64 encoded concept to avoid command line argument issues
    try:
        concept_base64 = sys.argv[1]
        concept = base64.b64decode(concept_base64).decode('utf-8')
    except:
        # Fallback to direct argument if not base64 encoded
        concept = sys.argv[1]
    
    material = sys.argv[2]
    openai_api_key = sys.argv[3]
    
    image_prompt = f"Create a vivid, single-paragraph text-to-image prompt for this conceptual art installation:\n\n{concept}\n\nThe installation uses {material} as a primary material. Describe the central element, colors, textures, scale, and how viewers would experience it. Be specific and visual. The output must start with 'a realistic image of a museum exhibition scene where in the center of the exhibition there is' "
    
    prompt_result = get_openai_response(image_prompt, openai_api_key)
    
    if prompt_result:
        result = {"imagePrompt": prompt_result}
        print(json.dumps(result))
    else:
        print(json.dumps({"error": "Failed to generate image prompt"}))

if __name__ == "__main__":
    main() 