def pull_drew_scripts(url):
    '''pull titles from Drews Script-o-Rama
    url: url that points to Drews Script-o-Rama index page'''
    html_page = requests.get(url)
    soup = BeautifulSoup(html_page.content, 'html.parser')
    titles = list(soup.findAll('p', align = 'LEFT'))[::2]
    for x in titles:
        temp_titles.append(str(x).split('<a')[1])
