import openai

# Replace this with your OpenAI API key
openai.api_key = "YOUR_API_KEY"


def sanitize_text(input_text):
    """
    Sends the input text to the GPT API for sanitization and improvement.

    Args:
        input_text (str): The text to sanitize and improve.

    Returns:
        str: The sanitized and improved text.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Use "gpt-3.5-turbo" for a less expensive option
            messages=[
                {"role": "system",
                 "content": "You are a helpful assistant that improves text to make it more human-readable, polished, and clear."},
                {"role": "user", "content": input_text}
            ],
            max_tokens=2000,
            temperature=0.7
        )
        improved_text = response["choices"][0]["message"]["content"]
        return improved_text
    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    print("Paste your text below (type 'exit' to quit):")
    while True:
        # Read user input
        user_input = input("\nYour text: ")
        if user_input.lower() == "exit":
            print("Exiting. Goodbye!")
            break

        # Sanitize and improve the text
        result = sanitize_text(user_input)
        print("\nSanitized Text:\n")
        print(result)
