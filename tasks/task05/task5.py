def new_user(nm, sn, age=42, **ext):
    return {"name": nm, "surname": sn, "age": age, "extra": ext}


assert new_user("Marie", "Curie", age=66, occupation="physicist", won_nobel=True) == \
    {
       "name": "Marie",
       "surname": "Curie",
       "age": 66,
       "extra": {
           "occupation": "physicist",
           "won_nobel": True
       }
    }, "test error"

assert new_user("Bill", "Gates", age=65) == \
   {
       "name": "Bill",
       "surname": "Gates",
       "age": 65,
       "extra": {}
   }

assert new_user("John", "Doe") == \
   {
       "name": "John",
       "surname": "Doe",
       "age": 42,
       "extra": {}
   }