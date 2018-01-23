#Nested Dictionary
user={
    'zain':{
      'firstname':'zain',
      'lastname':'khan',
      'location':'karachi',
    },
    'john':{
        'firstname':'john',
        'lastname':'aston',
        'location':'california',
    }
}

for username, user_info in user.items():
    print("\nUsername: "+username.title())
    fullname = user_info['firstname']+""+user_info['lastname']
    location = user_info['location']
    print("\tFullname: "+fullname.title())
    print("\tlocation: "+location.title())