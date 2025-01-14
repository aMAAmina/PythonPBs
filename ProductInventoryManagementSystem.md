## The problem covers (Dictionaries, JSON)
You are tasked with building a product inventory management system for an e-commerce store. The store provides its inventory data in JSON format, and you need to manipulate this data to perform the following tasks:

## Input Json
The store inventory is provided as a JSON string:
`{
  "products": [
    {"id": 101, "name": "Laptop", "price": 800, "quantity": 10},
    {"id": 102, "name": "Headphones", "price": 50, "quantity": 30},
    {"id": 103, "name": "Mouse", "price": 25, "quantity": 50},
    {"id": 104, "name": "Keyboard", "price": 40, "quantity": 20}
  ]
}`

## Tasks:
1. Load the JSON data into a Python dictionary.
2. Find the total inventory value for the store. The inventory value of each product is calculated as price * quantity.
3. Add a new product to the inventory. The product details are as follows:
`{"id": 105, "name": "Monitor", "price": 150, "quantity": 15}`
4. Remove a product from the inventory by its id. Remove the product with id = 103.
5. Save the updated inventory back to a JSON file named updated_inventory.json.

## Output:
1. Print the total inventory value.
2. Print the updated inventory after adding and removing products.
3. Save the final inventory to updated_inventory.json.
