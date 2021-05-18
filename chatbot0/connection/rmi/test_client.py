import RMIClient

uri = "PYRO:obj_18708f72719542f7a1b59b13b45e49e8@localhost:51218"

c = client.Client(uri)
remote_object = c.connect()

# print(remote_object)

# print(remote_object)
response = remote_object.diagnose("symptoms")
print(response)
