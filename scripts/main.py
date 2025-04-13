import pandas as pd
import matplotlib.pyplot as plt
import os

# Создание папки results, если она не существует
os.makedirs('results', exist_ok=True)

# Загрузка данных
try:
    data = pd.read_csv('house-price.csv')  # Убедитесь, что файл находится в той же директории, если нет, то вставьте сюда полный путь к файлу
except FileNotFoundError:
    print("Ошибка: файл house-price.csv не найден в текущей директории")
    print(f"Текущая директория: {os.getcwd()}")
    exit()

# Анализ влияния парковки на цену
parking_analys = data.groupby('parking')['price'].agg(['median', 'mean', 'count'])
print("Анализ влияния парковки на цену:")
print(parking_analys)

# Визуализация: медианная цена в зависимости от количества парковочных мест
plt.figure(figsize=(10, 6))
parking_analys['median'].plot(kind='bar', color='blue')
plt.title('Медианная цена в зависимости от количества парковочных мест')
plt.xlabel('Количество парковочных мест')
plt.ylabel('Медианная цена')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='-', alpha=0.7)
plt.tight_layout()

# Сохранение графика
output_path = os.path.join('results', 'price_by_parking.png')
plt.savefig(output_path)
print(f"График сохранен в: {output_path}")

# Дополнительная визуализация:для наглядности распределения цен
plt.figure(figsize=(10, 6))
data.boxplot(column='price', by='parking', grid=True)
plt.title('Распределение цен по количеству парковочных мест')
plt.suptitle('')
plt.xlabel('Количество парковочных мест')
plt.ylabel('Цена')
plt.tight_layout()

output_path_boxplot = os.path.join('results', 'price_distribution_by_parking.png')
plt.savefig(output_path_boxplot)
print(f"График boxplot сохранен в: {output_path_boxplot}")

plt.show()