from openai import OpenAI

endpoint = "https://rapidinsights-resource.services.ai.azure.com/openai/v1"
deployment_name = "gpt-5"
api_key = "9nmxbUsgzQhFGlMjB0MrUFjXyoClHrHwOuLSg1EXUqNIX1pQ5GvFJQQJ99CJACHYHv6XJ3w3AAAAACOGhf6l"

client = OpenAI(
    base_url=endpoint,
    api_key=api_key
)

response = client.responses.create(
    model=deployment_name,
    input="What is the capital of France?",
)

print(response.output_text)
