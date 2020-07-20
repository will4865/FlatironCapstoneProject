def lemmatize_token(script):
    """Function used to automatically remove stop words, twitter_specific words and punctuation, tokenize, lemmatize
    and join together words into one string before modeling"""
    tokenized = word_tokenize(script)
    lemmatizer = WordNetLemmatizer()
    lemmatized = []
    for word in tokenized:
        lemmatized.append(lemmatizer.lemmatize(word))
    #lemmatized = ' '.join(lemmatized)
    return lemmatized
