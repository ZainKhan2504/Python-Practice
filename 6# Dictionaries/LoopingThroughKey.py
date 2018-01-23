favorite_languages = {'jen':'python',
                      'sarah':'C',
                      'edward':'ruby',
                      'phil':'python'}
friend = ['phil','sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friend:
        print("Hi"+name.title()+",I see your favorite lanuage is "+favorite_languages[name].title()+"!")