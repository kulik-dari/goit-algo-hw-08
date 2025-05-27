"""
Домашнє завдання #8: Купи (піраміди)
Додаткове завдання: Злиття k відсортованих списків

Задача: Дано k відсортованих списків цілих чисел. 
Потрібно об'єднати їх у один відсортований список.
Використовуємо мінімальну купу для ефективного злиття.
"""

import heapq
from typing import List, Iterator

def merge_k_lists(lists: List[List[int]]) -> List[int]:
    """
    Об'єднує k відсортованих списків в один відсортований список 
    з використанням мінімальної купи.
    
    Алгоритм:
    1. Ініціалізуємо купу першими елементами з кожного списку
    2. На кожному кроці витягуємо мінімальний елемент з купи
    3. Додаємо наступний елемент з того ж списку до купи
    4. Повторюємо до тих пір, поки купа не порожня
    
    Args:
        lists (List[List[int]]): Список відсортованих списків
        
    Returns:
        List[int]: Об'єднаний відсортований список
    """
    if not lists:
        return []
    
    # Фільтруємо порожні списки
    non_empty_lists = [lst for lst in lists if lst]
    if not non_empty_lists:
        return []
    
    # Мінімальна купа: (значення, індекс_списку, індекс_елементу)
    heap = []
    
    # Ініціалізуємо купу першими елементами з кожного списку
    for list_idx, lst in enumerate(non_empty_lists):
        if lst:  # Перевіряємо, що список не порожній
            heapq.heappush(heap, (lst[0], list_idx, 0))
    
    result = []
    
    # Витягуємо елементи з купи та додаємо наступні
    while heap:
        value, list_idx, element_idx = heapq.heappop(heap)
        result.append(value)
        
        # Якщо в списку є наступний елемент, додаємо його до купи
        if element_idx + 1 < len(non_empty_lists[list_idx]):
            next_value = non_empty_lists[list_idx][element_idx + 1]
            heapq.heappush(heap, (next_value, list_idx, element_idx + 1))
    
    return result

def merge_k_lists_with_iterators(lists: List[List[int]]) -> List[int]:
    """
    Альтернативна реалізація з використанням ітераторів.
    
    Args:
        lists (List[List[int]]): Список відсортованих списків
        
    Returns:
        List[int]: Об'єднаний відсортований список
    """
    if not lists:
        return []
    
    # Створюємо ітератори для кожного списку
    iterators = [iter(lst) for lst in lists if lst]
    heap = []
    
    # Ініціалізуємо купу першими елементами
    for i, iterator in enumerate(iterators):
        try:
            value = next(iterator)
            heapq.heappush(heap, (value, i, iterator))
        except StopIteration:
            continue
    
    result = []
    
    while heap:
        value, list_idx, iterator = heapq.heappop(heap)
        result.append(value)
        
        # Намагаємося отримати наступний елемент з того ж ітератора
        try:
            next_value = next(iterator)
            heapq.heappush(heap, (next_value, list_idx, iterator))
        except StopIteration:
            continue
    
    return result

def merge_two_sorted_lists(list1: List[int], list2: List[int]) -> List[int]:
    """
    Злиття двох відсортованих списків (базовий випадок).
    
    Args:
        list1, list2: Відсортовані списки
        
    Returns:
        List[int]: Об'єднаний відсортований список
    """
    result = []
    i = j = 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    
    # Додаємо залишкові елементи
    result.extend(list1[i:])
    result.extend(list2[j:])
    
    return result

def merge_k_lists_divide_and_conquer(lists: List[List[int]]) -> List[int]:
    """
    Реалізація через підхід "розділяй та володарюй".
    
    Args:
        lists (List[List[int]]): Список відсортованих списків
        
    Returns:
        List[int]: Об'єднаний відсортований список
    """
    if not lists:
        return []
    if len(lists) == 1:
        return lists[0]
    
    # Рекурсивно ділимо списки навпіл
    mid = len(lists) // 2
    left = merge_k_lists_divide_and_conquer(lists[:mid])
    right = merge_k_lists_divide_and_conquer(lists[mid:])
    
    return merge_two_sorted_lists(left, right)

def demonstrate_algorithm_step_by_step(lists: List[List[int]]):
    """
    Демонструє алгоритм покроково.
    
    Args:
        lists (List[List[int]]): Список відсортованих списків
    """
    print(f"📥 Вхідні списки: {lists}")
    
    if not lists:
        print("✅ Порожній вхід - повертаємо порожній список")
        return []
    
    non_empty_lists = [lst for lst in lists if lst]
    if not non_empty_lists:
        print("✅ Всі списки порожні - повертаємо порожній список")
        return []
    
    print(f"📊 Фільтровані списки: {non_empty_lists}")
    
    # Ініціалізація
    heap = []
    for list_idx, lst in enumerate(non_empty_lists):
        if lst:
            heapq.heappush(heap, (lst[0], list_idx, 0))
    
    print(f"🏗️  Початкова купа: {heap}")
    
    result = []
    step = 1
    
    while heap:
        value, list_idx, element_idx = heapq.heappop(heap)
        result.append(value)
        
        print(f"   Крок {step}: Витягуємо {value} зі списку {list_idx}")
        print(f"            Результат поки що: {result}")
        
        if element_idx + 1 < len(non_empty_lists[list_idx]):
            next_value = non_empty_lists[list_idx][element_idx + 1]
            heapq.heappush(heap, (next_value, list_idx, element_idx + 1))
            print(f"            Додаємо {next_value} до купи")
        else:
            print(f"            Список {list_idx} вичерпано")
        
        print(f"            Купа: {sorted(heap)}")
        print()
        step += 1
    
    print(f"✅ Фінальний результат: {result}")
    return result

def benchmark_approaches(lists: List[List[int]]):
    """
    Порівнює різні підходи до злиття списків.
    
    Args:
        lists (List[List[int]]): Список відсортованих списків
    """
    import time
    
    print(f"\n⚡ Бенчмарк для {len(lists)} списків")
    
    # Підхід з купою
    start = time.time()
    result_heap = merge_k_lists(lists)
    time_heap = time.time() - start
    
    # Підхід з ітераторами
    start = time.time()
    result_iterators = merge_k_lists_with_iterators(lists)
    time_iterators = time.time() - start
    
    # Підхід "розділяй та володарюй"
    start = time.time()
    result_divide = merge_k_lists_divide_and_conquer(lists)
    time_divide = time.time() - start
    
    # Наївний підхід (злиття по черзі)
    start = time.time()
    result_naive = []
    for lst in lists:
        result_naive = merge_two_sorted_lists(result_naive, lst)
    time_naive = time.time() - start
    
    print(f"   🏗️  Купа:              {time_heap:.6f}s")
    print(f"   🔄 Ітератори:         {time_iterators:.6f}s")
    print(f"   ⚡ Розділяй-володарюй: {time_divide:.6f}s")
    print(f"   📈 Наївний:           {time_naive:.6f}s")
    
    # Перевіряємо, що всі результати однакові
    assert result_heap == result_iterators == result_divide == result_naive
    print(f"   ✅ Всі підходи дають однаковий результат")

def test_algorithm():
    """Тестує алгоритм на різних прикладах"""
    print("🧪 ТЕСТУВАННЯ АЛГОРИТМУ")
    print("=" * 50)
    
    test_cases = [
        # Основний приклад з завдання
        [[1, 4, 5], [1, 3, 4], [2, 6]],
        
        # Різні випадки
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],  # Без перетинів
        [[1, 3, 5], [2, 4, 6]],             # Чергування
        [[1], [2], [3]],                     # По одному елементу
        [[], [1, 2], [3, 4]],               # З порожнім списком
        [[1, 1, 1], [2, 2, 2]],             # З дублікатами
        [[5, 4, 3], [2, 1]],                # Не відсортовані (для тесту)
        [[]],                                # Тільки порожній список
        [],                                  # Порожній вхід
        [[1, 10, 100], [2, 20], [3, 30, 300, 3000]]  # Різні розміри
    ]
    
    for i, lists in enumerate(test_cases, 1):
        print(f"\n📊 Тест {i}: {lists}")
        
        # Перевіряємо, чи всі списки відсортовані
        all_sorted = all(lst == sorted(lst) for lst in lists)
        if not all_sorted:
            print("   ⚠️  Увага: Не всі списки відсортовані!")
        
        result = merge_k_lists(lists)
        print(f"   Результат: {result}")
        
        # Перевіряємо правильність
        expected = sorted([item for sublist in lists for item in sublist])
        if result == expected:
            print("   ✅ Правильно!")
        else:
            print(f"   ❌ Помилка! Очікувалося: {expected}")

def analyze_complexity():
    """Аналізує складність алгоритму"""
    print("\n📈 АНАЛІЗ СКЛАДНОСТІ АЛГОРИТМУ")
    print("=" * 40)
    print("Позначення:")
    print("  • k - кількість списків")
    print("  • n - загальна кількість елементів")
    print("\nПідхід з купою:")
    print("  • Часова складність: O(n log k)")
    print("  • Просторова складність: O(k)")
    print("  • Купа містить максимум k елементів")
    print("  • n операцій вставки/видалення з купи розміру k")
    print("\nПорівняння з іншими підходами:")
    print("  • Наївний (послідовне злиття): O(kn)")
    print("  • Розділяй-володарюй: O(n log k)")
    print("  • Сортування всіх елементів: O(n log n)")

def main():
    """Головна функція демонстрації"""
    print("🔗 ДОДАТКОВЕ ЗАВДАННЯ: ЗЛИТТЯ K ВІДСОРТОВАНИХ СПИСКІВ")
    print("=" * 70)
    print("Використання мінімальної купи для ефективного злиття")
    
    # Основний приклад з завдання
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    print(f"\n🎯 Основний приклад: {lists}")
    
    merged_list = merge_k_lists(lists)
    print(f"Відсортований список: {merged_list}")
    
    # Детальна демонстрація
    print(f"\n" + "=" * 70)
    print("🔍 ДЕТАЛЬНА ДЕМОНСТРАЦІЯ АЛГОРИТМУ")
    demonstrate_algorithm_step_by_step(lists)
    
    # Тестування
    test_algorithm()
    
    # Бенчмарк
    print(f"\n" + "=" * 70)
    print("⚡ ПОРІВНЯННЯ ПРОДУКТИВНОСТІ")
    
    # Малий тест
    small_lists = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    benchmark_approaches(small_lists)
    
    # Більший тест
    big_lists = [list(range(i, 100, 10)) for i in range(10)]
    benchmark_approaches(big_lists)
    
    # Аналіз складності
    analyze_complexity()
    
    print(f"\n🎉 Додаткове завдання виконано успішно!")

if __name__ == "__main__":
    main()
