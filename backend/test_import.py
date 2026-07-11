from google import genai

print("Import successful!")

client = genai.Client(api_key="dummy")

print(type(client))