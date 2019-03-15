
#3.7.19

#Quentin Sander

#Ask for name and age and find good speed for there age

name = input('Enter Name:')

age = -1

try:
    age = int(input('Enter Your Age:'))

except ValueError:
    print('\n''That was not an integer for your age')

print('\n''Name:', name)
print('Age:', age)


sum = 0

#Here you say what your fastest throws from the past 3 years
for i in range(3):
    enter_a_num = int(input("your fastest throws for 3 year:"))
    sum = sum + enter_a_num

print("")

print("The Sum Of Your Number Is: " + str(sum))

#Speed of the ball compared to your age
while True:
    speed_of_ball = int(input("speed of ball for your age:"))
    if speed_of_ball > 60:
        print("That is to fast " + "\n")
    elif speed_of_ball < 55:
        print("That is way to slow", "\n")
    else:
        print("That is perfect for your age", "\n")
        break

print("Hooray, You Found The Perfect speed")

try:
    my_num = int(input('Enter a Speed: '))
    print('Your number:', my_num)
except ValueError:
    print('\n''That was not a Speed, (: ')


#Here you are giting info about fastest pass and or hit
sum = 0

for i in range(3):
    enter_a_num = int(input("your fastest pass or swing for 3 year:"))
    sum = sum + enter_a_num

print("")

print("The Sum Of Your Number Is: " + str(sum))

while True:
    speed_of_ball = int(input("speed for your age:"))
    if speed_of_ball > 60:
        print("That is to fast " + "\n")
    elif speed_of_ball < 55:
        print("That is way to slow", "\n")
    else:
        print("That is perfect for your age", "\n")
        break

print("Hooray, You Found The Perfect speed")

try:
    my_num = int(input('Enter a Speed: '))
    print('Your number:', my_num)
except ValueError:
    print('\n''That was not a Speed, (: ')



my_number = 10

print ("Guess how good you are")
print("")

guess = int(input("Enter a guess:"))

while guess != my_number:
    print("")
    print ("Wrong, guess again")
    guess = int(input("Enter a guess: "))

print("")
print ("Good jod, you got it you are a pro!")



x = 20

while x > 5:
    print(x)
    x = x - 2

#The years that you plaed in for your age
    def print_league_year(x):
     print(x)
print('\n', x)

print_league_year(13)
print_league_year(23)


def name_and_age(name, age):
 print('\n', 'Hi, my name is', name, 'and I am', str(age), 'years old!')




def print_two_years(x, y=20):
 print('First Year:', x)
 print('Second Year: ' + str(y))


print_two_years(34, 45)
print_two_years(78)



def print_sum(x, y):
 print(x + y)


print_sum(46, 62)



def print_multiple_times(string, times):
 for i in range(times):
  print(string)


print_multiple_times('Hey there sports Player you will do great in your sport', 1)

'''
In this code I made it help sport players find there averages and to find how good they are compared to their
age this code will help people practes on the parts that they need to get better at for the League.
'''