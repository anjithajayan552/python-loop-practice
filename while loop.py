count = 1
while count<=5:
    print(count)
    count = count +1



saved = 0
month = 0
while saved < 500:
    saved = saved + 100
    month = month + 1
    print("month", month, "saved", saved)
print("goal reached in", month, "months")



total = 0
mark = int(input("enter mark(-1 to stop):"))
while mark !=-1:
    total = total + mark
    mark = int(input("enter mark(-1 to stop):"))
print("total=", total)