a = {
"key": "value",
"name": "John",
"marks": "100",
"list": [1, 2, 9]
}
# print(a["key"])
# print(a["list"])

print(a.items())
print(a.keys())
print(a.update({"name":"Nate"}))
print(a.get("name"))