import jsonpickle

###############################################
# Reading Payload
###############################################

class Thing(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
obj = Thing('Awesome')

###############################################
# Serializing object to JSON payload
###############################################

frozen = jsonpickle.encode(obj)

print("Serializing result")
print(frozen)

###############################################
#  Deserialization  JSON to object
###############################################
thawed = jsonpickle.decode(frozen)
print("Deserializing result")
print(thawed)

###############################################
# Handle Deserialization Error
###############################################


bad_payload = '''
        {
            "bad1": "print", 
            "bad2": "onData", 
            "bad3": "Madan Mohan",
            "py/object": "__main__.Thing"
        }
'''

print("Bad payload")
try:
  bad = jsonpickle.decode(bad_payload)
  print(bad)
except AttributeError:
  print("Deserialization failed")



