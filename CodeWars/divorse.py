def divisors(integer):
    xs = [i for i in range(2, integer) if integer % i == 0]
    if xs:
        return xs
    else:
        return f"{integer} is prime"


print(divisors(13)) #should return [2,3,4,6]