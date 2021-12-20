
while(True):
    try:
        print ("Enter num 1")
        num1 = input()
        print ("Enter num 2")
        num2 = input()
        print("sum of the number", int(num1)+int(num2))
        break
    except Exception as e:
        print(e)
        print("please fill valid value")


