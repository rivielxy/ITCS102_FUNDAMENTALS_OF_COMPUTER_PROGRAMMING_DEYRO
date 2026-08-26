# Code Challenge 2

money = 5762
dot = 0
dfh = 0
dth = 0
doh = 0
df = 0
dt = 0
dtn = 0
dfv = 0
do = 0

print("Your currently money is:", money)
print("Money to deposit --> ", money)
dot = money // 1000
money = money - (dot * 1000)
print("One Thousand Pesos: ", dot)
dfh = money // 500
money = money - (dfh * 500)
print("Five Hundred Pesos: ", dfh)
dth = money // 200
money = money - (dth * 200)
print("Two Hundred Pesos: ", dth)
doh = money // 100
money = money - (doh * 100)
print("One Hundred Pesos: ", doh)
df = money // 50
money = money - (df * 50)
print("Fifty Pesos: ", df)
dt = money // 20
money = money - (dt * 20)
print("Twenty Pesos: ", dt)
dtn = money // 10
money = money - (dtn * 10)
print("Ten Pesos: ", dtn)
df = money // 5
money = money - (dfv * 5)
print("Five Pesos: ", dfv)
do = money // 1
money = money - (do * 1)
print("One Peso: ", do)



