import random
import copy

N = random.randrange(1,11)
print(N)
User_NumberOf = 5
Stage_list = []
Fail_list = []
Rank_list = []

for i in range(User_NumberOf):
    Stage_list.append(random.randrange(1,N+1))

print(Stage_list)

cnt1 = 0
cnt1_list = []
for i in range(1,N+1):
    for j in Stage_list:
        if i == j:
            cnt1 = cnt1 + 1
    cnt1_list.append(cnt1)
    cnt1 = 0
#print(cnt1_list)

cnt2 = 0
cnt2_list = []
for i in range(len(cnt1_list)):
    for j in range(i, len(cnt1_list)):
        cnt2 = cnt2 + cnt1_list[j]
    cnt2_list.append(cnt2)
    cnt2 = 0
#print(cnt2_list)

Fail_list_false = []
for i in range(len(cnt2_list)):
    try:
        ans = cnt1_list[i]/cnt2_list[i]
        if ans == 0:
            ans = 1.0
    except ZeroDivisionError:
        ans = 0
    Fail_list.append(ans)
#print(Fail_list)
Fail_list_false = copy.deepcopy(Fail_list)

Fail_list.sort(reverse=True)

Fail_list_True = []
for i in Fail_list:
    if i not in Fail_list_True:
        Fail_list_True.append(i)
#print(Fail_list_True)

for i in range(len(Fail_list_True)):
    for j in range(len(Fail_list_false)):
        if Fail_list_True[i] == Fail_list_false[j]:
            Rank_list.append(j+1)
        else:
            pass

print(Rank_list)
