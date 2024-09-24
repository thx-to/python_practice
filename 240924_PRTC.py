# 백준 - 문제 - 문제 순위 : 단계별로 풀어보기에서 중간중간 모르는 개념들이 있어서 넘어옴..

"""
# 백준 1152
영어 대소문자와 공백으로 이루어진 문자열이 주어진다.
이 문자열에는 몇 개의 단어가 있을까? 이를 구하는 프로그램을 작성하시오.
단, 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.

입력 : 첫 줄에 영어 대소문자와 공백으로 이루어진 문자열이 주어진다.
이 문자열의 길이는 1,000,000을 넘지 않는다.
단어는 공백 한 개로 구분되며, 공백이 연속해서 나오는 경우는 없다.
또한 문자열은 공백으로 시작하거나 끝날 수 있다.
출력 : 첫째 줄에 단어의 개수를 출력한다.

예제 입력 1: The Curious Case of Benjamin Button
예제 출력 1 : 6

# 풀어보기
a = list(input().split())
print(len(a))
"""

"""
# 백준 1546
세준이는 기말고사를 망쳤다. 세준이는 점수를 조작해서 집에 가져가기로 했다.
일단 세준이는 자기 점수 중에 최댓값을 골랐다. 이 값을 M이라고 한다.
그리고 나서 모든 점수를 점수/M*100으로 고쳤다.
예를 들어, 세준이의 최고점이 70이고,
수학점수가 50이었으면 수학점수는 50/70*100이 되어 71.43점이 된다.
세준이의 성적을 위의 방법대로 새로 계산했을 때, 새로운 평균을 구하는 프로그램을 작성하시오.

입력 : 첫째 줄에 시험 본 과목의 개수 N이 주어진다. 이 값은 1000보다 작거나 같다.
둘째 줄에 세준이의 현재 성적이 주어진다.
이 값은 100보다 작거나 같은 음이 아닌 정수이고, 적어도 하나의 값은 0보다 크다.
출력 : 첫째 줄에 새로운 평균을 출력한다.
실제 정답과 출력값의 절대오차 또는 상대오차가 10-2 이하이면 정답이다.

예제 입력 1 :
3
40 80 60
예제 출력 1 : 75.0

# 풀어보기 / 검색찬스..

N = int(input()) # 전체 과목 수
S = list(map(int, input().split())) # 과목별 점수 리스트로 입력받음
M = max(S) # 최대 점수

NS = [] # 새로운 점수 리스트를 빈 리스트로 생성
#  for문에 대한 이해가 더 필요할듯
#  for 반복 변수 in 반복 범위
# 반복 변수는 반복 범위에 따라 변하면서 명령을 실행
# for문을 시작하면 반복 범위의 첫번째 데이터가 반복 변수에 들어가고 명령 실행
# 다음은 반복 범위의 두번째 데이터가 반복 변수에 들어가고 명령 실행 ...
# 이런식으로 반복 범위의 마지막까지 반복
for score in S : # S라는 리스트의 범위에서 score라는 변수로 처음부터 끝까지 명령 실행
    NS.append(score / M * 100) # score(반복 변수)/M*100의 값을 NS 리스트에 추가
print((sum(NS)) / N) # NS 리스트의 총합 / N으로 평균 출력
"""

"""
# 백준 27866
단어 S와 정수 i가 주어졌을 때, S의 i번째 글자를 출력하는 프로그램을 작성하시오.

입력 : 첫째 줄에 영어 소문자와 대문자로만 이루어진 단어 S가 주어진다. 단어의 길이는 최대 1000이다.
둘째 줄에 정수 i가 주어진다. (1 ≤ i ≤ |S|)
출력 : S의 i번째 글자를 출력한다.

예제 입력 1 :
Sprout
3
예제 출력 1 :
r

# 풀어보기
s = input()
i = int(input())
print(s[i-1])
"""

"""
# 백준 11720
N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

입력 : 첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.
출력 : 입력으로 주어진 숫자 N개의 합을 출력한다

예제 입력 1 :
1
1
예제 출력 1 :
1

# 풀어보기
N = int(input())
L = list(map(int,input()))
print(sum(L))
"""

