# # A = 30
# # B = 10

# # # print(A / B) # 몫
# # # print(A % B) #나머지


# # year = int(input())
# # if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
# #         print(1)
# #     else
# #         print(2)


# # for i in range(1, 4):
# #      for j in range(1, 5):
# #          print(i, j) 


# # 1 2 3 
# # 1 2 3 4 

# # range(1, 4)

# # for i in range(1, 4): #for i, i를 반복한다. 1~3 #1 2 3 
# #     for j in range(1,5):
# #         print(i, j) 


# # arr = [0] * 5 # arr = [0, 0, 0, 0, 0]

# # for i in range(5):  # i = 0, 1, 2, 3, 4 줄줄이 생성해내는 포문~ 
# #     # arr[i] =   i + 5 # [5, 6, 7, 8, 9]
# #     arr[i] = i + 5 
# # print(arr)


'''
arr = list(map(int, input().split()))

# for i in arr:
#     if i % 2 == 0: 
#         True
print(int(any(i % 2 == 0 for i in arr)))
# print(arr)
# flag 처리 코드를 flag 변수를 쓰지 않고, 함수로 바꿔
# 어떤 함수를 써야할 지 모르겠어.. 힌트 점 

# arr = list(map(int, input().split()))
# print(int(any(i % 2 == 0 for i in arr)))

# any함수: 조건에 맞으면 True 뱉엉, iterabel(반복가능한 것)을 받아야 해
# 만약, any(i % 2 == 0) 이면 "파이썬 : i는 누구야? 혼란스러어.." 
'''

