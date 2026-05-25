magic_box = ("Kiwi", "Banana", "Cherry")
backpack = ["🍎 Apple", "🍌 Banana", "🍒 Cherry"]
fruit = magic_box[2]
total = len(magic_box)
has_banana = "Banana" in magic_box

print("Волшебная коробка (кортеж):", magic_box)
print("Рюкзак (список):", backpack)

# Кортеж не поддерживает замену элементов - magic_box[0] = "Kiwi"

backpack.append("orange")
print("Рюкзак после добавления:", backpack)

# Кортеж не дает мне добавить туда новый элемент: print("Коробка после добавления:", magic_box) == AttributeError: 'tuple' object has no attribute 'append'

print("Смотрим элемент под номером 1:", fruit)
print("Сколько фруктов в коробке? Их", total)
print("Есть ли бананы в коробке?", has_banana)

for item in magic_box:
    print("Перебираем все фрукты в коробке:", item)
