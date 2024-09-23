# 백준 - 문제 - 단계별로 풀어보기 - 3 - 반복문 (7/12)

# 5) 백준 25314
# 오늘은 혜아의 면접 날이다. 면접 준비를 열심히 해서 앞선 질문들을 잘 대답한 혜아는
# 이제 마지막으로 칠판에 직접 코딩하는 문제를 받았다.
# 혜아가 받은 문제는 두 수를 더하는 문제였다.
# C++ 책을 열심히 읽었던 혜아는 간단히 두 수를 더하는 코드를 칠판에 적었다.
# 코드를 본 면접관은 다음 질문을 했다. “만약, 입출력이 N바이트 크기의 정수라면 프로그램을 어떻게 구현해야 할까요?”
# 혜아는 책에 있는 정수 자료형과 관련된 내용을 기억해 냈다.
# 책에는 long int는 4바이트 정수까지 저장할 수 있는 정수 자료형이고
# long long int는 8바이트 정수까지 저장할 수 있는 정수 자료형이라고 적혀 있었다.
# 혜아는 이런 생각이 들었다.
# “int 앞에 long을 하나씩 더 붙일 때마다 4바이트씩 저장할 수 있는 공간이 늘어나는 걸까?
# 분명 long long long int는 12바이트, long long long long int는 16바이트까지 저장할 수 있는 정수 자료형일 거야!”
# 그렇게 혜아는 당황하는 면접관의 얼굴을 뒤로한 채 칠판에 정수 자료형을 써 내려가기 시작했다.
# 혜아가 N바이트 정수까지 저장할 수 있다고 생각해서 칠판에 쓴 정수 자료형의 이름은 무엇일까?
# 입력 1 : 첫 번째 줄에는 문제의 정수 N이 주어진다.
# 입력 2 : 4 ≤ N ≤ 1,000 ; N은 4의 배수
# 출력 : 혜아가 N바이트 정수까지 저장할 수 있다고 생각하는 정수 자료형의 이름을 출력하여라.

"""
n = int(input())
for i in range(n//4) : # n을 4로 나눈 몫만큼 long 문자열 반복
     print("long", end = " ") # end를 사용하여 띄어쓰기 포함 한줄로 출력(줄바꿈 없이)
print("int") # int는 마지막에 한번만 출력되므로 반복문 바깥에서 출력
"""


# 6) 백준 15552
# 본격적으로 for문 문제를 풀기 전에 주의해야 할 점이 있다.
# 입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다는 점이다.
# C++을 사용하고 있고 cin/cout을 사용하고자 한다면,
# cin.tie(NULL)과 sync_with_stdio(false)를 둘 다 적용해 주고, endl 대신 개행문자(\n)를 쓰자.
# 단, 이렇게 하면 더 이상 scanf/printf/puts/getchar/putchar 등 C의 입출력 방식을 사용하면 안 된다.
# Java를 사용하고 있다면, Scanner와 System.out.println 대신 BufferedReader와 BufferedWriter를 사용할 수 있다.
# BufferedWriter.flush는 맨 마지막에 한 번만 하면 된다.
# Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다.
# 단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다.
# 또한 입력과 출력 스트림은 별개이므로, 테스트케이스를 전부 입력받아서 저장한 뒤 전부 출력할 필요는 없다.
# 테스트케이스를 하나 받은 뒤 하나 출력해도 된다.
# 자세한 설명 및 다른 언어의 경우는 이 글에 설명되어 있다.
# 이 블로그 글에서 BOJ의 기타 여러 가지 팁을 볼 수 있다.
# 입력 1 : 첫 줄에 테스트케이스의 개수 T가 주어진다. T는 최대 1,000,000이다.
# 입력 2 : 다음 T줄에는 각각 두 정수 A와 B가 주어진다. A와 B는 1 이상, 1,000 이하이다.
# 출력 : 각 테스트케이스마다 A+B를 한 줄에 하나씩 순서대로 출력한다.

"""
import sys
T = int(sys.stdin.readline())
for i in range(T) :
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)
"""


# 7) 백준 11021
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 입력 1: :첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 입력 2 : 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 출력 : 각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다.

# 1차시도
"""
T = int(input())
i = 1
sum = []
while (i <= T) :
    A, B = map(int, input().split())
    sum.append(A + B)
    i += 1
for j in sum :
    print(f"Case #{i}: {j}")
"""

# 재시도 / 뭔가될거같은데
"""
T = int(input())
sum = []
for i in range(T) :
    A, B = map(int, input().split())
    sum.append(A + B)
    for j in sum :
        print(f"Case #{i+1} : {j}")
"""

# 답
"""
T = int(input())
for i in range(1, T+1) :
    A, B = map(int, input().split())
    print("Case #" + str(i) + ":", A+B) # A + B 앞에 쉼표 대신 + 넣으면 TypeError 출력 (Can only concatenate str not "int" to str)
"""
