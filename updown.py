import random

q = random.randint(1,100)
life = 5

while life>0:
      a = int(input("type the answer : "))
      if q < a:
            print("lower")
            life = life - 1
            print("lives:" ,life)
      if q > a:
            print("higher")
            life = life - 1
            print("lives:" ,life)
      if a == q:
            print("answer !")
            break
      
print("the answer is:",q)

