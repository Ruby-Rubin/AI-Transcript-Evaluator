import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
api_key=os.getenv("GROQ_API_KEY")
)

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
- Imagine you are a English professor grading a student's presentation. Grade the transcript based on the three criteria above.
- State the reason alone, no need to mention about the transcript itself. For example, if the transcript is not clear, you can say "The speaker's ideas were not well organized and the language used was too complex for the audience to understand."
- Score from 1 to 10
- Reasons must be around 1-2 sentences for each category
- No markdown
- No extra text
- Return ONLY valid JSON
- Do not wrap JSON in markdown
- Do not add explanations
- Do not add comments
- Output must be parseable by json.loads()


Transcript:
{transcript}
"""

  response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0
)

  text = response.choices[0].message.content.strip()

  text = text.replace("```json", "")
  text = text.replace("```", "")

  

  return json.loads(text)


