animals = ("cat", "dog", "mouse", "rabbit")
score = 0

print("В волшебной коробке животные:", animals)

for round_num in range(2):
    answer = input(f"\n Раунд {round_num + 1}: Какое животное под номером {round_num + 1}? ")
    if animals[round_num] == answer:
        score += 1
        print("Правильно!")
    else: 
        print("Неправильно! Там было", animals[round_num])

print(f"Твой счёт: {score} из 2")
