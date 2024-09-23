# 백준 - 문제 - 단계별로 풀어보기 - 4 - 1차원 배열 (5/10)

# 5) 백준 10810
# 도현이는 바구니를 총 N개 가지고 있고, 각각의 바구니에는 1번부터 N번까지 번호가 매겨져 있다.
# 또, 1번부터 N번까지 번호가 적혀있는 공을 매우 많이 가지고 있다.
# 가장 처음 바구니에는 공이 들어있지 않으며, 바구니에는 공을 1개만 넣을 수 있다.
# 도현이는 앞으로 M번 공을 넣으려고 한다.
# 도현이는 한 번 공을 넣을 때, 공을 넣을 바구니 범위를 정하고,
# 정한 바구니에 모두 같은 번호가 적혀있는 공을 넣는다.
# 만약, 바구니에 공이 이미 있는 경우에는 들어있는 공을 빼고, 새로 공을 넣는다.
# 공을 넣을 바구니는 연속되어 있어야 한다.
# 공을 어떻게 넣을지가 주어졌을 때, M번 공을 넣은 이후에
# 각 바구니에 어떤 공이 들어 있는지 구하는 프로그램을 작성하시오.
# 입력 1 : 첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)이 주어진다.
# 입력 2 : 둘째 줄부터 M개의 줄에 걸쳐서 공을 넣는 방법이 주어진다.
# 입력 3 : 각 방법은 세 정수 i j k로 이루어져 있으며,
# 입력 4 : i번 바구니부터 j번 바구니까지에 k번 번호가 적혀져 있는 공을 넣는다는 뜻이다.
# 입력 5 : 예를 들어, 2 5 6은 2번 바구니부터 5번 바구니까지에 6번 공을 넣는다는 뜻이다.
# 입력 6 : (1 ≤ i ≤ j ≤ N, 1 ≤ k ≤ N)
# 입력 7 : 도현이는 입력으로 주어진 순서대로 공을 넣는다.
# 출력 1 : 1번 바구니부터 N번 바구니에 들어있는 공의 번호를 공백으로 구분해 출력한다.
# 출력 2 : 공이 들어있지 않은 바구니는 0을 출력한다.

# 일단 문제자체가 이해가 안감..
"""
N, M = map(int, input().split())
baskets = [0] * (N+1) # N개의 바구니를 0으로 초기화한 배열

for _ in range(M) : # M번 동안
    x, y, i = map(int, input().split()) # x, y, i를 입력 받아서
    for j in range(x, y + 1) : # x부터 y까지의 바구니에
        baskets[j] = i # i 번호의 공을 넣음
for i in range(1, len(baskets)) : # 각 바구니에
    print(baskets[i], end=" ") # 어떤 공이 들어있는지 출력
"""

# -------------------------------------------------------------------------------------

# 6) 백준 10813
# 도현이는 바구니를 총 N개 가지고 있고,
# 각각의 바구니에는 1번부터 N번까지 번호가 매겨져 있다.
# 바구니에는 공이 1개씩 들어있고,
# 처음에는 바구니에 적혀있는 번호와 같은 번호가 적힌 공이 들어있다.
# 도현이는 앞으로 M번 공을 바꾸려고 한다.
# 도현이는 공을 바꿀 바구니 2개를 선택하고,
# 두 바구니에 들어있는 공을 서로 교환한다.
# 공을 어떻게 바꿀지가 주어졌을 때,
# M번 공을 바꾼 이후에 각 바구니에 어떤 공이 들어있는지 구하는 프로그램을 작성하시오.
# 입력 1 : 첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)이 주어진다.
# 입력 2 : 둘째 줄부터 M개의 줄에 걸쳐서 공을 교환할 방법이 주어진다.
# 입력 3 : 각 방법은 두 정수 i j로 이루어져 있으며,
# 입력 4 : i번 바구니와 j번 바구니에 들어있는 공을 교환한다는 뜻이다. (1 ≤ i ≤ j ≤ N)
# 입력 5 : 도현이는 입력으로 주어진 순서대로 공을 교환한다.
# 출력 : 1번 바구니부터 N번 바구니에 들어있는 공의 번호를 공백으로 구분해 출력한다.

# 7) 백준 5597
# X대학 M교수님은 프로그래밍 수업을 맡고 있다.
# 교실엔 학생이 30명이 있는데,
# 학생 명부엔 각 학생별로 1번부터 30번까지 출석번호가 붙어 있다.
# 교수님이 내준 특별과제를 28명이 제출했는데,
# 그 중에서 제출 안 한 학생 2명의 출석번호를 구하는 프로그램을 작성하시오.
# 입력 1 : 입력은 총 28줄로 각 제출자(학생)의 출석번호 n(1 ≤ n ≤ 30)가
# 입력 2 : 한 줄에 하나씩 주어진다. 출석번호에 중복은 없다.
# 출력 1 : 출력은 2줄이다. 1번째 줄엔 제출하지 않은 학생의 출석번호 중
# 출력 2 : 가장 작은 것을 출력하고, 2번째 줄에선 그 다음 출석번호를 출력한다.

# 8) 백준 3052
# 두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다.
# 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다.
# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다.
# 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.
# 입력 1 : 첫째 줄부터 열번째 줄 까지 숫자가 한 줄에 하나씩 주어진다.
# 입력 2 : 이 숫자는 1,000보다 작거나 같고, 음이 아닌 정수이다.
# 출력 : 첫째 줄에, 42로 나누었을 때, 서로 다른 나머지가 몇 개 있는지 출력한다.

# 9) 백준 10811
# 도현이는 바구니를 총 N개 가지고 있고,
# 각각의 바구니에는 1번부터 N번까지 번호가 순서대로 적혀져 있다.
# 바구니는 일렬로 놓여져 있고, 가장 왼쪽 바구니를 1번째 바구니, 그 다음 바구니를 2번째 바구니, ...,
# 가장 오른쪽 바구니를 N번째 바구니라고 부른다.
# 도현이는 앞으로 M번 바구니의 순서를 역순으로 만들려고 한다.
# 도현이는 한 번 순서를 역순으로 바꿀 때, 순서를 역순으로 만들 범위를 정하고,
# 그 범위에 들어있는 바구니의 순서를 역순으로 만든다.
# 바구니의 순서를 어떻게 바꿀지 주어졌을 때,
# M번 바구니의 순서를 역순으로 만든 다음,
# 바구니에 적혀있는 번호를 가장 왼쪽 바구니부터 출력하는 프로그램을 작성하시오.
# 입력 1 : 첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)이 주어진다.
# 입력 2 : 둘째 줄부터 M개의 줄에는 바구니의 순서를 역순으로 만드는 방법이 주어진다.
# 입력 3 : 방법은 i j로 나타내고, 왼쪽으로부터 i번째 바구니부터 j번째 바구니의 순서를
# 입력 4 : 역순으로 만든다는 뜻이다. (1 ≤ i ≤ j ≤ N)
# 입력 5 : 도현이는 입력으로 주어진 순서대로 바구니의 순서를 바꾼다.
# 출력 : 모든 순서를 바꾼 다음에, 가장 왼쪽에 있는 바구니부터 바구니에 적혀있는 순서를 공백으로 구분해 출력한다.

# 10) 백준 1546
# 세준이는 기말고사를 망쳤다.
# 세준이는 점수를 조작해서 집에 가져가기로 했다.
# 일단 세준이는 자기 점수 중에 최댓값을 골랐다.
# 이 값을 M이라고 한다. 그리고 나서 모든 점수를 점수/M*100으로 고쳤다.
# 예를 들어, 세준이의 최고점이 70이고, 수학점수가 50이었으면
# 수학점수는 50/70*100이 되어 71.43점이 된다.
# 세준이의 성적을 위의 방법대로 새로 계산했을 때,
# 새로운 평균을 구하는 프로그램을 작성하시오.
# 입력 1 : 첫째 줄에 시험 본 과목의 개수 N이 주어진다.
# 입력 2 : 이 값은 1000보다 작거나 같다. 둘째 줄에 세준이의 현재 성적이 주어진다.
# 입력 3 : 이 값은 100보다 작거나 같은 음이 아닌 정수이고, 적어도 하나의 값은 0보다 크다.
# 출력 1 : 첫째 줄에 새로운 평균을 출력한다.
# 출력 2 : 실제 정답과 출력값의 절대오차 또는 상대오차가 10-2 이하이면 정답이다.