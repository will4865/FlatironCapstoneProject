def pdf_text_pull(title):
    """pull all text data from .pdf file"""
    return str(high_level.extract_text('/Users/will4856/Downloads/scripts_to_scrape/{}.pdf'.format(title)))