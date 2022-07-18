# put your python code here

d = {
    1: "AEILNORSTU",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ"
}
s = input()
sum = 0
for i in s:
    for key,value in d.items():
        if(i in value):
            sum += key
print(sum) 


