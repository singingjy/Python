import pygame as p

p.init() #라이브러리 초기화
size = (1000,600) #(x,y)
white = (255,255,255) #RGB(Red,Green,Blue) - 빛의 3원색 최색 최대 255입력값
screen = p.display.set_mode(size)
p.display.set_caption("점프게임")

playing = True

while playing: # == while True => forever

      for event in p.event.get(): #사용자가 뭘 누르는지 체크
           if event.type == p.QUIT: #만일 게임창 x버튼을 누르면
                 p.quit() #게임창 꺼짐
                 quit() #결과창 꺼짐
                 playing = False # 계속반복 종료
      
      screen.fill(white)

      p.display.flip() # 화면 업데이트 
      
                 
               

      
