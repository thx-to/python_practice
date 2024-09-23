# 백준 - 문제 - 단계별로 풀어보기 - 3 - 반복문 (3/12)


# 1) 백준 2739
# N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.
# 입력 : 첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 9보다 작거나 같다.
# 출력 : 출력형식과 같게 N*1부터 N*9까지 출력한다.
"""
n = int(input())
for i in range(n,n+1) :
    for j in range(1, 10) :
        print(f"{i} * {j} = {i*j}")
    print()
"""

# 2) 백준 10950
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 입력 1 : 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 입력 2 : 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 출력 : 각 테스트 케이스마다 A+B를 출력한다.

T = int(input())
i = 1
sum = []
while (i <= T) :
    A, B = map(int,input().split())
    sum.append(A + B)
    i += 1
for j in sum :
    print(j)


"""
t = int(input())
for i in range(1, t+1) :
    list1 = list(map(int,input().split()))
    print(f"{list1[0]+list1[1]}")
"""

# 3) 백준 8393
# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.
# 입력 : 첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.
# 출력 : 1부터 n까지 합을 출력한다.
"""
n = int(input())
sum = 0
for i in range(1, n+1, 1) :
    sum += i
print(sum)
"""
