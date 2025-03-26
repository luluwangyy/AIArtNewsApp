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
        dict: Dictionary with image URL
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
        
        # Extract URLs from output
        if isinstance(output, list) and output:
            # Check if we have FileOutput objects in the list
            first_output = output[0]
            
            # For FileOutput objects, convert to string to get the URL
            # FileOutput objects convert to their URL when cast to string
            url = str(first_output)
            logger.info(f"Extracted URL: {url}")
            
            return {"url": url}
        else:
            url = str(output) if output else None
            logger.info(f"Extracted URL: {url}")
            return {"url": url}
        
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
        # Log arguments for debugging
        logger.info(f"Received {len(sys.argv) - 1} arguments")
        
        # Validate command line arguments
        if len(sys.argv) < 3:
            error_msg = {"error": "Missing required arguments"}
            logger.error(f"Missing required arguments. Expected: prompt, api_key. Got: {len(sys.argv)-1} arguments")
            print(json.dumps(error_msg))
            sys.exit(1)
            
        prompt = sys.argv[1]
        replicate_api_key = sys.argv[2]
        
        logger.info(f"Prompt length: {len(prompt)}")
        logger.info(f"Prompt first 50 chars: {prompt[:50]}...")
        logger.info(f"API key length: {len(replicate_api_key)}")
        logger.info(f"API key first 10 chars: {replicate_api_key[:10]}...")
        
        # Validate API key format
        if not replicate_api_key.startswith('r8_'):
            error_msg = {"error": "Invalid Replicate API key format"}
            logger.error(f"Invalid Replicate API key format. Keys should start with 'r8_'")
            print(json.dumps(error_msg))
            sys.exit(1)
        
        result = generate_image(prompt, replicate_api_key)
        print(json.dumps(result))
        
    except Exception as e:
        error_msg = {"error": f"Script error: {str(e)}"}
        logger.error(f"Script error: {str(e)}")
        print(json.dumps(error_msg))
        sys.exit(1)
