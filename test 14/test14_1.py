from collections import defaultdict

def word_count(texts):
    count = defaultdict(int)
    for text in texts:
        for word in text.split():
            count[word] += 1
    return dict(count)
