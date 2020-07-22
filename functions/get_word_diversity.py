def get_word_diversity(script):
    unique_word_count = len(dict(Counter(list(script))).keys())
    return unique_word_count
