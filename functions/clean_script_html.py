def clean_script_html(script):
    '''removes html tags from scripts scraped from the web'''
    cleaned_script = script.replace('[','')
    cleaned_script = cleaned_script.replace(']','')
    cleaned_script = cleaned_script.replace('<pre>','')
    cleaned_script = cleaned_script.replace('</pre>','')
    cleaned_script = cleaned_script.replace('<b>','')
    cleaned_script = cleaned_script.replace('</b>','')
    cleaned_script = cleaned_script.replace('</pre>','')
    cleaned_script = cleaned_script.replace('\n','')
    cleaned_script = cleaned_script.replace('\r','')
    cleaned_script = cleaned_script.replace('<html>','')
    cleaned_script = cleaned_script.replace('</html>','')
    cleaned_script = cleaned_script.replace('<head','')
    cleaned_script = cleaned_script.replace('</head>','')
    cleaned_script = cleaned_script.replace('<title>','')
    cleaned_script = cleaned_script.replace('</title>','')
    return cleaned_script
