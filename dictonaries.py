profile = {
    "name" : "nikhil" ,
    "age" : "20" ,
    "gender" : "male"

}
print(profile["age"])
profile ['age'] = '21'
print(profile)
print(profile.get("name"))
print(profile.get("color")) # sice no color retuns none
print(profile.get("color" , "black"))
# we can set a default value so that if no volor present it returns black
profile["favourite food"] = "pizza"
del profile['age']
print(profile)