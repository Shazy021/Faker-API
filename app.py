from fastapi import FastAPI
from modules.buyer_gen import fake_buyer
from modules.order_gen import fake_order, fake_user_order
from fastapi.param_functions import Body

app = FastAPI(
    title="Fake data",
    description="Generate fake data"
)


@app.get('/get_user', response_model=dict, summary="Generate fake user")
async def generate_user() -> dict:
    """
    Generate a fake buyers
    """
    return fake_buyer()


@app.post('/get_order', response_model=dict, summary="Generate fake random users order")
async def generate_order(input_data: dict[str, int] = Body(example={
    'max_users_id': 256,
    'max_products_id': 2020,
    'min_buyers_id': 255,
    'min_products_id': 2016,
    'max_items': 4
})) -> dict:
    """
    Generate a fake order with specified parameters
    """
    max_users_id, max_products_id = input_data['max_users_id'], input_data['max_products_id']
    min_buyers_id = input_data.get('min_buyers_id', 0)
    min_products_id = input_data.get('min_products_id', 0)
    max_items = input_data.get('max_items', 25)

    return fake_order(
        max_users_id,
        max_products_id,
        min_buyers_id,
        min_products_id,
        max_items
    )


@app.post('/get_user_order', response_model=dict, summary="Generate fake order for buyer")
async def generate_user_order(input_data: dict[str, int] = Body(example={
    'user_id': 1,
    'max_products_id': 5,
    'min_products_id': 0,
    'max_items': 4
})) -> dict:
    """
    Generate a fake order for specified user.
    """
    user_id, max_products_id = input_data['user_id'], input_data['max_products_id']
    min_products_id = input_data.get('min_products_id', 0)
    max_items = input_data.get('max_items', 25)

    return fake_user_order(
        user_id,
        max_products_id,
        min_products_id,
        max_items
    )
