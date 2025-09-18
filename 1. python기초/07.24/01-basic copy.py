'''
# for 문
students = ['a', 'h', 'b']
for students in students:
    print(f'{students} : 하이!')
'''

'''
# 도전15.


#시도1 
year = int
    if int(input()) / 4 == 0: 
        print(1) #윤년
    if int(input()) / 100 != 0:
        print(1)
    elif int(input()) / 400 == 0:
        print(1)
    else:
        print(0)
# 배운점 #input(#값을 입력해서 넣을고야, 빈칸으로~ )

# 강사님
# 윤년을 구하기 
# 윤년인 조건(if) 나머지 버리기 (else)

year = int(input())
if year % 4 == 0 and year % 100 !=0 or (year % 400 == 0):
    print(1)
else:
    print(0)


# 강사님
# i = 1일때 j는 1, 2, 3 ,4

# for i in range(1, 4):
#     for j in range(1, 5):
#         print(i, j) #들여쓰기 안해서 오류 
#         # 1 1 / 1 2 / 1 3 두번째 포문에서 반복함. 
     




시도1 
list_my = [0, 0, 0, 0, 0]

for list_my in range(5):
    print(f'{list_my}', end=' ')

# 하나씩 출력. 
# 첫자리 5 배정하고 +1 추가?? 

# # 강사님(2) -도전 16
# arr = [0] * 5 # 이거 약간 감 안와! 

# for i in range(5):
# # i = 0, 1, 2, 3, 4, 5,
#     arr(i) = i + 5


# # (2) iterater 방식
# # for num in arr:
# #     print(num, end = ' ')

# # 핵심문제!
# for i in range(2, 10, 3) -> while로 바꿔보기 

# while문
초기식
while 조건식:
    code
    증감식
'
i = 2
result = [] # 리스트 담을 그릇 필요해 
while i < 10: 
    result.append(i) # 점점 추가하려면 이거 써야해 .
    i += 3
print(result)    
'''

# 도전 16 시도~! 

# arr = [0] * 5 

# for i in range(5, 10):
    
#     # 어떻게 행렬을 바꿀까? 
#     print(f'{i}', end = ' ')

# while로 바꿀 수 있을까? 


# while문으롱..?우엥

# # while문
# # 초기식
# # while 조건식:
# #     code
# #     증감식


# arr = [0] * 5 # arr = [0, 0, 0, 0, 0]

# for i in range(5):  # i = 0, 1, 2, 3, 4 줄줄이 생성해내는 포문~ 
#     # arr[i] =   i + 5 # [5, 6, 7, 8, 9]
#     arr[i] = i + 5 


# # (2) iterater 방식
# # for num in arr:
# #     print(num, end = ' ')

# # 핵심문제!
# for i in range(2, 10, 3) -> while로 바꿔보기 