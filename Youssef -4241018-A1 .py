

print("\n\n                         BISM ALLAH ALRAHMAN ALRAHIM \n\n")
# 1
def lcm(a, b):
    if a == 0 or b == 0:
        return 0

    start = max(a, b)

    for i in range(start, a * b + 1):
        if i % a == 0 and i % b == 0:
            return i


print(lcm(6, 8))
print(lcm(4, 10))


# ****************************************************************
# 2
def d(text):
    t = {}
    for ch in text:
        if ch in t:
            t[ch] += 1
        else:
            t[ch] = 1
    return t


s = "Youssef love python  "
print(d(s))


# ****************************************************************
# 3
def SecLarg(lst):
    f = s = -10000000000000000

    for i in lst:
        if i > f:
            s = f
            f = i
        elif i > s and i != f:
            s = i
    return s


l = [1, 5, 9, 1, 10]
print(SecLarg(l))


# ****************************************************************
# 4
def sum_dig(n):
    total = 0
    while n > 0:
        a = n % 10
        n //= 10
        total += a
    return total


s = 300
print(sum_dig(s))

# ****************************************************************
#5
def passw(password):
    digit = False
    upper = False
    if len(password) >= 8:
        for ch in password:
            if ch >= '0' and ch <= '9':
                digit = True
            if ch >= 'A' and ch <= 'Z':
                upper = True
        
        if digit == True and upper == True:
            print("Strong")
        else:
            print("Weak")
        
passw("Hello123")
passw("hello123")


# ****************************************************************
#7
def remove_common(list1, list2):
    result = []

    for x in list1:
        found = False
        for y in list2:
            if x == y:
                found = True
                break
        if not found:
            result.append(x)

    for x in list2:
        found = False
        for y in list1:
            if x == y:
                found = True
                break
        if not found:
            result.append(x)

    return result


print(remove_common([1,2,3,4], [3,4,5,6]))

# ****************************************************************
#6
def Dict(lis1, lis2):
    dic =  {}
    for i in lis1:
        dic[i] = lis1[i]
        
    for i in lis2:
        if i in dic:
            dic[i] += lis2[i] 
        else:
            dic[i] = lis2[i]
    
    return dic

print(Dict({"a":2,"b":3},{"b":4,"c":5}))

# ****************************************************************
#8
def word_len(sent):
    result = {}
    words = sent.split()
    for word in words:
        result[word] = len(word)
    return result
print(word_len("I love sphnix"))

# ****************************************************************
#9
def Shopping():
    products = {
        "Laptop": 15000,
        "Mouse": 300,
        "Keyboard": 800,
        "Headphones": 1200
    }
     
    total = 0
    for price in products.values():
        total += price
        
    max_price = 0
    max_product = ""
    for name in products:
        if products[name] > max_price:
            max_price = products[name]
            max_product = name

    print("Total Cost:", total)
    print("Most Expensive Product:", max_product, "-", max_price)


Shopping()
    
    

# ****************************************************************
#10
sent = "I love python python very much"
words = sent.split()
result = []

for word in words:
    if word not in result:
        result.append(word)

print(result)
# ****************************************************************
#11

# ****************************************************************

# ****************************************************************

# ****************************************************************

# ****************************************************************

# ****************************************************************


# ****************************************************************
 
# ****************************************************************

# ****************************************************************

# ****************************************************************

# ****************************************************************
