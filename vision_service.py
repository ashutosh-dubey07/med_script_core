import os
import mimetypes

from google import genai
from google.genai import types
from dotenv import load_dotenv

def extract_medicines(image_path):
    # load environment varaibles
    load_dotenv()

    # create gemini client
    client = genai.Client(
        api_key=os.getenv("GEMINI_API_KEY")
    )

    # read image
    with open(image_path, "rb") as f:
        image_bytes = f.read()

    # automatically detect image MIME type 
    mime_type, _ = mimetypes.guess_type(image_path)

    if mime_type is None:
        mime_type = "image/jpeg"

    # prompt for  vision
    prompt = """
You are an expert medical prescription reader.

Analyze this handwritten prescription carefully.

Instructions:

1. Extract ONLY medicine names.
2. Ignore patient name.
3. Ignore doctor name.
4. Ignore hospital name.
5. Ignore dosage.
6. Ignore frequency.
7. Ignore dates.
8. Ignore BP and weight.
9. Ignore signatures.
10.If you are not confident, mark the medicine as [Uncertain].
11. Return ONLY medicine names.
12. One medicine per line.
13. Do NOT explain anything.
14. Do NOT use markdown.
"""

    # send image + prompt to gemini
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=[
            prompt,
            types.Part.from_bytes(
                data=image_bytes,
                mime_type=mime_type
            )
        ]
    )

    return response.text