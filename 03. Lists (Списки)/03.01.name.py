bicycles = ['trek', 'cannondale', 'reline', 'specialized']
message = f"My first bicycles was a {bicycles[0].title()}"

print(message)

# Добавление элементов в список
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.append('iz')
print(motorcycles)

# Удаление элемента из списка по индексу
del motorcycles[0]
print(motorcycles)

# Удаление элемента с использованием pop()
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)

# Удаление элемента из списка по значению
motorcycles.remove('suzuki')
print(motorcycles)