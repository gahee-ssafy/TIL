# 강의요약
### 7.16.(1차)
GUI : 그래픽 유저 인터페이스
TUI : 텍스트 (이말은 잘 안씁니다.) = CLI
CLI : Command Line Interface

interface : 대상을 제어하는 수단 ( ex) 리모컨) )

Window OS의 Interface
GUI : Windows Shell
CLI : cmd(명령프롬프트), Power Shell

Linux OS의 Interface
GUI : GNOME
CLI : bash

왜 굳이 bash를 쓸까??
bash가 편해서 ---> Tab키 자동완성

Git을 다룰때 Interface
GUI : Github Desktop, 소스트리
CLI : git bash

결론 : GUI, CLI 둘다 쓸수는 있어야하지만 우리는 CLI를 쓸겁니다.

GUI의 장점 : 그래프 같은 복잡한 분석 보기 편하다
CLI의 장점 : 빠르다(Commit 명령어 3~4초면 끝)

---

# 배쉬사용 
항상 HOME 디렉토리에서 시작 : ~
. : 현재 디렉토리
cd ~ : 홈 디렉토리
cd .. : 상위 디렉토리
cd - : 뒤로가기

touch : 파일생성
mkdir : 폴더생성
start : 파일 열기
rm : 파일 삭제
rm -rf : 폴더 삭제
cp : 복사

절대경로
~/Desktop/test/python/

상대경로(현재 티렉토리를 기준)
cd ./python
cd ../python2

---

python.org ---> python 설치 ---> 3.11.9
인터프리터

extension??
너 IDE 뭐써??
vscode는 IDE일까??
vscode는 텍스트 에디터 : 여기에 extension을 추가해서 마치 IDE처럼 쓴다.

IDE
Python : Pycharm, jupyter notebook
C : Visual Studio
Java : IntelliJ

node.js ---> 런타임
js 백엔드 프레임워크 ---> express.js 

---

Markdown : 로직 X 
README.md에 활용
: 내가 공부한내용, 프로젝트에 대한 간단한 설명(가독성, 편의성)

---
git init  : git 시작 (로컬 저장소 생성)
rm -rf .git : git 삭제(git 종료)

git add . : staging area에 변경사항 올리기
git status : staging area의 작업 파일 확인

git config --global user.email "이메일주소"
git config --global user.name "이름"
git config --global -l

git commit -m "메시지명" : repository에(staging area의 변경사항을)올리기
git log : repository 작업 파일 확인 (커밋 이력 확인)

---

참고자료 

git commit --amend : vim 에디터가 열린다

수정 후(커서 위치를 확인 후 과감하게 타이핑)

ecs -> :q -> 저장하지 않고 종료
ecs -> :q! -> 저장하지 않고 강제 종료
ecs -> :wq -> 저장하고 종료

### 7.17.(2차)
  git : 분산 버전 관리 시스템

git : 로컬저장소 // github : 원격저장소

git init : git 시작

git config --global user.name "이름"
git config --global user.email "이메일"

git add . : staging area에 올리기
git status : staging area의 작업 파일 확인

git commit -m "메시지명" : repository에 올리기
git log : 커밋 이력을 확인

git remote add origin url : 로컬 저장소와 원격저장소를 연결(origin은 별칭)
git remote -v : remote 목록 확인

git push origin +master : 가장 최근에 commit 되어있던 것을 강제로 push (origin:별칭, master:branch명, +:강제로 진행)

---

Q) clone과 pull의 차이점이 뭘까??
A) 새로운 환경에서 처음 다운로드 : clone

명령어 : git clone url

Q) clone을 받으면 remote를 할 필요가 있을까?
A) remote를 할 필요가 없다.

Q) clone과 pull의 차이?
A) 한번 clone을 받고 그 이후에는 pull로 진행

명령어 : git pull origin +master

---

자리 옮긴후 

1. git clonfig --global -l 확인
user.name, user.email 확인

1. 제어판 -> 사용자 계정 -> window 자격 증명 -> github, gitlab 삭제


commit 메시지 수정하기

명령어 : git commit --amend

vim에디터에서 수정하고
esc -> :q! : 저장하지 않고 강제 종료
esc -> :wq! : 강제 저장하고 종료

---
git revert : 특정 commit을 없었던 일로 만들기

a.txt 만들고 commit
b.txt 만들고 commit
c.txt 만들고 commit

git log -> 해시값 전체 복사(ctrl + shift + c), 붙여넣기(shift + insert)

명령어 :
git revert 해시값 : 이 특정 커밋을 없었던 일로 만든다.
vim 에디터 -> esc -> :wq

---

git reset : 특정 commit으로 되돌리기

git reflog : 이전 과거 commit 기록들을 모두 볼 수 있음

명령어 : git reset --hard HEAD@{번호}

---

staging area 있는 작업을 working directory로 옮기기
(git add 취소하기)

<git 2.23 버전 이전>

1. commit이 없는 경우
git rm --cached 파일명

2. 이전에 했던 commit이 있는경우(권장 방법)
git restore --staged 파일명

## 07.18.(금)
바이브 코딩을 함.
코파일럿을 활용하여 AI생성형 챗봇을 만듦.
코파일럿은 프로그래밍 경험이 없어도 코딩을 자동보완하는 EXTENSION임.



## 07.21.(월)
### 강의노트
ctrl 누른 상태에서 마우스 좌클릭
print줄바꿈 내장 함수의 end옵션 default는 줄바꿈
print공백 내장 함수의 sep옵션 default는 공백
print('hello', end = ' ')
print('world')

<!-- # 변수에 값이 저장된다는 개념이 아니다.
# 변수에 값이 할당된다. 값은 메모리 주소를 가르키고, 메모리를 참조한다. -->

degree = 36.5
print(id(degree))
# 재할당하면 메모리 주소가 바뀐다. 
degree = 36.6
print(id(degree))

<!-- 
# 변수명 규칙 : 숫자로 시작할 수 없다.
# 언더스코어 가능 _
# 키워드 사용 불가능 (if, for)
# 내장함수나 메서드 가급적 사용 하지 않는다
# 대소문자는 서로 다른 유니코드값을 가지고 있다. -->

lst = [1, 2, 3]
sum = 7 # 에러는 나지 않지만 가급적 사용하지 않는다
print(sum(lst))


a = 2
b = 2.0
c = 3 + 2j
d = '1'

정수(int) : 음의정수, 양의정수, 0
print(type(a))
print(type(b))
print(type(c))
print(type(d))

1억을 지수표현법으로
num = 1e8
print(num)

# 우선순위는 음의 부호보다 거듭제곱의 우선순위가 더 높다!!
- 그래서 소괄호를 활용해야 함. 
예문) 
num = -2 ** 2
print(num)

공백도 유니코드 값을 가진다.
space = ' '
print(ord(space))

# f-string
예문1)
name = '장상호'
age = 20
height = 185.76

print(f'이름은 {name}이고, 나이는 {age}살, 키는 {height:.1f}')
   1.  :.1f /소수점 하나만 보임.

예문2) 
전 가희
name = '가희'
print(f'{전 }{name}')
- f스트링을 쓰면, 공백이나 띄움이 자유로움.
- 프린트만 쓰면 공백이나 띄움이 제한적임. 
  > 콤마는 모두 공백.

![이미지](./07.18/image.png)
# 시퀀스타입, 중요 
# 리스트 : 가변시퀀스

= 변함 + 순서 

arr = [1, 2, 3, 4]
arr[0] = 10
print(arr)

# 문자열 : 불변시퀀스
- 불변 + 순서
char = "hello"
char[0] = 'y'
print(char)


char = 'Hello World'

length = len(char)
print(length)
print(char[0], char[-1])
print(char[::2])
print(char[::-1])
char[start:stop:step]
- 시작, 멈춤, 걸음폭
- step이 -1이면 역순으로 생성함. -1부터 시작.
- start는 0으로 시작. 
- stop은 그 전까지 생성함. 예를들어 char = 12345, char[0:3:]라면 123임. 



### vscode 단축키 
ctrl + ` : 터미널 열고 닫기
ctrl + b : 사이드바 열고 닫기
ctrl + s : 저장
ctrl + w : 창 닫기
ctrl + a : 전체 블록 지정
ctrl + l : 한줄 블록 지정
ctrl + / : 주석
home키, end키
shift + tab : 들여쓰기 취소
ctrl + , : settings
ctrl + shift + f : 전체 파일에서 찾기
ctrl + shift + p : 명령 팔레트
ctrl + h : 바꾸기
alt + shift + 방향키 : 한줄 복사 붙여넣기
alt + 마우스 좌클릭 : 커서 여러개
ctrl + alt + 방향키 : 커서 여러개

# 0722
# list 
* 가변 시퀀스
* 인덱싱, 슬라이싱 가능. 
   1. 슬라이싱 
      1. arr = [1, 2, 3, [4, 5, 6]]
      2. print(arr[1:1:1])
   2. 인덱싱 
      1. arr = [1, 2, 3, [4, 5, 6]]
      2. print(arr[3][0])
   3. 실습실.. 
      1. numbers = list(range(1, 11))print(numbers)
      2. numbers = list(range(0, 11, 2))print(numbers)


예문) 
arr = [1, 2, 3, [4, 5, 6]]
print(arr[3][0])
print(arr[3][:])
print(arr[3][::-1])

len 함수(내장함수일까? 메서드일까?)
print(len(arr))


리스트의 할당 개념 (추후에 깊은 복사 얕은 복사의 개념에 중요함)
arr = [1, 2, 3, 4]
print(id(arr)) 
arr[3] = 7 # 재할당 X
print(id(arr)) # 메모리 주소가 같다
arr = [5, 7, 4] # 재할당 O
print(id(arr)) # 메모리 주소가 다르다



# 튜플 
* 불변 시퀀스(리스트와 차이는 불변)
* my_tuple = (1, 2, 3, 4, 5)
* 특징
1. 안정성 (보안성)
2. 빠름. (시간복잡도상 효율적)적이다.

# 이해못함!
방향배열 자료구조
y방향, x방향
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# 특징 2
x, y = 1, 2 # 튜플이 생략되어 있다.
x, y = (1, 2)

def kfc(x, y, z):
    return x, y, z # 튜플이 생략되어 있다.
    # return (x, y, z)

x, y, z = 1, 2, 3

print(kfc(x, y, z))


# range(start, end, step) 
* 불변 시퀀스
1. step이 양수
2. start부터 end - 1까지 step만큼 증가
3. step이 음수
* start부터 end + 1까지 step만큼 감소 
* 핵심은 항상 수직선 상에서 end를 포함하지 않는다!!!

예) n번 반복하는 반복문을 만들고 싶다
for i in range(n)

# 딕셔너리 : 가변비시퀀스
1. 리스트에는 인덱스 -> 딕셔너리에는 key가 인덱스를 대신
2. 핵심 : 딕셔너리는 비시퀀스이기때문에 key로 접근을 한다!!
   1. 딕셔너리 초기화 2가지 방법
      1.  하드코딩
      예문) 
      my_dict = {"apple": 2, "banana": 5, "peach": 4}
      2. key로 접근
      예문)
      d = dict() # 빈딕셔너리
      d["apple"] = 2
      d["banana"] = 5
      d["peach"] = 4

Q) d = {} 딕셔너리? 세트?  ---> 빈 딕셔너리
s = set() ---> 빈 세트

print(my_dict["banana"])
print(my_dict.keys()) # key만 출력
print(my_dict.values())
print(my_dict.items()) # key와 value 출력


# 세트 가변비시퀀스
- 세트의 특징 : 중복을 허용하지 않는다 ex) 로또
예문
my_set = {1, 2, 3, 4}
my_set.add(5)
print(my_set)


# None 타입 (빈 문자열과는 다르다)
a = None
b = ""

print(type(a))
print(type(b))


# bool 타입
print(bool(3)) # 0을 제외한 모든 정수는 True
print(bool(0.0))
print(bool("")) # 빈문자열을 제외한 모든 문자열 True


# 명시적 형변환
num = '3.5'
num = int(float(num)) # int는 버림

print(num)


# 복합 연산자
a가 1씩증가
a = 3
a = a + 1 # 이렇게 하지 말기 무조건 복합연산자 쓰기
a += 1


# 비교연산자
주의 1. 항상 부등호 먼저
=> X ---> >= O
 print(3 => 2)

# 주의 2. !는 부정의 의미를 갖고 있다.
print(3 != 2) # 3과 2는 같지 않다
print(not(True))

# 이해못함! 
# 단축평가 : and는 둘다 참이어야 참, or은 둘중 하나라도 참이면 참 print(0 or 3 or 8) ???
print(2 and 3 and 8) ???
print(7 or 0 or 8) ???
