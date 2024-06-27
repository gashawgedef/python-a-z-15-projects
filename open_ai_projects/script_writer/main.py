import openai

# Set your OpenAI API key
openai.api_key = "your_actual_api_key_here"

# Example prompt for the API
prompt_text = "Translate the following English text into French: 'Hello, how are you?'"

# Call the OpenAI API to generate a completion based on the prompt
response = openai.Completion.create(
  engine="davinci-codex",
  prompt=prompt_text,
  max_tokens=50
)

# Print the generated response
print("Generated Response:")
print(response.choices[0].text.strip())
