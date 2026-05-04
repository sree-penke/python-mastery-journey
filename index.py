from collection import namedtuple

User = namedtuple("User",["name","role","age"])
user = User("sree","admin",25)

print(user.name)
print(user.role)
print(user.age)
print(type(user))      # what type is it?
print(user[0])  