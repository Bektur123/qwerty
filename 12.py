
#1
a = [1,2,2,1,6,4,7,8,6,5]
b=[2,6,7,8]
print(b)

#2
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,
31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,
57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,
84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,
108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,
128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,
148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,
168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,
188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,
208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,
228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,
248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,
268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,
288,289,290,291,292,293,294,295,296,297,298,299,300]
b = (a[1:254])
print(b)

#3
name=int(input('dlina?'))
print(f'dlina {name}')
a=int(input('shirina?'))
print(f'shirina {a}')
b=name*a
print(f'super {b}')


#4
d = input('Выберите на английском букву a, если хотите машину лексус или тойоту,\nот 2004 года с пробегом 150000, белую или серую, с левымрулем и максимум 2 хозяина\nи стоимостью не больше 10000 или введите\nбукву b если хотите машину лексус или тойоту от 2004 года с пробегом 200000,\nбелую или серую, с левым рулем и максимум 2 хозяина и стоимостью меньше 8000: ')

a='1'
b='2'

if d==a:
        print('Вы выбрали машину a  это лексус или тойоту от 2004 года с пробегом 150000 белую или серую с левым рулем и максимум 2 хозяина и стоимостью не больше 10000')
elif d==b:
        print('Вы выбрали машину b это лексус или тойоту от 2004 года с пробегом 200000, белую или серую с левым рулем и максимум 2 хозяина и стоимостью меньше 8000')
else:
        print('Вы не хотели такую машину')


#Problem 5

login = str(input("Введите ваш логин: "))
pasword = int(input("Введите пароль: "))
x = "leet_hacker_1337@gentoo.com"
y = 1029384756
if login == x and pasword == y:
    print(True)
else:
    print(False)


# Problem 6


movie = ["Ужас", "Детектив" , "Комедия"]
a = "От 21:00 до 23:59"
   
b = "От 00:00 до 20:59"

cost = int(input("Введите цену билета: "))
    
if cost < 500 and cost >= 300:
    print(b,movie)
elif cost < 500 and cost < 300:
    print(a,movie)
else:
    print(False)


# Problem 7


district = str(input("Введите район дома: "))
cost = int(input("Введите цену дома: "))
materials = str(input("Введите материал из которого состоит дом: "))
size = int(input("Введите размер территории в сотках: "))
if district == "чон арык" or district == "байтик" or district == "ортосай":
    if materials == "кирпич" and size < 4 and cost <= 50000:
        print("Данный дом подходит условиям")
    elif materials == "пескоблок" and size < 5 and cost <= 45000:
        print("Данный дом подходит условиям")
    else:
        print("Данный дом не подходит условиям")
else:
    print("Данный дом не подходит условиям")



# Problem 8

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print(a[5: 11])







