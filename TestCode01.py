print("Hellow world!!")

list = [99887,8,9188,9133,9,5]
rank_list = []
str_list = []

for i in list:
    str_list.append(str(i))

print(str_list)

def Rank_index(rank_list, value):
    cnt = 0
    for i in rank_list:
        if i == value:
            break
        cnt = cnt+1

    return cnt

def Rank_check(list):
    for i in range(len(list)):
        sel = i
        z = 0
        for j in range(i+1, len(list)):
            if list[sel][z] < list[j][z]:
                sel = j
            elif(list[sel][z] == list[j][z]):
                print("T")
        temp = list[sel]
        list[sel] = list[i]
        list[i] = temp
        print(list)

    return list



print(Rank_check(str_list))
