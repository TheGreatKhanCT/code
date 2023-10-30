people = {
'htanaka': 'Haru Tanaka',
'ppatel': 'Priya Patel',
'bagarcia': 'Benjamin Alberto Garcia',
'zmin': 'Zhang Min',
'afarooqi': 'Ayesha Farooqi',
'hajackson': 'Hanna Jackson',
'papatel': 'Pratyush Aarav Patel',
'hrjackson': 'Henry Jackson'
}
how_many = len(people)
print(how_many)
print("hajackson" in people)
person = "bagarcia"
print(people.get(person))
people.update({"hrjackson": "Henrietta Jackson"})   #update from henry jackson to henrietta jackson
print(people)
people.update({"wwiggins": "Wanda Wiggins"})    #this adds a new key value

for i in people.keys():                         #display the content of the dictionary with the new and updated values
    print(f"{i} = {people[i]}")
for j in people:
    print(people[j])
for k in people.values():
    print(k)
for key, value in people.items():
    print(key, "=", value)              #shows the key and value with a = in between

peeps2 = people.copy()                  #copy of the dictionary
print(peeps2)
del peeps2["zmin"]                      #delete zmin from the dictionary
print(peeps2)
peeps3 = people.copy()
peeps3.clear()
print(peeps3)

product = {
'name' : 'Ray-Ban Wayfarer Sunglasses',
'unit_price' : 112.99,
'taxable' : True,
'in_stock' : 10,
'models' : ['Black', 'Tortoise']
}
print('Name: ', product['name'])
print('Price: ', f"${product['unit_price']:.2f}")
print('Taxable: ', product['taxable'])
print('In Stock:', product['in_stock'])
print('Models:')
for model in product['models']:
    print(" " * 10 + model)         #*10 means print a space " " ten times

new_product = {         #create generic dictionary for new products
    "name": "",
    "unit_price": 0,
    "taxable": True,
    "in_stock": 0,
    "models": []
}
DWC001 = dict.fromkeys(new_product.keys())  #create dictionary named DWC001 that has the same keys as new_product
DWC001.setdefault("taxable", True)
DWC001.setdefault("models",[])
DWC001.setdefault("reorder_point",100)
print("Dictioonary after fromkeys() and setdefault()")
print(DWC001)
print("\nDictionary after fromkeys() and setdefault()")     #change taxable field from None to True
DWC001["taxable"] = True
print(DWC001)