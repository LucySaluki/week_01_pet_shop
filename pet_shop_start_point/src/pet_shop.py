# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

# Test 1 - get total cash from pet shop 
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

# Test 2 - add or remove cash and get the total again
def add_or_remove_cash(pet_shop,amount):
    pet_shop["admin"]["total_cash"]=pet_shop["admin"]["total_cash"]+ amount
    
