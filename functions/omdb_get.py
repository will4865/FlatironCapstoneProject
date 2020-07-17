def omdb_get(list):
    for film in list:
        apikey='87ed8015'
        url = 'http://www.omdbapi.com/?apikey={}'.format(apikey)
        t = film
        plot = 'long'
        url_params = {'t': t, 'plot' : plot}
        response = requests.get(url, params = url_params)
        film_desc.append(response.json()) 
