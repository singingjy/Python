import pygame as p
import random as r

p.init() #라이브러리 초기화
size = (1000,600) #(x,y)
white = (255,255,255) #RGB(Red,Green,Blue) - 빛의 3원색 최색 최대 255입력값
screen = p.display.set_mode(size)
p.display.set_caption("첫 게임")
playing = True
#이미지업로드
picture = p.image.load("toad.png")
picture_x = 100
picture_y = 100
x = 0
y = 0
#유령 이미지
ghost = p.image.load("유령.png")
ghost_x = 800
ghost_y = 100
#fps
clock = p.time.Clock()

while playing: # == while True => forever
      clock.tick(60) #초당 60번
      for event in p.event.get(): #사용자가 뭘 누르는지 체크
           if event.type == p.QUIT: #만일 게임창 x버튼을 누르면
                 p.quit() #게임창 꺼짐
                 quit() #결과창 꺼짐
                 playing = False # 계속반복 종료
           if event.type == p.KEYDOWN: #키보드를 눌렀을때
                 if event.key == p.K_LEFT:
                       x = -1
                 if event.key == p.K_RIGHT:
                       x = 1
                 if event.key == p.K_UP:
                       y = -1
                 if event.key == p.K_DOWN:
                       y = 1
           if event.type == p.KEYUP: #키보드를 눌렀을때
                 if event.key == p.K_LEFT:
                       x = 0
                 if event.key == p.K_RIGHT:
                       x = 0
                 if event.key == p.K_UP:
                       y = 0
                 if event.key == p.K_DOWN:
                       y = 0
                       
      picture_x += x # += --> picture_x = picture_x + x
      picture_y += y

      
      screen.fill(white)
      screen.blit(picture,(picture_x,picture_y)) #(x,y)
      screen.blit(ghost,(ghost_x,ghost_y))

      ghost_x = r.randint(0,900) #randint -> 난수 (주사위)
      ghost_y = r.randint(0,500)

      
    

      if picture_x >= 900:
            picture_x = 900
      if picture_x <= 0:
            picture_x = 0
      if picture_y >= 450:
            picture_y = 450
      if picture_y <= 0:
            picture_y = 0
      
            

      p.display.flip() # 화면 업데이트

      
      
                 
               

      
