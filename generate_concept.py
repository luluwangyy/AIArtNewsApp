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
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error calling OpenAI API: {e}", file=sys.stderr)
        return None

def main():
    if len(sys.argv) < 4:
        print("Usage: python3 generate_concept.py \"<creative_steps_base64>\" \"<material>\" \"<openai_api_key>\"")
        sys.exit(1)

    # Decode the base64 encoded steps to avoid command line argument issues
    try:
        creative_steps_base64 = sys.argv[1]
        creative_steps = base64.b64decode(creative_steps_base64).decode('utf-8')
    except:
        # Fallback to direct argument if not base64 encoded
        creative_steps = sys.argv[1]
    
    material = sys.argv[2]
    openai_api_key = sys.argv[3]
    
    concept_prompt = f"Based on these steps:\n\n{creative_steps}\n\nDevelop a brief concept for a conceptual art installation using {material}. Describe it in 4-5 sentences, focusing on innovation, unique exploration of the concept and unique use of the material."
    
    concept = get_openai_response(concept_prompt, openai_api_key)
    
    if concept:
        result = {"concept": concept}
        print(json.dumps(result))
    else:
        print(json.dumps({"error": "Failed to generate concept"}))

if __name__ == "__main__":
    main() 