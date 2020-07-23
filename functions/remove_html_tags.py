def remove_html_tags(text):
    """Remove html tags from a string using regex"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)
