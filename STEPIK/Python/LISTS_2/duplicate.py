# наговнокодил, более правильный вариант снизу

# put your python code here
# разделили список, чтобы не считать пробелы
###########################33
s = input().split()
print(s)

######################################
# финальный список символов 
# тип список списков
#####################################
list_final_char = []

i = - 1

# массив по каждой букве
while i < (len(s) - 2):
    
    i += 1
    ###############################
    # список внутри списка, на каждом 
    # повторение обновляется
    ###############################
    list_char_repeat = []
    
    ###############################
    # проверка на одиночные буквы
    ###############################
    if (s[i] != s[i + 1]) and (s[i] != s[i - 1]) :
        list_final_char.append([s[i]])

    ###############################
    ## блок с повторами
    ###############################
    else:        
        for k in range(i, len(s) - 1):
            if(s[k] == s[k + 1]) or (s[k] == s[k - 1]):
                list_char_repeat.append(s[k])
            else:
                
                break
            i = k 
        ###############################
        # добавили список
        ############################### 
        if(len(list_char_repeat) > 0):
            list_final_char.append(list_char_repeat)

print(list_final_char)


#######################################################################
#######################################################################
#######################################################################
##*******************************************************************##
#######################################################################
#######################################################################
#######################################################################


res = []

for el in input().split():
    if res and el in res[-1]:
        res[-1].append(el)
    else:
        res.append([el])

print(res)