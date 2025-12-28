from urllib.parse import urlparse,parse_qs,unquote

def normalize_ddg_url(raw_url: str) -> str:
    if raw_url.startswith("//duckduckgo.com/l/"):
        parsed = urlparse('https:'+raw_url)
        qs = parse_qs(parsed.query)

        if "uddg" in qs:
            return unquote(qs['uddg'][0])
        
    return raw_url