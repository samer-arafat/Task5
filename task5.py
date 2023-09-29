# please write down your name, age, street, city, and country...
name = (' "name: lama" ')
age = (' "age: 20" ')
country = 'palestine'
city = 'gaza'
street = '159'
address = (' "address: 159, gaza, palestine" ')
print(name)
print(age)
print(address)
name = 'lama'
age = 15
address = '159, Gaza, Palestine'
txt = (' "Hello, {lama}, your age is 15 Years Old, Your Address is 159, Gaza, Palestine." ')

print(txt)
print(type(name))
print(type(address))
print(type(city))
print(type(country))
print(type(street))
print("Hello 'lama', How Are You? \ """ 'Your', 'age is', "15"" + And Your", country)
print(' "Hello " lama", " How Are You? \  ')
print(' """ Your age Is "15"" + And')

name = 'ITF Gsg Python'
print(name[0])
print(name[2])
print(name[-1])
print(name[0:3])
print(name[0:7:2])
print(name[11:14])
print(name[14:7:-1])

name = "$&$&Mohammed$&$&"
print(name.strip('$&$&'))

msg = "I %7 Python And Although I %7 GSG with Zakaria"
print(msg.replace('%7',('love')))
num1, num2, num3, num4, num5,num6 = '4', '56', '963', '384', '8719', '87190'

print(num1.zfill(5))
print(num2.zfill(5))
print(num3.zfill(5))
print(num4.zfill(5))
print(num5.zfill(5))
print(num6.zfill(5))

# #tite : here we can make the first letter in each word uppercase, also we can change any leeter in the word vice versa.
txt1 = ('saMer')
print(txt1.title())
print(txt1.upper())
print(txt1.lower())

name_one = "SaMER"
name_two = "Abed"
print(name_one.lower())
print(name_two.upper())
