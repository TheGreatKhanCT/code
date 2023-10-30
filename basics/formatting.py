import math
#variables, numerical values
unit_price = 49.99
quantity = 30
sales_tax_rate = .065  
subtotal = quantity * unit_price
sales_tax = sales_tax_rate * subtotal
total = subtotal + sales_tax

#Format amounts to show as string with leading dollar sign
s_subtotal = "$" + f"{subtotal:,.2f}"
s_sales_tax = "$" + f"{sales_tax:,.2f}"
s_total = "$" + f"{total:,.2f}"

#Output the string with the dollar sign attached and alignment of >9
#format with 3 quotation marks to make linebreakes cleaner instead of using n\
output = f"""
Subtotal:   {s_subtotal:>9} 
Sales Tax:  {s_sales_tax:>9}
Total:      {s_total:>9}
"""
print(output)
