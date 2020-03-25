# Slicing and Dicing

a = "Python"
b = "Learn"
c = ['Pempek' , 12000, 'Bakso', 15000]

print(b[1:])
print(a[-2:] + b[-4])
print( b[:2] + a[2])
print("Harga " + c[-2] + " = Rp.", c[-1])
print("Jumlah data di variable C = " + str(len(c)) + " Data")

# Break
print("")
print("")

# Tuples

print("TUPLES")
name = ("Nami" , "Robin", "Hancock")
age = (26 , 29 , 27)

print("Mugiwara Pirates = " + str(name[0:2]))
print("Hancock age = " + str(age[2]))

data = name + age

print(data)

# Break
print("")
print("")

# Dictionary

print("Dictionary")

gals = {'Name' : 'Nico Robin', 'Age' : 29, 'Pirates' : 'Mugiwara'}

print(gals)

del gals['Pirates']

print(gals)

gals['Name'] = 'Nami'
gals['Age'] = 26
gals['Role'] = 'The Navigator'

print(gals)

