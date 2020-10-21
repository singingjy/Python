import random as r
import time as t

w = ["pineapple","strawberry","watermelon","mango","peach"]
n = 1
print("타자 게임을 시작해겠습니다 엔터를 눌러주세요")
input()
start = t.time()


q = r.choice(w)
while n <= 5:
      print("문제 :",n)
      print(q)
      x = input()
      if q == x :
            print("correct!")
            n = n + 1
            q = r.choice(w)
      else:
            print("false! again!")


end = t.time()
et = end - start
et2 = format(et,".2f")
print("걸린시간 :" , et2,"초")
