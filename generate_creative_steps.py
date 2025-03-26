import sys
import json
import openai

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
            max_tokens=600
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error calling OpenAI API: {e}", file=sys.stderr)
        return None

def main():
    if len(sys.argv) != 4:
        print("Usage: python3 generate_creative_steps.py \"<material>\" \"<framework>\" \"<openai_api_key>\"")
        sys.exit(1)

    material = sys.argv[1]
    framework = sys.argv[2]
    openai_api_key = sys.argv[3]
    
    creative_steps_prompt = f"Using the material '{material}' and this framework:\n\n{framework}\n\nAnswer each step in the framework in relation to the material. Be concise and thought-provoking. Format the response in bullet points and separate lines."
    
    creative_steps = get_openai_response(creative_steps_prompt, openai_api_key)
    
    if creative_steps:
        result = {"creativeSteps": creative_steps}
        print(json.dumps(result))
    else:
        print(json.dumps({"error": "Failed to generate creative steps"}))

if __name__ == "__main__":
    main() 