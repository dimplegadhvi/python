#deldte elements from a dictionary
a={'name':'john','age':20,9:56,7:90}
print(a)

del(a[9])
print(a)

print(a.popitem())
print(a)

a.clear()
print(a)
