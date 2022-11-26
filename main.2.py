num = int(input("enter the number:"))
st = int(input("enter the stepin vid 1 do 7:"))
if st > 7 or st < 0:
    print("stepin povunna bytu vid 1  do 7")
else:
    print(num**st)