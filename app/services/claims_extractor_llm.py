import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_MODEL_KEY") 

GITHUB_MODELS_ENDPOINT = (
    "https://models.inference.ai.azure.com"
    "/chat/completions"
)



SYSTEM_PROMPT = """
You are a factual claim extraction system.

A factual claim is any declarative statement that asserts:
- An event
- A condition
- A trend
- A cause-effect relationship
- A quantitative change
- A reported action or decision

Claims MAY be:
- Attributed to sources (e.g., “experts say”, “reports indicate”)
- About markets, prices, or industry behavior
- About announced plans or decisions

Rules:
- Extract ONLY claims explicitly stated in the text
- Do NOT invent facts
- Do NOT merge multiple claims into one
- Do NOT include opinions, advice, or rhetorical language
- Preserve original meaning; light rephrasing for clarity is allowed

Return JSON ONLY in this format:
{ "claims": ["claim 1", "claim 2"] }

"""

def extract_claims_from_text(text:str) -> list[str]:
    if not text or len(text) < 150:
        return[]
    
    payload = {
        "model":"gpt-4o-mini",
        "messages":[
            {"role":"system","content":SYSTEM_PROMPT},
            {"role":"user",
             "content":f"""
Extract factual claims from the following article.
TEXT:
{text}
            """
            }
        ],
        "temperature":0.0,
    }
    headers = {
        "Authorization":f"Bearer {GITHUB_TOKEN}",
        "Content-Type":"application/json"
    }
    try:
        response = requests.post(
            GITHUB_MODELS_ENDPOINT,
            headers=headers,
            json=payload,
            timeout=60
        )

        response.raise_for_status()

        data = response.json()
        content = data["choices"][0]["message"]["content"]

        parsed = json.loads(content)
        claims = parsed.get("claims",[])

        cleaned = [
            c.strip()
            for c in claims
            if isinstance(c,str) and len(c.strip()) > 20
        ]

        return cleaned
    
    except Exception as e:
        print("Claims extraction failed: ",e)
        return []