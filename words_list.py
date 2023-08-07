from random_word import RandomWords
r = RandomWords()


def get_random_words_list() -> str:
    
    words_list = []
    
    for _ in range(10):  
        random_word = r.get_random_word()
        words_list.append(random_word)
    
    return words_list