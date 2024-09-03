#اكتب دالة تستقبل قائمة من الأعداد الصحيحة كمعلمة.
# يقوم البرنامج بإرجاع مجموع الأرقام الموجودة في القائمة.
# للاختبار، اكتب برنامجًا رئيسيًا حيث يمكنك إنشاء قائمة واستدعاء دالة وطباعة المبلغ الذي تُرجعه.

def All_sum(A):
    return sum(A)

A = [] 
while True:
    x = int(input("<Enter 0 To Collect Numbers Or To Exit>\nPut a number Every Time\nTo Collect: "))
    if x == 0:
        break
    A.append(x)

D = All_sum(A)
print("All The Sum is: ", D ,"Thank you")


#-------------------------------------------------------------------------------------------------------#

list = [12,54,23,11,53,76,86]
Collect = sum(list)
print("All THE Sum is(For The TESt) : " , Collect, "Thank you")