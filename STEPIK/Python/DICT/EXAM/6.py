# print(build_query_string({'name': 'timur', 'age': 28}))
# print(build_query_string({'sport': 'hockey', 'game': 2, 'time': 17}))
# должен выводить:
# age=28&name=timur
# game=2&sport=hockey&time=17

def build_query_string(params):
    print('&'.join(sorted([str(key) + '=' + str(value)  for key,value in params.items()])))

