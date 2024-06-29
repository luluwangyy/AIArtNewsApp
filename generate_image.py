

#npm install express@4npm cache clean --force 
#npm install express@4           
#sudo chown -R 501:20 "/Users/luluwang/.npm  
#npm install express@4  

#pip install replicate --break-system-packages
import os
import sys
import json
import replicate


# Set your API token

from dotenv import load_dotenv
load_dotenv()
os.environ["REPLICATE_API_TOKEN"] = os.getenv('REPLICATE_API_TOKEN')

def generate_image(prompt):
    output = replicate.run(
        "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
        input={"prompt": prompt}
    )
    return output

if __name__ == "__main__":
    prompt = sys.argv[1]
    result = generate_image(prompt)
    print(json.dumps(result))  # Output the result as JSON
