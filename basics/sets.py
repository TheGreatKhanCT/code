sample_set = {1.98,98.9,74.95,2.5,1,16.3}   #define a set
print(sample_set)
print(len(sample_set))
print(74.95 in sample_set)
sample_set.add(11.23)
sample_set.update([88,123.45,2.98])
print("\nLoop through set and print each item formatted")
for price in sample_set:
    print(f"{price:>6.2f}")