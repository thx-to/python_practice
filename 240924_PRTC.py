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
"""

"""
# 백준 1260
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력 : 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
출력 : 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다.
V부터 방문된 점을 순서대로 출력하면 된다.

예제 입력 1 :
4 5 1
1 2
1 3
1 4
2 4
3 4
예제 출력 1 : 
1 2 4 3
1 2 3 4
"""

"""
# 백준 2751
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력 : 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다.
둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
출력 : 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

예제 입력 1 : 
5
5
4
3
2
1
예제 출력 1 : 
1
2
3
4
5
"""

"""
# 백준 10989
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력 : 첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다.
둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.
출력 : 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

예제 입력 1 :
10
5
2
3
1
4
2
3
5
1
7
예제 출력 1 : 
1
1
2
2
3
3
4
5
5
7
"""

"""
# 백준 1463
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
2. X가 2로 나누어 떨어지면, 2로 나눈다.
3. 1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다.
연산을 사용하는 횟수의 최솟값을 출력하시오.

입력 : 첫째 줄에 1보다 크거나 같고, 10^6보다 작거나 같은 정수 N이 주어진다.
출력 : 첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.

예제 입력 1 : 2
예제 출력 1 : 1
"""

"""
# 백준 25083
아래 예제와 같이 새싹을 출력하시오.

입력 : 입력은 없다.
출력 : 새싹을 출력한다.

예제 입력 1 : 
예제 출력 1 :
         ,r'"7
r`-_   ,'  ,/
 \. ". L_r'
   `~\/
      |
      |
      
"""

"""
# 백준 10809
알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서,
단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

입력 : 첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.
출력 : 각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.
만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다. 단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.

예제 입력 1 : baekjoon
예제 출력 1 : 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
"""

"""
# 백준 1920
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

입력 : 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다.
다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다.
모든 정수의 범위는 -2^31 보다 크거나 같고 2^31보다 작다.
출력 : M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

예제 입력 1 :
5
4 1 5 2 3
5
1 3 7 9 5
예제 출력 1 :
1
1
0
0
1
"""

"""
# 백준 9086
문자열을 입력으로 주면 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 작성하시오.

입력 : 입력의 첫 줄에는 테스트 케이스의 개수 T(1 ≤ T ≤ 10)가 주어진다.
각 테스트 케이스는 한 줄에 하나의 문자열이 주어진다.
문자열은 알파벳 A~Z 대문자로 이루어지며 알파벳 사이에 공백은 없으며 문자열의 길이는 1000보다 작다.
출력 : 각 테스트 케이스에 대해서 주어진 문자열의 첫 글자와 마지막 글자를 연속하여 출력한다.

예제 입력 1 :
3
ACDKJFOWIEGHE
O
AB
예제 출력 1 :
AE
OO
AB
"""

"""
# 백준 5597
X대학 M교수님은 프로그래밍 수업을 맡고 있다. 교실엔 학생이 30명이 있는데, 학생 명부엔 각 학생별로 1번부터 30번까지 출석번호가 붙어 있다.
교수님이 내준 특별과제를 28명이 제출했는데, 그 중에서 제출 안 한 학생 2명의 출석번호를 구하는 프로그램을 작성하시오.

입력 : 입력은 총 28줄로 각 제출자(학생)의 출석번호 n(1 ≤ n ≤ 30)가 한 줄에 하나씩 주어진다. 출석번호에 중복은 없다.
출력 : 출력은 2줄이다. 1번째 줄엔 제출하지 않은 학생의 출석번호 중 가장 작은 것을 출력하고, 2번째 줄에선 그 다음 출석번호를 출력한다.

예제 입력 1 :
3
1
4
5
7
9
6
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
예제 출력 1 :
2
8
"""

"""
# 백준 2675
문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.
즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.
QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

입력 : 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다.
각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다. S의 길이는 적어도 1이며, 20글자를 넘지 않는다. 
출력 : 각 테스트 케이스에 대해 P를 출력한다.

예제 입력 1 :
2
3 ABC
5 /HTP
예제 출력 1 :
AAABBBCCC
/////HHHHHTTTTTPPPPP
"""

"""
# 백준 2606
신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다.
한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.
예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자.
1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다.
하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.
1 - 2 - 3  4
 \ /      / 
  5 - 6  7
어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때,
1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

입력 : 첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하인 양의 정수이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다.
둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다.
이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.
출력 : 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.

예제 입력 1 :
7
6
1 2
2 3
1 5
5 2
5 6
4 7
예제 출력 1 : 4
"""