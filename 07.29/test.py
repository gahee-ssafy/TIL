
# scores = {'bogeom':89, 
#           'sangho' : 100, 
#           'IU' : 78,
#           'sori' : 76,
#           'hejun' :85}

# # print(sorted(scores.values()))

# # print(*sorted(scores.values())[-1:-2:-1])

# # print(scores.items())
# max_key = ''
# max_value = 0 #정수 초기화...............

# for key, value in scores.items():
#     if value > max_value: #최대값 갱신코드 
#         max_value = value   #최대값 갱신코드 
#         max_key = key  #이렇게 알아서 키값 냄김. 
# print(max_key)

#     # items() 메서드 키값 찾아줌. 
#     # 키값에서 값을 뽑아.
#     # 뽑아서 젤큰거
#     # 젤큰거 갑스올 키불러.? 

# 도전25

# num = map(int,input().split())
# valid_num = set(num) #add값쓰기 


# for i in num:
#     if 1 <= i <= 45:
#         valid_num.add(i) #add값쓰기 
#     print('VALID')


        
# else:
#     print('INVALID')

# #add()를 어따 써야하지..? 


# arr = list(map(int, input().split()))

# def new_flag(arr):
#     for i in arr:
#         if i % 2 == 0:
#             return 1

#         return 0 
    
# print(new_flag(arr)) # 1 2 3 4 5 # 0 



# num = map(int,input().split())

# valid_num = set() #add값쓰기 
# for i in num:
#     if 1 <= i <= 45:
#         valid_num.add(i) #add값쓰기 
   

# if len(valid_num) == 6:print('VALID')      
# else: print('INVALID')  



# set1 = {0, 1, 2, 3, 4}
# set2 = {1, 3, 5, 7, 9}
# set3 = {0, 1}

# print(set1.difference(set2))  # {0, 2, 4}
# print(set1.intersection(set2))  # {1, 3}
# print(set1.issubset(set2))  # False
# print(set3.issubset(set1))  # True
# print(set1.issuperset(set2))  # False
# print(set1.union(set2))  # {0, 1, 2, 3, 4, 5, 7, 9}



# 실습1. 
