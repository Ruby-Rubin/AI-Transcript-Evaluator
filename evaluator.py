import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def evaluate_transcript(transcript):

    prompt = f"""
    Evaluate the transcript on ONLY these criteria:

    1. Clarity
    2. Technical Accuracy
    3. Professionalism

    Return ONLY valid JSON.

    {{
      "clarity": {{
        "score": 0,
        "reason": ""
      }},
      "technical_accuracy": {{
        "score": 0,
        "reason": ""
      }},
      "professionalism": {{
        "score": 0,
        "reason": ""
      }}
    }}

    Rules:
    - Score from 1 to 10
    - Reasons must be under 10 words
    - No markdown
    - No extra text

    Transcript:
    {transcript}
    """

    response = model.generate_content(prompt)

    text = response.text.strip()

    text = text.replace("```json", "")
    text = text.replace("```", "")

    return json.loads(text) 