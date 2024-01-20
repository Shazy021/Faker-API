# Faker-API
This is API to generate fake data using FastAPI.

## Installation
1. Clone the repository:

```
git clone https://github.com/Shazy021/Faker-API.git
```

2. You can change the IP address or port in `docker-compose` and `Dokerfile` files:
    * In docker-compose.yml you can change port `ports:- "8010:80"`
    * In Dockerfile yo can change uvicorn parameters:
```
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80", "--workers","4"]
```

3. Docker compose:
```
docker-compose up
```

The API will be accessible at http://localhost:8010

## Endpoints
### 1. Generate Fake User

- Method: GET
- Route: /get_user
- Description: Generates a fake user.
- Response: A dictionary representing the generated fake user data.

### 2. Generate Fake Random Users Order

- Method: POST
- Route: /get_order
- Description: Generates a fake random order with specified parameters.
- Request Parameters:
  - max_users_id (required, int): Maximum user ID.
  - max_products_id (required, int): Maximum product ID.
  - min_buyers_id (optional, int): Minimum buyer ID (default: 0).
  - min_products_id (optional, int): Minimum product ID (default: 0).
  - max_items (optional, int): Maximum number of items in the order (default: 25).
- Response: A dictionary representing the generated fake order data.

### 3. Generate Fake User's Order
- Method: POST
- Route: /get_user_order
- Description: Generates a fake order for a specified user.
- Request Parameters:
  - user_id (required, int): User ID.
  - max_products_id (required, int): Maximum product ID.
  - min_products_id (optional, int): Minimum product ID (default: 0).
  - max_items (optional, int): Maximum number of items in the order (default: 25).
- Response: A dictionary representing the generated fake order data for the specified user.
---
## Examples
### 1. Generate Fake User

- Method: GET
- URL: http://localhost:8010/get_user
- Response:
```
{
  "longitude": "133.584761",
  "latitude": "-57.7149335",
  "place": "Queenstown",
  "region": "Tasmania"
}
```
---
### 2. Generate Fake Random User's Order

- Method: POST
- URL: http://localhost:8010/get_order
- Request Body:
```
{
  "max_users_id": 256,
  "max_products_id": 2020,
  "min_buyers_id": 255,
  "min_products_id": 2016,
  "max_items": 4
}
```
- Response:
```
{
  "buyer_id": 256,
  "item_ids": [
    2020,
    2016,
    2019
  ],
  "time": "19-01-2024 00:55:45"
}
```
---
### 3. Generate Fake User's Order

- Method: POST
- URL: http://localhost:8010/get_user_order
- Request Body:
```
{
  "user_id": 1,
  "max_products_id": 5,
  "min_products_id": 0,
  "max_items": 4
}
```
- Response:
```
{
  "buyer_id": 1,
  "item_ids": [
    1,
    1,
    2
  ],
  "time": "19-01-2024 02:02:50"
}
```
