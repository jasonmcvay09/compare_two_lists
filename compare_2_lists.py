a = [1,2,6,3,2,7,8,9,44]
b = [1,2,55,2,22,7,123,9,44]
addition = [i for i in b if i not in a]
missing = [i for i in a if i not in b]

print(addition)
print(missing)
