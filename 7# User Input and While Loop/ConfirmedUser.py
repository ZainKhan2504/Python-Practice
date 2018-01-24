unconfirmed_user = ['alice','brian','candace']
confirmed_user = []
while unconfirmed_user:
    user = unconfirmed_user.pop()
    print("The verified user are: "+user.title())
    confirmed_user.append(user)
print("\nConfirmed user are:")
for confirmed_user in confirmed_user:
    print(confirmed_user)