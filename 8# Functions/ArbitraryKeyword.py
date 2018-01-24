def build_profile(firstname,lastname,**userinfo):
    profile = {}
    profile['firstname'] = firstname
    profile['lastname'] = lastname
    for key, value in userinfo.items():
        profile[key] = value
    return profile

user_profile=build_profile('Zain','Khan',location='karachi',field='BSE')
print(user_profile)