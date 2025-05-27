"""
Домашнє завдання #8: Купи (піраміди)
Основне завдання: Мінімізація витрат на з'єднання кабелів

Задача: Є декілька мережевих кабелів різної довжини, їх потрібно об'єднати 
по два за раз в один кабель у порядку, який призведе до найменших витрат.
Витрати на з'єднання двох кабелів дорівнюють їхній сумі довжин.

Використовуємо мінімальну купу (min-heap) для ефективного розв'язання.
"""

import heapq
from typing import List

def minimize_cable_connection_cost(cables: List[int]) -> int:
    """
    Знаходить мінімальну вартість з'єднання всіх кабелів.
    
    Алгоритм:
    1. Створюємо мінімальну купу з довжин кабелів
    2. На кожному кроці беремо два найкоротші кабелі
    3. З'єднуємо їх (вартість = сума їх довжин)
    4. Додаємо з'єднаний кабель назад до купи
    5. Повторюємо до тих пір, поки не залишиться один кабель
    
    Args:
        cables (List[int]): Список довжин кабелів
        
    Returns:
        int: Мінімальна загальна вартість з'єднання
    """
    if len(cables) <= 1:
        return 0
    
    # Створюємо мінімальну купу з довжин кабелів
    heap = cables.copy()
    heapq.heapify(heap)
    
    total_cost = 0
    operations = []  # Для відстеження операцій
    
    # Поки у купі більше одного кабелю
    while len(heap) > 1:
        # Беремо два найкоротші кабелі
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        
        # Вартість з'єднання
        connection_cost = first + second
        total_cost += connection_cost
        
        # Зберігаємо операцію для демонстрації
        operations.append((first, second, connection_cost))
        
        # Додаємо з'єднаний кабель назад до купи
        heapq.heappush(heap, connection_cost)
    
    return total_cost, operations

def minimize_cable_connection_cost_simple(cables: List[int]) -> int:
    """
    Спрощена версія функції, яка повертає тільки мінімальну вартість.
    
    Args:
        cables (List[int]): Список довжин кабелів
        
    Returns:
        int: Мінімальна загальна вартість з'єднання
    """
    if len(cables) <= 1:
        return 0
    
    heap = cables.copy()
    heapq.heapify(heap)
    
    total_cost = 0
    
    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        
        connection_cost = first + second
        total_cost += connection_cost
        
        heapq.heappush(heap, connection_cost)
    
    return total_cost

def demonstrate_algorithm_step_by_step(cables: List[int]):
    """
    Демонструє алгоритм покроково для кращого розуміння.
    
    Args:
        cables (List[int]): Список довжин кабелів
    """
    print(f"🔌 Початкові кабелі: {cables}")
    print(f"📊 Кількість кабелів: {len(cables)}")
    
    if len(cables) <= 1:
        print("✅ Менше двох кабелів - з'єднання не потрібне")
        return 0
    
    heap = cables.copy()
    heapq.heapify(heap)
    
    print(f"\n🏗️  Створено мінімальну купу: {heap}")
    print("\n📋 Покрокове виконання:")
    
    total_cost = 0
    step = 1
    
    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        connection_cost = first + second
        total_cost += connection_cost
        
        print(f"   Крок {step}: З'єднуємо кабелі {first} + {second} = {connection_cost}")
        print(f"            Вартість кроку: {connection_cost}")
        print(f"            Накопичена вартість: {total_cost}")
        
        heapq.heappush(heap, connection_cost)
        print(f"            Купа після кроку: {sorted(heap)}")
        print()
        
        step += 1
    
    print(f"✅ Загальна мінімальна вартість: {total_cost}")
    return total_cost

def compare_with_naive_approach(cables: List[int]):
    """
    Порівнює оптимальний підхід з наївним (сортування + послідовне з'єднання).
    
    Args:
        cables (List[int]): Список довжин кабелів
    """
    print(f"\n🔍 Порівняння підходів для кабелів: {cables}")
    
    # Оптимальний підхід (мінімальна купа)
    optimal_cost = minimize_cable_connection_cost_simple(cables)
    
    # Наївний підхід (просто сортуємо і з'єднуємо послідовно)
    sorted_cables = sorted(cables)
    naive_cost = 0
    current_length = sorted_cables[0]
    
    for i in range(1, len(sorted_cables)):
        current_length += sorted_cables[i]
        naive_cost += current_length
    
    print(f"   🎯 Оптимальний підхід (купа): {optimal_cost}")
    print(f"   📈 Наївний підхід (сортування): {naive_cost}")
    print(f"   💰 Економія: {naive_cost - optimal_cost} ({((naive_cost - optimal_cost) / naive_cost * 100):.1f}%)")

def test_algorithm():
    """Тестує алгоритм на різних прикладах"""
    print("🧪 ТЕСТУВАННЯ АЛГОРИТМУ")
    print("=" * 50)
    
    test_cases = [
        [4, 3, 2, 6],           # Основний приклад
        [1, 2, 3, 4, 5],        # Послідовні числа
        [10, 20, 30],           # Простий випадок
        [1, 1, 1, 1],           # Однакові довжини
        [100],                   # Один кабель
        [],                      # Порожній список
        [5, 10, 15, 20, 25, 30], # Більший приклад
        [1, 100, 2, 99, 3, 98]   # Змішані великі і малі значення
    ]
    
    for i, cables in enumerate(test_cases, 1):
        print(f"\n📊 Тест {i}: {cables}")
        
        if len(cables) <= 1:
            print(f"   Результат: 0 (менше двох кабелів)")
            continue
        
        cost = minimize_cable_connection_cost_simple(cables)
        print(f"   Мінімальна вартість: {cost}")
        
        # Для невеликих прикладів показуємо детальний розбір
        if len(cables) <= 6:
            print("   Детальний розбір:")
            demonstrate_algorithm_step_by_step(cables)

def analyze_complexity():
    """Аналізує складність алгоритму"""
    print("\n📈 АНАЛІЗ СКЛАДНОСТІ АЛГОРИТМУ")
    print("=" * 40)
    print("Часова складність: O(n log n)")
    print("  • Створення купи: O(n)")
    print("  • n-1 операцій видалення та вставки: O((n-1) * log n)")
    print("  • Загальна: O(n log n)")
    print("\nПросторова складність: O(n)")
    print("  • Зберігання купи: O(n)")
    print("\n🎯 Оптимальність:")
    print("  • Жадібний алгоритм дає оптимальне рішення")
    print("  • Завжди вибираємо два найкоротші кабелі")
    print("  • Мінімізуємо вплив довгих кабелів на загальну вартість")

def main():
    """Головна функція демонстрації"""
    print("🔌 ДОМАШНЄ ЗАВДАННЯ #8: МІНІМІЗАЦІЯ ВИТРАТ НА З'ЄДНАННЯ КАБЕЛІВ")
    print("=" * 70)
    print("Використання мінімальної купи (heapq) для оптимального з'єднання кабелів")
    
    # Основний приклад
    cables = [4, 3, 2, 6]
    print(f"\n🎯 Основний приклад: {cables}")
    cost, operations = minimize_cable_connection_cost(cables)
    
    print(f"\n📋 Послідовність операцій:")
    for i, (first, second, result) in enumerate(operations, 1):
        print(f"   {i}. З'єднуємо {first} + {second} = {result}")
    
    print(f"\n✅ Мінімальна загальна вартість: {cost}")
    
    # Детальна демонстрація
    print(f"\n" + "=" * 70)
    print("🔍 ДЕТАЛЬНА ДЕМОНСТРАЦІЯ АЛГОРИТМУ")
    demonstrate_algorithm_step_by_step(cables)
    
    # Порівняння підходів
    print(f"\n" + "=" * 70)
    print("⚖️  ПОРІВНЯННЯ З НАЇВНИМ ПІДХОДОМ")
    compare_with_naive_approach(cables)
    compare_with_naive_approach([1, 2, 3, 4, 5])
    compare_with_naive_approach([10, 1, 20, 2, 30, 3])
    
    # Тестування
    test_algorithm()
    
    # Аналіз складності
    analyze_complexity()
    
    print(f"\n🎉 Завдання виконано успішно!")

if __name__ == "__main__":
    main()
