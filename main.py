def proc1():
    n = int(input("ввод кол слов:"))
    result = " "
    for i in range(n):
        w = input(f"ввод слов {i + 1}:")
        result += w + " "
    print("результат:", result.strip())

def proc2():
    n = int(input("ввод кол слов:"))
    result = []
    for i in range(n):
        result.append(str(input()))

    result = []
    while(new_word := str(input())) != "stop":
        result.append(new_word)
        print(" ".join(result))


def proc3():
    result = []
    while (new_word := str(input())) != "stop":
        if "ф" in new_word or  "Ф" in new_word:
            print("Ого! Это редкое слово!")
    else:
        print("Эх,это не очень редкое слово")

def proc4():
    import random
    error_count = 0
    count = 0
    while error_count < 3:
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        if int(input(f"{a} + {b} = ")) == a + b:
            count += 1
            print('Правильно!')
        else:
            error_count += 1
            print('Неправильно!')
    print(f"Игра окончена. Правильных ответов {count}")

proc1(),proc2(),proc3(),proc4()
