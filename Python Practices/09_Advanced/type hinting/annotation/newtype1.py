from typing import NewType

UserId = NewType("UserId", int)

user_id = UserId(123456)
print(user_id)
print(type(user_id))

user_id = UserId("123456")
print(user_id)
print(type(user_id))

user_id = UserId(123456)
print(user_id)
print(type(user_id))
