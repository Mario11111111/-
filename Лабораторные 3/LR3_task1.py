def find_item_index(items, item_to_find):
    """
    Функция для поиска индекса первого вхождения товара в списке.
    :param items: Список товаров
    :param item_to_find: Товар, который нужно найти
    :return: Индекс первого вхождения товара или None, если товар не найден
    """
    if item_to_find in items:
        return items.index(item_to_find)
    return None
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
for find_item in ['банан', 'груша', 'персик']:
    index_item = find_item_index(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")