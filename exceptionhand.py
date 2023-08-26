try:
    x=int(input())
    y=int(input())
    print(x/y)
except (ArithmeticError) as msg :
    print("enter valid num only",msg)
except (ZerodivisionError,ValueError) as msgg:
    print("ZerodivisionError",msgg)
#nested exceptionhandling
try:
    print("outer try block")
    try:
        print("inner try")
        print(10/0)
    except ZerodivisionError:
        print("inner exception")
    finally:
        print("inner finally")
except:
    print("outer except block")
finally:
    print("outer finally block")
        