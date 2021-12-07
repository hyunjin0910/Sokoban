#(1-1) 지도값 입력받기
f=open("map.txt",'r')

data=[]

for i in range(13):
    line=f.readline()
    line=line.rstrip('\n')
    data.append(line)

a=data[1:4]
b=data[6:]

#(1-2) 2차원배열 만들기
import numpy as np
a_list=[]
for A in a:
    v1=list(A.replace('#','0').replace("O","1").replace("o","2").replace("P","3"))
    a_list.append(v1)
a_list2=np.array(a_list)

b_list=[]
for B in b:
    v2=list(B.replace('#','0').replace("O","1").replace("o","2").replace("P","3"))
    b_list.append(v2)
b_list2=np.array(b_list, dtype=object)
# (1-3) 출력하기
    #stage1
print("Stage 1")
print(*a, sep='\n')

a_height=a_list2.shape[0]
a_width=a_list2.shape[1]
a_hall=0
a_ball=0
a_p1=np.where(a_list2=='3')
a_p2=a_p1[0]
a_p3=a_p1[1]


for i in a_list:
    a_hall+=i.count('1')
    a_ball+=i.count('2')



print("가로크기 :",a_width)
print("세로크기 :",a_height)
print("구멍의 수:",a_hall)
print("공의 수:",a_ball)
print("플레이어의 위치",a_p2)
#
#
# print("Stage 2")
# print(*b, sep='\n')
