requested_topping = ['mushrooms','extra cheese']
for request_topping in requested_topping:
    if request_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding "+request_topping+".")
print("Finished making you pizza!")