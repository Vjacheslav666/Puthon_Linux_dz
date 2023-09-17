import string

def word_exists(text):
    # Удаление знаков пунктуации из текста
    text = text.translate(str.maketrans("", "", string.punctuation))
    
    # Разбиение текста на слова
    words = text.split()
    
    # Проверка наличия слова в выводе
    def check_word_exists(word):
        return word in words
    
    return check_word_exists

# Пример использования
check_fn = word_exists("Hello world! How are you?")
print(check_fn("Hello"))  # True
print(check_fn("goodbye"))  # False