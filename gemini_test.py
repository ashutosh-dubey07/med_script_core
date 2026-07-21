import os
from dotenv import load_dotenv
from google import genai


def test_gemini():
    try:
        load_dotenv()

        api_key = os.getenv("GEMINI_API_KEY")

        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents="Say only Hello."
        )

        print(response.text)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    test_gemini()