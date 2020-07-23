def script_pull_imsdb(url):
    '''pull scripts from IMSDB.com'''
    html_page = requests.get(url)
    soup = BeautifulSoup(html_page.content, 'html.parser')
    script = str(soup.findAll('pre'))
    imsdb_scripts.append(script)
