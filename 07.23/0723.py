'''
input() 입력받는 거 
# 3. 문자 여러개 받아서 각 변수에 할당 
a, b = map(int, input().split()) 
print(a, b)


a, b = map(int, input().split(',')) 
print(a, b)

map 함수? 정수로 변환하려고
따라서, 문자만들려면 사용안함.
파이썬 실행후 input 넣어야 행
'''

# # 4. 정수 여러개를 리스트에 할당
# arr = map(int,input().split)
# print(*arr)



# 함수 = 나만의 명령어 만들기 ~  #연습마니
# def add_num(a, b): #정의
#     result = a + b
#     return result 
# a = 2
# b = 3
# sum_result = add_num(a, b) #호출
# print(sum_result)

# parameter(매개변수) vs argument(인자)
# 상부, add_num(a, b) 중 a, b 가 parameter.
# 이어서, sum_result = add_num(a, b) 중 a, b가 argument 

# return_value = print(1)
# print(return_value)

# def num(a,b,c,d,e)
#     result = 
#     return result
# 뒤집기_num = list(num(,,-1))
# # 뒤집기 str[슬라이싱]  # 이거 숫자는 슬라이싱이 안된대.. 

# # 가희실습 
# def num(a):
#     result = str(a)[::-1]
#     return result 
# a_result = num(12345)

# print(a_result)

# 스앵님. 
# num = 12345 # 변수 초기화
# def reverse_func(num): # 정의
#     num = str(num) # 재할당.. 
#     num = num[::-1] # 거꾸로 슬라이싱
#     return num
# result = reverse_func(num) # 호출 
# #NameError: name 'num' is not defined. Did you mean: 'sum'?
# #>> 이거.. 지역스코프에 먼저 변수 있어서 그렇대...
# #>> 그래서, 변수 초기화필요(52번)
# print(result)

'''
num = 827364 # 한번에 처리함? 짝수 어떻게 셈? 

def a_func(num):
    num = str(num)
    digit1 = int(num[0]) #8
    digit2 = int(num[1]) #2
    digit3 = int(num[2]) #7
    digit4 = int(num[3])
    digit5 = int(num[4])
    digit6 = int(num[5])
    return digit1 #불러올 거 정하는 애 

result = a_func(num) #함수호출 
print(result)
# '''
# #스앵님
# num = 827364
# def get_count(num): #get_count = "줘"
#     digit1 = num // 100000 % 10
#     # num // 100000 # 8 
#     digit2 = num // 10000 % 10
#     digit3 = num // 1000 % 10
#     digit4 = num // 100 % 10
#     digit5 = num // 10 % 10
#     digit6 = num % 10
#     even_cnt = (digit1 % 2 == 0)
#     odd_cnt = 6 - even_cnt
    

#     return even_cnt, odd_cnt


# even_cnt, odd_cnt = get_count(num)
# print(even_cnt)
# print(odd_cnt)

# 재귀함수 중요함....
# ㅇ_ㅇ! ㅇㅅaㅇ ㅇㅅㅇr*
# ㅇ.ㅇ! ㅇㅂㅇ ㅇㅁㅇ
# 1. 재귀 호출
# - 무한루프 위험 존재. 
# 2. 종료 조건(기저 조건) 등장
# - return
# # 이미지1에서 재귀함수 이해높이기. 

# def kfc(lev):
#     if lev == 2:
#         return
#     print(lev)  #0
#     kfc(lev + 1) # 호출
#     print(lev)  #

# kfc(0)
# LEGB 중요

# def factorial(n):
#     if n == 5: 
#         return
 

# cnt = 0 
# def factorial(n):
#     global cnt
#     cnt += 1 
#     if n == 1:
#         return 1 
#     else: 
#         return n * factorial(n - 1)

# factorial(5)
# print(cnt)

# lambda #스펠링 조심~ map 함수랑 자주 써염. 
# map 사용법
# map(a, b) 
# * a = 함수.

# 가희가
# temp = [0, 20, 30, 37, 100]

# lambda : C * 9 / 5 + 32
# result = list(map(lambda, temp))

# # gpt! 
# temp = [0, 20, 30, 37, 100]

# result = map(lambda C: C * 9 / 5 + 32, temp)  # 람마 쓰는방법 몰라잉 
# print(*(result)) #= print(list(result))



