# Первая строка входа содержит число операций 1≤n≤10^5
# Каждая из последующих nn строк задают операцию одного из следующих двух типов:
# 
#     InsertInsert xx, где 0≤x≤10^9 — целое число;
#     ExtractMaxExtractMax.
# 
# Первая операция добавляет число xx в очередь с приоритетами,
# вторая — извлекает максимальное число и выводит его.

###########################################
# Sample Input:
# 
# 6
# Insert 200
# Insert 10
# ExtractMax
# Insert 5
# Insert 500
# ExtractMax
########################################### 
# Sample Output:
# 
# 200
# 500

from heapq import heappush, heappop


    

def main():
    operation_amount = int(input())
    operations = [args for args in (input().split() for _ in range(operation_amount))]
    init_heap = []

    for oper in operations:
        if oper[0] == 'ExtractMax':
            element = heappop(init_heap)
            print(-element)
        else:
            heappush(init_heap, -int(oper[1])) 


    
if __name__ == "__main__":
    main()

