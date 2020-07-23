def BS(url, find_key, class_ = None):
    """instatiate Beautiful soup session, pull text from url using find_key and optional class_"""
    html_page = requests.get(url)
    soup = BeautifulSoup(html_page.content, 'html.parser')
    script = soup.findAll(find_key, class_ = class_)
    return str(script)
