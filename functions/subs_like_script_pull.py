def subs_like_script_pull(dict_of_titles):
    """use Selenium and BeautifulSoup to pull script text from subslikescript.com"""
    for original_title, cleaned_title in dict_of_titles.items():
        driver = webdriver.Chrome('/Users/will4856/Downloads/chromedriver')
        driver.get("https://subslikescript.com/")
        elem = driver.find_element_by_xpath("/html/body/div/div/main/nav[1]/form/input")
        elem.clear()
        elem.send_keys(cleaned_title)
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div/div/main/article/ul/a').click()
        BS_url = driver.current_url
        script = BS(BS_url, 'div', class_= 'full-script')
        index_at = films_at_large[films_at_large['title'] == original_title].index.tolist() 
        add_script_to_df(index_at, script, films_at_large)
        driver.close()
