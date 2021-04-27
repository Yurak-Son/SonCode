list = [95, 99887,8,9133,9188,9,99999]
str_list = []

for i in list:
    str_list.append(str(i))

print(str_list)

def Rank_check(list):
    for i in range(len(list)):
        sel = i
        str_index = 0
        for j in range(i+1, len(list)):
            if list[sel][str_index] < list[j][str_index]:
                sel = j
            try:
                while(list[sel][str_index] == list[sel][str_index]):
                    if list[sel][str_index] < list[j][str_index]:
                        sel = j
                        break
                    elif list[sel][str_index] > list[j][str_index]:
                        break
                    str_index = str_index+1
                str_index = 0
            except :
                print("error")
                if len(list[sel]) > len(list[j]):
                    sel = j
                str_index = 0
        temp = list[sel]
        list[sel] = list[i]
        list[i] = temp

    return list

print(Rank_check(str_list))
