import os
import sys
import json
import replicate
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def generate_image(prompt, api_token):
    """
    Generate an image using the Stability AI SDXL model
    
    Args:
        prompt (str): The text prompt to generate the image from
        api_token (str): Replicate API token
        
    Returns:
        list: List of image URLs generated
    """
    try:
        # Set API token
        os.environ["REPLICATE_API_TOKEN"] = api_token
        logger.info(f"Generating image for prompt: {prompt}")
        
        # Run the model
        output = replicate.run(
            "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
            input={"prompt": prompt}
        )
        
        logger.info(f"Generated output: {output}")
        return output
        
    except replicate.exceptions.ModelError as e:
        error_msg = {"error": f"Model error: {str(e)}"}
        logger.error(f"Model error: {str(e)}")
        print(json.dumps(error_msg))
        sys.exit(1)
    except Exception as e:
        error_msg = {"error": str(e)}
        logger.error(f"Unexpected error: {str(e)}")
        print(json.dumps(error_msg))
        sys.exit(1)

if __name__ == "__main__":
    try:
        # Validate command line arguments
        if len(sys.argv) < 4:
            error_msg = {"error": "Missing required arguments"}
            logger.error("Missing required arguments")
            print(json.dumps(error_msg))
            sys.exit(1)
            
        prompt = sys.argv[1]
        replicate_api_key = sys.argv[3]
        
        result = generate_image(prompt, replicate_api_key)
        print(json.dumps(result))
        
    except Exception as e:
        error_msg = {"error": f"Script error: {str(e)}"}
        logger.error(f"Script error: {str(e)}")
        print(json.dumps(error_msg))
        sys.exit(1)
