import trafilatura
def extract_article(url:str) -> dict:
    downloaded = trafilatura.fetch_url(url)

    if not downloaded:
        return {
            "url":url,
            "title":None,
            'text':None,
            "success":False
        }
    
    extracted = trafilatura.extract(
        downloaded,
        include_comments=False,
        include_tables=False,
        no_fallback=True
    )

    if not extracted:
        return{
            "url":url,
            "title":None,
            'text':None,
            "success":False
        }
    
    metadata = trafilatura.extract_metadata(downloaded)

    return {
        "url": url,
        "title": metadata.title if metadata else None,
        "text": extracted.strip(),
        "success": True
    }