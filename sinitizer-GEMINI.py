import requests
import re

def sanitize_pasted_text(text, api_key):
    """
    Sanitizes pasted text to make it more human-like using the Gemini API.

    Args:
        text: The text to sanitize.
        api_key: Your Gemini API key.

    Returns:
        The sanitized text, or None if an error occurred.
    """

    # Preprocessing: Remove extra whitespace and newlines
    text = re.sub(r'\s+', ' ', text).strip()

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"  # Include your API key here
    }

    # Example prompt engineering for a more natural and engaging tone
    prompt = f"""
    Please rewrite the following pasted text to sound more natural and engaging, as if a human wrote it.  Avoid overly formal or robotic language, and ensure the meaning is preserved.

    ```
    {text}
    ```
    """


    try:
        response = requests.post(
            "https://api.gemini.yahoo.com/v1/completions",  # or the appropriate endpoint
            headers=headers,
            json={"prompt": prompt, "max_tokens": 500}  # Adjust max_tokens as needed
        )
        response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)


        generated_text = response.json()["choices"][0]["text"].strip()
        return generated_text

    except requests.exceptions.RequestException as e:
        print(f"Error communicating with the Gemini API: {e}")
        return None

    except KeyError as e:
        print(f"Unexpected response format from Gemini API: {e}")  # Handle potential key errors
        print(response.json()) # Print the full response for debugging
        return None



# Example usage:
api_key = "YOUR_GEMINI_API_KEY"  # Replace with your actual API key
pasted_text = """
This is some pasted   text.  It has  weird   spacing and might sound a bit robotic.    We want to make it  more human-like.
"""

sanitized_text = sanitize_pasted_text(pasted_text, api_key)

if sanitized_text:
    print("Sanitized text:\n", sanitized_text)