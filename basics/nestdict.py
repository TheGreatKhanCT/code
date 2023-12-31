#generic products dictionary to contain multiple product dictionaries
products = {
    "RB00111" : {"name": "Ray-Ban Sunglasses", "price": 112.98, "models": ["black", "tortoise"]},
    "DWC0317" : {"name": "Drone With Camera", "price": 72.95, "models": ["white", "black"]},
    "MTS0540" : {"name": "T-shirt", "price": 2.95, "models": ["small", "medium", "large"]},
    "ECD2989" : {"name": "Echo Dot", "price": 29.99, "models": []}
}
#this header shows the output
print(f'{"ID":<6} {" Name":<17} {"Price":>8} {"Models"}')
print('-' * 60) #prints 60 hyphens
#loop through each dictionary in the products dictionary
for oneproduct in products.keys():
    #get the id of one product
    id = oneproduct
    #get the name of one product
    name = products[oneproduct]['name']
    #get the unit price of one product and format with $
    unit_price = '$' + f"{products[oneproduct]['price']:,.2f}"
    #create an empty string variable named models
    models = ""
    #loop though models list and tack onto models / one item from the list followed by a comma and a space
    for m in products[oneproduct]['models']:
        models += m + ', '
    #if the models variable is more than 2 char in length, peel off the last 2 chars (last comma and space)
    if len(models) > 2:
        models = models[:-2]
    else:
        #otherwise, if no models, show <none>
        models = '<none>'
    #print all the variables with a neat f-string
    print(f"{id:<6} {name:<17} {unit_price:>8} {models}")
#any unindented code down here executed after the loop completes