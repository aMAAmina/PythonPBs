import json

json_data = """{
                "products":
                [
                    {"id": 101, "name": "Laptop", "price": 800, "quantity": 10},
                    {"id": 102, "name": "Headphones", "price": 50, "quantity": 30},
                    {"id": 103, "name": "Mouse", "price": 25, "quantity": 50},
                    {"id": 104, "name": "Keyboard", "price": 40, "quantity": 20}
                ]
            }"""

#parse json to dict
inventory_dict_data = json.loads(json_data)
#calculate the total store inventory
total_store_inventory = 0
len = len(inventory_dict_data["products"])
i = 0
while i < len:
    total_store_inventory += inventory_dict_data["products"][i]["price"] * inventory_dict_data["products"][i]["quantity"]
    i += 1
#add a new product
new_prod = json.loads('{"id": 105, "name": "Monitor", "price": 150, "quantity": 15}')
inventory_dict_data["products"].append(new_prod)
#remove a product id = 103
i = 0
while i < len:
    if inventory_dict_data["products"][i]["id"] == 103:
        inventory_dict_data["products"].remove(inventory_dict_data["products"][i])
        break
    i += 1

def main():
    print("the total store inventory is: ", total_store_inventory)
    print("the updated inventory is ", inventory_dict_data)
    with open('updated_inventory.json','w') as fp:
        json.dump(inventory_dict_data, fp)

if __name__ == "__main__":
    main()
