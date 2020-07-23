def get_tn(url):
    '''automates pull of release_date, title, production_budget, dom_box_office, and worldwide_box_office
    
    url: url of  thenumbers.com page that lists relevant info for web scraping
        example: https://www.the-numbers.com/movie/budgets/all'''
    html_page = requests.get(url)
    soup = BeautifulSoup(html_page.content,'html.parser')
    titles = soup.findAll('td')
    new_test_entry = list(titles)
    final_release_dates = new_test_entry[1:][::3][::2]
    for x in final_release_dates:
        new_final_release_dates.append(str(x).split('">')[1][:-9])
    final_titles = new_test_entry[2:][::3][::2]
    for x in final_titles:
        new_final_titles.append(str(x).split('=summary">')[1][:-13])
    final_prod_bud = new_test_entry[3:][::3][::2]
    for x in final_prod_bud:
        new_final_prod_bud.append(str(x).split('$')[1][:-5])
    final_dom_gross = new_test_entry[4:][::3][::2]
    for x in final_dom_gross:
        new_final_dom_gross.append(str(x).split('$')[1][:-5])
    final_world_gross = new_test_entry[5:][::3][::2]
    for x in final_world_gross:
        new_final_world_gross.append(str(x).split('$')[1][:-5])
