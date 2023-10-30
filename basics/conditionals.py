total = 100
sales_tax_rate = .065
taxable = True
if taxable:
    print(f"Subtotal : ${total:.2f}") #.2f here is fixed 2 decimals, use correct spacing to align the numbers neatly
    sales_tax = total * sales_tax_rate
    print(f"Sales Tax: ${sales_tax:.2f}")
    total = total + sales_tax
print(f"Total   :  ${total:.2f}")
