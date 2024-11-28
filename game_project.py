import random

def choose_word():
    words = ["словарь", "программа", "санягучимен", "стол", "проигрыватель"]
    return random.choice(words)

def play():
    word = choose_word()
    word_completion = "_" * len(word) # инициализируется строкой из символов подчеркивания, длина которой равна длине загаданного слова. Это будет отображение текущего состояния угаданного слова.
    guessed = False # переменная, которая отслеживает, угадано ли слово.
    guessed_letters = [] # список для хранения угаданных букв
    tries = 6 # устанавливает количество попыток

    print("Давайте играть в Виселицу!")
    print(word_completion)
    print("\n")

    while not guessed and tries > 0: # цикл идет, пока игра может продолжаться
        guess = input("Введите букву или слово: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Вы уже угадали эту букву.")
            elif guess not in word:
                print("Буквы нет в слове.")
                tries -= 1
            else:
                print("Вы угадали букву!")
                guessed_letters.append(guess)
                word_completion = "".join([char if char in guessed_letters else "_" for char in word])

                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess == word:
                guessed = True
                word_completion = word
            else:
                print("Неправильное слово:", guess)
                tries -= 1
        else:
            print("Неправильный ввод. Попробуйте снова.")

        print("Осталось попыток:", tries)
        print(word_completion)
        print("\n")

    if guessed:
        print("Поздравляем! Вы угадали слово:", word)
    else:
        print("Вы проиграли. Загаданное слово было:", word)

if __name__ == "__main__":
    play()