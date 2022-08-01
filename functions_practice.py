def hello():
    print("Hello Tyler")

def pack(a, b, c):
    return[a, b, c]

def eat_lunch(lunch_list):
    if len(lunch_list) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(lunch_list)):
                if i == 0:
                    print(f"First I eat {lunch_list[0]}")
                else:
                    print(f"Next I eat {lunch_list[i]}")

hello()
print(pack("a","b","c"))
print(pack(1,2,3))
eat_lunch([])
eat_lunch(["cookie"])
eat_lunch(["sandwich", "cookie", "juice box"])