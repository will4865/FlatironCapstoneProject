def pull_script_titles(url):
    '''pull titles from url using Beautiful Soup and clean titles before appending them to script_titles list
    url: url from IMSDB
        example: https://www.imsdb.com/alphabetical/A'''
    temp_titles1 = []
    temp_titles2 = []
    html_page = requests.get(url)
    soup = BeautifulSoup(html_page.content,'html.parser')
    titles = list(soup.findAll('p'))
    for x in titles:
        temp_titles1.append(str(x).split('title="')[1])
    for x in temp_titles1:
        temp_titles2.append(x.split('">')[0])
    for x in temp_titles2:
        script_titles.append(x.replace(' Script',''))
