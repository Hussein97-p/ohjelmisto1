#Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron,
# jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi).
# Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.
#--------------------------------------------------------------------------------------------------------------------#
#قم بكتابة برنامج يطلب من المستخدم رقم الشهر،
#وبعد ذلك يقوم البرنامج بطباعة الموسم المقابل (الربيع، الصيف، الخريف، الشتاء).
#في برنامجك، قم بتخزين المواسم المقابلة للأشهر كسلاسل في بنية بيانات صفية.
#دعونا نحدد طول كل موسم بثلاثة أشهر، بحيث يكون شهر ديسمبر هو أول شهر شتاء
#--------------------------------------------------------------------------------------------------------------------#
Four_season = ["winter","spring","Summer","Autoum"]
print("Please enter a number between 1 and 12")
The_mounth = int (input("Enter The Mounth number: "))

if The_mounth in  [12,1,2] : 
    print(The_mounth , "Belong To The Season" , Four_season [0])
elif The_mounth in  [3,4,5] : 
    print(The_mounth , "Belong To The Season" , Four_season [1])
elif The_mounth in  [6,7,8] : 
    print(The_mounth , "Belong To The Season" , Four_season [2])
elif The_mounth in  [9,10,11] : 
    print(The_mounth , "Belong To The Season" , Four_season [3])
else :
    print("Please enter a number between 1 and 12.")
