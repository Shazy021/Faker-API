from datetime import datetime
import random
from random import randint


def random_times() -> str:
    """
    Returns a random time as a formatted string.

    :return: A string with the current date and random time in the format '%d-%m-%Y HH:MM:SS'.
    """
    return datetime.now().strftime(f'%d-%m-%Y {randint(0, 23):02d}:{randint(0, 59):02d}:{randint(0, 59):02d}')


def fake_order(max_buyers_id: int,
               max_products_id: int,
               min_buyers_id: int = 0,
               min_products_id: int = 0,
               max_items: int = 25) -> dict:
    """
    Creates a fake order object.

    :param max_buyers_id: Maximum buyer ID.
    :param max_products_id: Maximum product ID.
    :param min_buyers_id: Minimum buyers ID. Defaults to 0.
    :param min_products_id: Minimum products ID. Defaults to 0.
    :param max_items: Maximum number of items in the order. Defaults to 25.
    :return: Fake order object with random values within the specified limits.
    """
    items_count = random.randint(1, max_items)

    order = {
        'buyer_id': random.randint(min_buyers_id, max_buyers_id),
        'item_ids': [random.randint(min_products_id, max_products_id) for _ in range(items_count)],
        'time': random_times()
    }
    return order


def fake_user_order(user_id: int,
                    max_products_id: int,
                    min_products_id: int = 0,
                    max_items: int = 25) -> dict:
    """
    Creates a fake order object for a specific user.

    :param user_id: User ID.
    :param max_products_id: Maximum product ID.
    :param min_products_id: Minimum buyers ID. Defaults to 0.
    :param max_items: Maximum number of items in the order. Defaults to 25.
    :return: Fake order object with random values for specified user.
    """
    order = {
        'buyer_id': user_id,
        'item_ids': [random.randint(min_products_id, max_products_id) for _ in range(random.randint(1, max_items))],
        'time': random_times()
    }
    return order
