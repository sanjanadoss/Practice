string = "geeks for geeks"
string = string.replace(" ", "")
ans_dict = {}
  
for i in string:
    if i in ans_dict:
        ans_dict[i] += 1
    else:
        ans_dict[i] = 1
print(ans_dict)

#counting occurance and printing them like w3s2a1
string = "geeks for geeks"
string = string.replace(" ", "")
ans_dict = {}
  
for i in string:
    if i in ans_dict:
        ans_dict[i] += 1
    else:
        ans_dict[i] = 1
for i in ans_dict:
    print("{}{}".format(i, ans_dict[i]), end="")

#count occurance in sorting order
string = "geeks for geeks"
string = string.replace(" ", "")
ans_dict = {}
for i in string:
    if i in ans_dict:
        ans_dict[i] += 1
    else:
        ans_dict[i] = 1
a = sorted(ans_dict.items(), key=lambda x: x[1])
for i in range(len(a)):
    print("{}".format(a[i]), end="")