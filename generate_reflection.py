import sys
import json
import openai

def get_openai_response(prompt, api_key):
    """
    Get a response from OpenAI's API.
    """
    try:
        openai.api_key = api_key
        
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
        print(f"Error calling OpenAI API: {str(e)}", file=sys.stderr)
        return None

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 generate_reflection.py \"<art_description>\" \"<openai_api_key>\"")
        sys.exit(1)

    art_description = sys.argv[1]
    openai_api_key = sys.argv[2]
    
    reflection_prompt = f"Based on the art description: {art_description}\n\nProvide a thoughtful reflection on the conceptual elements and artistic potential. Consider themes, symbolism, and cultural context. Format the response in bullet points and separate lines."
    
    reflection = get_openai_response(reflection_prompt, openai_api_key)
    
    if reflection:
        result = {"reflection": reflection}
        print(json.dumps(result))
    else:
        print(json.dumps({"error": "Failed to generate reflection"}))
        sys.exit(1)

if __name__ == "__main__":
    main() 