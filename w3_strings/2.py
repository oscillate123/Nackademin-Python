string = "google.com"

unique = []

for char in string:
    if char not in unique:
        unique.append(char)

unique = "".join(unique)
print("\n")
print(f" Unique chars:\n {unique}")

count = {}

for i in string:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print("\n")
print(" Character count:" + "\n" + str(count).replace(",", "\n").replace("{"," ").replace("}"," "))
