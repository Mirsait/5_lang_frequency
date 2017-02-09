

def load_data(filepath):
    """load data from file"""
    with open(filepath) as file_obj:
        text = file_obj.read()
    return text


def get_most_frequent_words(text):
    """
    returns a list of frequent words in order of decreasing frequency
    """
    words = re.split('\W+', text[:].lower())
    dist = {}
    for word in words:
        if word in dist.keys():
            dist[word] += 1
        else:
            dist.setdefault(word, 1)
    def k(x): return x[1]
    arr = sorted(dist.items(), key=k, reverse=True)[0:10]
    return arr


if __name__ == '__main__':
    pass
