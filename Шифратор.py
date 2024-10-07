# задаем алфавит
eng_al = "abcdefghijklmnopqrstuvwxyz"

# функция шифрования Цезаря
def cript_caesar(char, step):
    # если не буква, то не шифруем
    if not char.isalpha():
        return char
    # находим индекс исходной буквы
    ind = eng_al.find(char.lower())
    # вычисляем новый индекс, используя шаг шифра
    res = eng_al[(ind + step) % len(eng_al)]
    # если исходная буква была заглавной, новую возвращаем тоже заглавной
    if char.isupper():
        return res.upper()
    # если нет, то возвращаем маленькую
    else:
        return res

# функция простой замены
def cript_simple(char, mapping):
    # если не буква, то не шифруем
    if not char.isalpha():
        return char
    # находим соответствие в таблице замены
    res = mapping.get(char.lower(), char)
    # если исходная буква была заглавной, новую возвращаем тоже заглавной
    if char.isupper():
        return res.upper()
    # если нет, то возвращаем маленькую
    else:
        return res

# получаем от пользователя выбор шифра
print("Выберите метод шифрования:")
print("1. Шифр Цезаря")
print("2. Простая замена")
choice = input("Введите 1 или 2: ")

# получаем от пользователя исходный текст
print("Введите текст:")
text = input()

if choice == "1":
    # получаем от пользователя шаг шифра
    print("Введите шаг:")
    step = int(input())
    res = ""
    # в цикле обрабатываем каждую букву с помощью функции шифрования Цезаря
    for c in text:
        res += cript_caesar(c, step)
    print(f"Результат при шаге {step}:", res, sep="\n")
elif choice == "2":
    # создаем таблицу простой замены
    mapping = {c: eng_al[(eng_al.index(c) + 3) % len(eng_al)] for c in eng_al}
    res = ""
    # в цикле обрабатываем каждую букву с помощью функции простой замены
    for c in text:
        res += cript_simple(c, mapping)
    print("Результат:", res, sep="\n")
else:
    print("Неверный выбор.")

input()