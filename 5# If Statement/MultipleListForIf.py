available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']

for request_toppings in requested_toppings:
    if request_toppings in available_toppings:
        print("Adding "+request_toppings+".")
    else:
        print("Sorry, we don't have "+request_toppings+".")
print("\nFinished making your pizza!")