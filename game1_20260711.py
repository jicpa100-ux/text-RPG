map=100,100
key="없음"
x = 0
y = 0

name=input("이름을 입력하시오:")
if name == "제미나이"or name == "챗지피티":
    print(name,"이라는 AI가 있었다.")
else:
    print(name,"이라는 사람이 있었다.")

a=input("x={}, y={}\nWASD로 이동:".format(x,y))

while True:

    while True:

            if a=="w":
                print("앞으로 갔습니다.")
                print("------------------------------------------")
                y+= 1
            elif a=="a":
                print("왼쪽으로 갔습니다.")
                print("------------------------------------------")
                x-=1
            elif a=="s":
                print("뒤로 갔습니다.")
                print("------------------------------------------")
                y-=1
            elif a=="d":
                print("오른쪽으로 갔습니다.")
                print("------------------------------------------")
                x+=1

            if x==0 and y==0:
                print("맵에 중심입니다.")
                
            elif x==100 or x==-100 or y==100 or y==-100:
                print("맵의 끝입니다.")
                
            elif x==-100 and y==100:
                print("상자가 있다.열려면 o")
                input()
                
            elif x==0 and y==1:
                print("앞으로 갔습니다.앞에 절벽이 보인다.")
                
            elif x==0 and y==2:
                quit=input("절벽으로 떨어졌습니다.게임 종료:q:")
                if quit=="q":
                    break
                
            elif x==-1 and y==0:
                print("왼쪽으로 갔습니다. 옆에 보물 상자가 보인다.열려면 o:")
                b2=input()
                if b2=="o"and key=="있음":
                    print("열림. 돈 20원을 얻었습니다.")
                else:
                    print("열쇠를 얻으시오. 잠겨 있음.")
                    
            elif x==-2 and y==0:
                print("왼쪽으로 갔습니다. 아무것도 안 보인다.")
                
            elif x==0 and y==-1:
                print("뒤로 갔습니다.상자가 있다.열려면 o:")
                input()
            else:
                print("{}은 바보".format(name))

            a=input("x={}, y={}\nWASD로 이동:".format(x,y))

    ans=input("다시 시작하시겠습니까? y/n")
    if ans==y
        continue
    elif ans==n
        break
    

