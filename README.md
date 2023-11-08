
# FastAPI Order Service

This is a basic template for a FastAPI order service, allowing users to create orders and manage them through HTTP requests. The service includes endpoints for creating users, creating orders, canceling orders, deleting orders, and retrieving order information.

## Prerequisites

- Python 3.7 or higher
- FastAPI
- Uvicorn

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/VadimS077/Simple_FastApi_Project.git 
   ```

2. Navigate to the project directory:

   ```shell
   cd Simple_FastApi_Project
   ```

3. Create a virtual environment (optional):

   ```shell
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install the required dependencies:

   ```shell
   pip install uvicorn  
pip install fastapi  
pip install pydantic
   ```

## Usage

1. Start the FastAPI server:

   ```shell
   uvicorn main:app --reload
   ```

2. Open your web browser and go to [http://localhost:8080/docs](http://localhost:8080/docs) to access the Swagger UI. The Swagger UI provides an interactive interface for testing the API endpoints.

3. Use the Swagger UI to test the following endpoints:

   - POST `/users`: Create a new user by providing the user's name in the request body.
   - GET `/users/{user_id}`: Retrieve the user's ID and name by specifying the user ID in the path parameter.
   - POST `/orders`: Create a new order by providing the user ID, product name, and product count in the request body.
   - PATCH `/orders/{order_id}`: Cancel an order by specifying the order ID in the path parameter.
   - DELETE `/orders/{order_id}`: Delete an order by specifying the order ID in the path parameter.
   - GET `/orders/{order_id}`: Retrieve the product count of products based on the order ID, product name, and cancellation status.

