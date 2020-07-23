def script_com_pull(list_to_pull):
    """use Selenium to navigate to scripts.com search result site, use Beautiful Soup to pull text data, 
    and add script data to dataframe at specific index"""
    for title in list_to_pull:
        script = []
        driver = webdriver.Chrome('/Users/will4856/Downloads/chromedriver')
        driver.get("https://www.google.com/")
        time.sleep(random.randint(1,5))
        elem = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input')
        elem.clear()
        elem.send_keys(title + ' ')
        time.sleep(random.randint(1,5))
        elem.send_keys('site:scripts.com')
        time.sleep(random.randint(1,5))
        elem.send_keys(Keys.RETURN)
        try:
            driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/a/h3').click()
        except:
            script = 'error'
            index_at = films_at_large[films_at_large['title'] == title].index.tolist() 
            add_script_to_df(index_at, script, films_at_large)
            continue
        BS_url = driver.current_url
        try:
            test_script = str(BS(BS_url, 'p'))
            test_script = test_script.replace('<p>','')
            test_script = test_script.replace('</p>','')
            test_script = test_script.split('<p')[0]
            test_script = test_script.split('</a>')
            for i in test_script:
                if 'href' in i:
                    script.append(i.split(';">')[0].split('<a')[0])
                    script.append(i.split(';">')[1])
                else:
                    script.append(i)
        except:
            script = 'error'
            index_at = films_at_large[films_at_large['title'] == title].index.tolist() 
            add_script_to_df(index_at, script, films_at_large)
            continue
        for i in range(2,101):
            try:
                test_script = str(BS(BS_url+'&p={}'.format(i), 'p'))
                test_script = test_script.replace('<p>','')
                test_script = test_script.replace('</p>','')
                test_script = test_script.split('<p')[0]
                test_script = test_script.split('</a>')
                for i in test_script:
                    if 'href' in i:
                        script.append(i.split(';">')[0].split('<a')[0])
                        script.append(i.split(';">')[1])
                    else:
                        script.append(i)
            except:
                break
        script = ' '.join(script)
        index_at = films_at_large[films_at_large['title'] == title].index.tolist() 
        add_script_to_df(index_at, script, films_at_large)
        driver.close()        
