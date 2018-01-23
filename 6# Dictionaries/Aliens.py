#Make an empty list for storing aliens
aliens = []

#Make 30 green lines
for alien_num in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

#Show the first five aliens
for alien in aliens[:5]:
    print(alien)
print("...")

#Show ho many aliens have been created
print("Total number of aliens: "+str(len(aliens)))
