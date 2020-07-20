def clean_lemmatize_token_alt(tweet):
    cleaned = tweet.translate(str.maketrans('', '', string.punctuation)).lower()
    tokenized = word_tokenize(cleaned)
    lemmatizer = WordNetLemmatizer()
    lemmatized = []
    for word in tokenized:
        lemmatized.append(lemmatizer.lemmatize(word))
    #lemmatized = ' '.join(lemmatized)
    return lemmatized
