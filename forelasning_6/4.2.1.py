"""

1. Skriv en funktion som tar två tal som argument och sedan returnerar
summan av divisionsrester mellan alla tal upp till det första och det andra.
Det vill säga:
1%k + 2%k + 3%k + ::: + n%k
där ::: betyder att det kan vara hur många termer som helst, och % betecknar
modulusoperatorn. Till exempel, om n = 7 och k = 3 så får vi:
1%3 + 2%3 + 3%3 + 4%3 + 5%3 + 6%3 + 7%3 =
1 + 2 + 0 + 1 + 2 + 0 + 1 =
7
gör lösningen genom rekursion, det vill säga en funktion som anropar sig
själv

"""

ret_value = 0


def rekursion(n, k):
    global ret_value

    if n <= 0:
        return ret_value
    else:
        ret_value += n % k
        print(f" + {n % k}")
        rekursion(n-1, k)
    return ret_value


print(rekursion(7, 3))
