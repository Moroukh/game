import random

def play_game():
    
    user_score = 0
    computer_score = 0

    choices = ["рыцарь", "принцесса", "ведьма", "дракон", "чудище"]

    print("Начинаем игру 'Рыцарь, Принцесса, Ведьма, Дракон, Чудище'!")
    print("Правила победы:")
    print("Рыцарь побеждает Дракона и Чудище")
    print("Принцесса побеждает Рыцаря и Ведьму")
    print("Ведьма побеждает Рыцаря и Чудище")
    print("Дракон побеждает Принцессу и Ведьму")
    print("Чудище побеждает Принцессу и Дракона")
    print("-" * 30)

    while True:
        user_choice = input(f"Выбери: {', '.join(choices)}? (или 'exit' для выхода): ").lower()
        if user_choice == "exit":
            print("-" * 30)
            print("Игра завершена.")
            print(f"Финальный счет: Твой - {user_score}, Компьютера - {computer_score}")
            if user_score > computer_score:
                print("Поздравляем! Ты выиграл игру!")
            elif computer_score > user_score:
                print("Компьютер одержал победу в игре.")
            else:
                print("Игра закончилась ничьей.")
            break

        if user_choice not in choices:
            print("Неверный выбор. Пожалуйста, выбери один из предложенных вариантов.")
            continue

        computer_choice = random.choice(choices)
        print(f"Компьютер выбрал: {computer_choice.capitalize()}")

        if user_choice == computer_choice:
            print("Ничья!")
        elif (user_choice == "рыцарь" and (computer_choice == "дракон" or computer_choice == "чудище")) or \
             (user_choice == "принцесса" and (computer_choice == "рыцарь" or computer_choice == "ведьма")) or \
             (user_choice == "ведьма" and (computer_choice == "рыцарь" or computer_choice == "чудище")) or \
             (user_choice == "дракон" and (computer_choice == "принцесса" or computer_choice == "ведьма")) or \
             (user_choice == "чудище" and (computer_choice == "принцесса" or computer_choice == "дракон")):
            print("Ты победил!")
            user_score += 1
        else:
            print("Компьютер победил!")
            computer_score += 1

        print(f"Текущий счет: Твой - {user_score}, Компьютера - {computer_score}")
        print("-" * 30)
        
play_game()
