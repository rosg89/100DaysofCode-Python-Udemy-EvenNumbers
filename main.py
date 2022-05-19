#Write your code below this row 👇

#Sum of all the even numbers 1-100.

#Forma facil
total = 0

for number in range (2,101,2):
  total += number

print(total)

#Forma dificil
total2 = 0

for number in range(1,101):
  if number%2 == 0:
    total2+=number

print(total2)