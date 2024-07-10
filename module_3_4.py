# Напишите функцию single_root_words, которая принимает одно обязательное слово
# в параметр root_word, а далее неограниченную последовательность в параметр *other_words.
# Функция должна составить новый список same_words только из тех слов списка other_words,
# которые содержат root_word или наоборот root_word содержит одно из этих слов.
# После вернуть список same_words в качестве результата своей работы.
def single_root_words(root_word, *other_words):
    same_words = []  # Создаем пустой лист
    list_mod = [i.upper() for i in other_words]  # Преобразуем все элементы листа к верхнему регистру
    word_mod = root_word.upper()  # Преобразуем root_word к верхнему регистру
    for item in list_mod:  # Ищем вхождение root_word в списке other_words
        if word_mod in item:
            same_words.append(item)
        elif item in word_mod:  # Ищем вхождение элементов other_words в root_word
            same_words.append(item)  # Добавляем в список
    return same_words
    #print(word_mod)


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
