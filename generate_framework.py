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
        print("Usage: python3 generate_framework.py \"<reflection>\" \"<openai_api_key>\"")
        sys.exit(1)

    reflection = sys.argv[1]
    openai_api_key = sys.argv[2]
    
    framework_prompt = f"Based on the reflection: {reflection}\n\nCreate a 3-5 step framework for developing a conceptual art. Each step should be a short, inspiring guideline. Focus on encouraging artistic exploration and critical thinking about materials and their meanings. Format the response in bullet points and separate lines."
    
    framework = get_openai_response(framework_prompt, openai_api_key)
    
    if framework:
        result = {"framework": framework}
        print(json.dumps(result))
    else:
        print(json.dumps({"error": "Failed to generate framework"}))
        sys.exit(1)

if __name__ == "__main__":
    main() 