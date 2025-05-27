#!/usr/bin/env python3
"""
Скрипт для запуску всіх завдань домашнього завдання #8
Купи (піраміди)
"""

import sys
import time
import traceback

def run_task(task_name, task_function):
    """
    Запускає окреме завдання з обробкою помилок
    
    Args:
        task_name (str): Назва завдання
        task_function (callable): Функція для виконання
    
    Returns:
        bool: True якщо завдання виконано успішно, False інакше
    """
    print(f"\n{'='*70}")
    print(f"🚀 {task_name}")
    print(f"{'='*70}")
    
    try:
        start_time = time.time()
        task_function()
        end_time = time.time()
        
        execution_time = end_time - start_time
        print(f"\n✅ {task_name} виконано успішно!")
        print(f"⏱️  Час виконання: {execution_time:.3f} секунд")
        return True
        
    except Exception as e:
        print(f"\n❌ Помилка в {task_name}:")
        print(f"   {str(e)}")
        print("\nДетальна інформація про помилку:")
        traceback.print_exc()
        return False

def task1_main():
    """Запуск основного завдання: З'єднання кабелів"""
    try:
        import task1
        if hasattr(task1, 'main'):
            task1.main()
        else:
            # Якщо функція main відсутня, виконуємо базову демонстрацію
            print("Функція main() не знайдена, запускаємо базову демонстрацію...")
            from task1 import minimize_cable_connection_cost_simple
            
            # Тестові випадки
            test_cases = [
                [4, 3, 2, 6],
                [1, 2, 3, 4, 5],
                [10, 20, 30]
            ]
            
            for cables in test_cases:
                cost = minimize_cable_connection_cost_simple(cables)
                print(f"Кабелі {cables}: мінімальна вартість = {cost}")
                
    except ImportError:
        print("❌ Файл task1.py не знайдено")
        raise

def task2_main():
    """Запуск додаткового завдання: Злиття k списків"""
    try:
        import task2
        if hasattr(task2, 'main'):
            task2.main()
        else:
            # Якщо функція main відсутня, виконуємо базову демонстрацію
            print("Функція main() не знайдена, запускаємо базову демонстрацію...")
            from task2 import merge_k_lists
            
            # Основний приклад з завдання
            lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
            merged_list = merge_k_lists(lists)
            print(f"Списки: {lists}")
            print(f"Відсортований список: {merged_list}")
            
    except ImportError:
        print("❌ Файл task2.py не знайдено")
        print("💡 Додаткове завдання є опціональним, пропускаємо...")
        return

def demo_heaps_usage():
    """Демонстрація основних можливостей модуля heapq"""
    import heapq
    
    print("📚 ДЕМОНСТРАЦІЯ РОБОТИ З КУПАМИ (heapq)")
    print("=" * 50)
    
    # Базові операції з купою
    print("\n🏗️  Базові операції:")
    data = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"Початкові дані: {data}")
    
    heapq.heapify(data)
    print(f"Після heapify: {data}")
    
    print(f"Мінімальний елемент: {data[0]}")
    
    min_elem = heapq.heappop(data)
    print(f"Витягнули мінімум: {min_elem}, купа тепер: {data}")
    
    heapq.heappush(data, 0)
    print(f"Додали 0: {data}")
    
    # n найменших/найбільших елементів
    print(f"\n📊 Корисні функції:")
    original = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(f"Дані: {original}")
    print(f"3 найменші: {heapq.nsmallest(3, original)}")
    print(f"3 найбільші: {heapq.nlargest(3, original)}")

def performance_comparison():
    """Порівняння продуктивності різних підходів"""
    import random
    
    print("\n⚡ ПОРІВНЯННЯ ПРОДУКТИВНОСТІ")
    print("=" * 40)
    
    # Генеруємо тестові дані
    sizes = [100, 1000, 5000]
    
    for size in sizes:
        print(f"\n📊 Тест для {size} елементів:")
        
        # Тест для завдання 1 (з'єднання кабелів)
        cables = [random.randint(1, 100) for _ in range(size)]
        
        try:
            from task1 import minimize_cable_connection_cost_simple
            
            start = time.time()
            cost = minimize_cable_connection_cost_simple(cables)
            heap_time = time.time() - start
            
            print(f"   🔌 З'єднання кабелів (купа): {heap_time:.4f}s, вартість: {cost}")
            
        except ImportError:
            print("   🔌 task1.py не знайдено")
        
        # Тест для завдання 2 (злиття списків)
        k = min(10, size // 10)  # Кількість списків
        if k > 0:
            lists = []
            for _ in range(k):
                sublist = sorted([random.randint(1, 1000) for _ in range(size // k)])
                lists.append(sublist)
            
            try:
                from task2 import merge_k_lists
                
                start = time.time()
                result = merge_k_lists(lists)
                merge_time = time.time() - start
                
                print(f"   🔗 Злиття {k} списків (купа): {merge_time:.4f}s, елементів: {len(result)}")
                
            except ImportError:
                print("   🔗 task2.py не знайдено")

def main():
    """Головна функція для запуску всіх завдань"""
    print("🏗️ ДОМАШНЄ ЗАВДАННЯ #8: КУПИ (ПІРАМІДИ)")
    print("Виконання всіх завдань")
    print("=" * 70)
    
    # Демонстрація роботи з купами
    demo_heaps_usage()
    
    # Список завдань для виконання
    tasks = [
        ("ОСНОВНЕ ЗАВДАННЯ: Мінімізація витрат на з'єднання кабелів", task1_main),
        ("ДОДАТКОВЕ ЗАВДАННЯ: Злиття k відсортованих списків", task2_main)
    ]
    
    results = []
    total_start_time = time.time()
    
    # Виконуємо всі завдання
    for task_name, task_function in tasks:
        success = run_task(task_name, task_function)
        results.append((task_name, success))
        
        # Пауза між завданнями для зручності перегляду
        if success and task_name != tasks[-1][0]:
            try:
                input("\n⏸️  Натисніть Enter для продовження до наступного завдання...")
            except KeyboardInterrupt:
                print("\n\n⚠️  Виконання перервано користувачем")
                break
        elif not success:
            # При помилці питаємо чи продовжувати
            try:
                user_choice = input("\n❓ Продовжити виконання інших завдань? (y/n): ")
                if user_choice.lower() not in ['y', 'yes', 'так', 'т']:
                    break
            except KeyboardInterrupt:
                print("\n\n⚠️  Виконання перервано користувачем")
                break
    
    # Порівняння продуктивності
    if any(result[1] for result in results):  # Якщо хоча б одне завдання виконалось
        try:
            input("\n⏸️  Натисніть Enter для запуску тестів продуктивності...")
            performance_comparison()
        except KeyboardInterrupt:
            pass
    
    total_end_time = time.time()
    total_time = total_end_time - total_start_time
    
    return results[0][1] if results else False  # Повертаємо результат основного завдання

def interactive_mode():
    """Інтерактивний режим вибору завдань"""
    print("🔄 ІНТЕРАКТИВНИЙ РЕЖИМ")
    print("Виберіть завдання для виконання:")
    print("1. Основне завдання: З'єднання кабелів")
    print("2. Додаткове завдання: Злиття k списків")
    print("3. Демонстрація heapq")
    print("4. Тести продуктивності")
    print("5. Виконати всі завдання")
    print("0. Вихід")
    
    tasks_map = {
        '1': ("ОСНОВНЕ ЗАВДАННЯ", task1_main),
        '2': ("ДОДАТКОВЕ ЗАВДАННЯ", task2_main),
        '3': ("ДЕМОНСТРАЦІЯ HEAPQ", demo_heaps_usage),
        '4': ("ТЕСТИ ПРОДУКТИВНОСТІ", performance_comparison),
        '5': ("ВСІ ЗАВДАННЯ", main)
    }
    
    while True:
        try:
            choice = input("\nВаш вибір (0-5): ").strip()
            
            if choice == '0':
                print("👋 До побачення!")
                break
            elif choice in tasks_map:
                task_name, task_function = tasks_map[choice]
                if choice == '5':
                    task_function()
                    break
                else:
                    if choice in ['3', '4']:
                        # Для демонстрацій не потрібна обробка помилок
                        print(f"\n🚀 {task_name}")
                        print("="*50)
                        task_function()
                    else:
                        run_task(task_name, task_function)
            else:
                print("❌ Невірний вибір. Спробуйте ще раз.")
                
        except KeyboardInterrupt:
            print("\n\n⚠️  Програма перервана користувачем")
            break
        except EOFError:
            print("\n\n👋 До побачення!")
            break

if __name__ == "__main__":
    print("🏗️ Домашнє завдання #8: Купи (піраміди)")
    print("=" * 50)
    
    # Перевіряємо аргументи командного рядка
    if len(sys.argv) > 1:
        if sys.argv[1] == "--interactive" or sys.argv[1] == "-i":
            interactive_mode()
        elif sys.argv[1] == "--demo":
            demo_heaps_usage()
        elif sys.argv[1] == "--performance":
            performance_comparison()
        elif sys.argv[1] == "--help" or sys.argv[1] == "-h":
            print("Використання:")
            print("  python3 run_all.py              # Виконати всі завдання")
            print("  python3 run_all.py -i           # Інтерактивний режим")
            print("  python3 run_all.py --demo       # Демонстрація heapq")
            print("  python3 run_all.py --performance # Тести продуктивності")
            print("  python3 run_all.py --help       # Показати цю довідку")
        else:
            print(f"❌ Невідомий аргумент: {sys.argv[1]}")
            print("Використайте --help для довідки")
    else:
        # Запускаємо всі завдання за замовчуванням
        try:
            success = main()
            sys.exit(0 if success else 1)
        except KeyboardInterrupt:
            print("\n\n⚠️  Виконання перервано користувачем")
            sys.exit(1)
