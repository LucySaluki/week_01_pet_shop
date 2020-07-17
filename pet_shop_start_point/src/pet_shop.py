# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

# Test 2 - get total cash from pet shop 
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

# Test 3 and 4 - add or remove cash and get the total again
def add_or_remove_cash(pet_shop,amount):
    pet_shop["admin"]["total_cash"]=pet_shop["admin"]["total_cash"]+ amount

# Test 5 - check the number of pets sold
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

# Test 6 - increase the number of pets_sold
def increase_pets_sold(pet_shop, number_of_pets):
    pet_shop["admin"]["pets_sold"]=pet_shop["admin"]["pets_sold"] + number_of_pets
    return pet_shop["admin"]["pets_sold"]

# Test 7 - get stock count
def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

# Test 8 and 9 - get count of pet breeds
def get_pets_by_breed(pet_shop, breed_type):
    pets_list=[]
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed_type:
            pets_list.append(pet) 
    return pets_list

# Test 10 and 11 - find pet by name
def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet

# Test 12 - remove pet from list
def remove_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            pet_shop["pets"].remove(pet)

#  Test 13 - add pet to stock
def add_pet_to_stock(pet_shop,new_pet):
    pet_shop["pets"].append(new_pet)

# Test 14 - get customer cash
def get_customer_cash(customer):
    return customer["cash"]

# Task 15 - remove cash from customer
def remove_customer_cash(customer, amount):
    customer["cash"]=customer["cash"]-amount

# Task 16 - customer pet count
def get_customer_pet_count(customer):
    return len(customer["pets"])

# Task 17 - add pet to customer
def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

# Optional extras
# Task 18 to 20 - check customer can afford
def customer_can_afford_pet(customer, pet):
    if pet["price"]<=customer["cash"]:
        return True
    else:
        return False
