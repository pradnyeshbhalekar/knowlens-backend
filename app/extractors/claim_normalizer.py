import re
import string

def normalize_claim(text:str) -> str:
    if not text:
        return ""
    
    text = text.lower()
    text = text.translate(str.maketrans("","",string.punctuation))
    text = re.sub(r"\s+", " ", text).strip()
    return text