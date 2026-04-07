import os
from google import genai
from google.genai import types

def test():
    key = "AIzaSyDgNbymGqTYK6wZlMI6OBhGPWkfxmmFXxI"
    client = genai.Client(api_key=key)
    try:
        r = client.models.generate_content(model="gemini-2.5-flash", contents="Respond with exactly 'OK' if you receive this.")
        print("SUCCESS:", r.text)
    except Exception as e:
        print("ERROR:", str(e))

if __name__ == "__main__":
    test()
