distinct_substrings = set()

s = input("Enter String : ")

for i in range(len(s)+1):
    for j in range(1,len(s)+1):
        distinct_substrings.add(s[i:j])

print(distinct_substrings)
