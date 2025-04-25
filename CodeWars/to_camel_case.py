
import re
def to_camel_case(text):
    splitted = re.split('_|-',text)
    return splitted[0] + "".join(list(map(lambda x : x.capitalize(), splitted[1:])))
    

print(to_camel_case("the_stealth_warrior"))