'''
# <시도1>

total_1 = 0 
while True:
    A = int(input())
    # ValueError: invalid literal for int() with base 10: '1 3 5 0'
    if A == 0:
        break
    
total_1 += A
print(total_1)



# SWEA 18
total_1 = 0 

while True:
    N = int(input())
    # ValueError: invalid literal for int() with base 10: '1 3 5 0'
    if N == 0:
        print(total_1)
        break

    elif N < 0:
        print(total_1)
        total_1 = 0 # 값 초기화

    else:
        total_1 += N 

#SWEA 19

arr = list(map(int,(input().split())))

max_v = float('-inf') #최대값 범위가 없을 때, 음의 무한대~~ 

# min_v = float('inf')
for idx, value in enumerate(arr):
    if value > max_v:
        max_v = value # 최대값 갱신
        result = idx #그 때의 인덱스 


print(result)


# my_email = input()

# idx_1 = my_email.find('@')
# # @~ 끝까지 어떻게 출력? 슬라이싱 
# print(my_email[idx_1:])

# # 이메일 형식 아니면 출력
# if idx_1 <= 0:
#     print('Invaild email')


# 함수로 변환.. 1함수 있고 @있으면 이렇게 아니면 저렇게 출력. 
# 실습 19
def get_domain(email):
    idx = email.find('@')

    if idx == -1:
        return 'Invaild email'
    
    domain = email[idx + 1:]
    return domain

email = input()
result = get_domain(email)
print(result)
'''

# <실습21- 시도1> 

# numbers = []

# while True:
#     n = int(input())  # 하나씩 입력받아
#     if n == 0:
#         break  # 0이면 멈춤
#     numbers.append(n)  # 리스트에 추가

# print(*numbers[::-1])  # 확인용


# # pop() 어디다가 넣을 지 몰루


# stack = [] 

# while True:
#     char = input()

#     if char == 0:
#         break

#     stack.append(char)

# word = ""
# while not stack: 

# n = int(input())
# friends = [1, 2, 3]
# for _ in range(n):
#         front = friends.pop(0)
#         friends.append(front)

# print(friends[0])

# <실습23-시도1> 

# arr = list(map(int,input().split()))
# arr.sort() #밑위에 붙이려니 타입에러뜸. 정렬기능만 해야함. 


# print(*arr)


# # n = int(input())
# numbers = list(map(int, input().split())) # 1 3 2 

# # 오름차순 정렬
# numbers.sort() # 1 2 3 

# result = ""
# for num in numbers: #반뵥 
#     result += str(num) # 문자열로 바꿔서 연결

# print(result)


# arr = [[0] * 5 for _ in range(5)]

# print(arr)


# n = int(input())
# arr = [list(map(int,input().split())) for _ in range(n)]
# print(arr)

