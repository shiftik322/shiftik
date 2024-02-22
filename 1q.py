from typing import Tuple
from math import sqrt


def four_squares(n: int) -> Tuple[int, int, int, int]:
    a, b, c, d = 1, 1, 1, 1
    l = 2
    print(n)
    count = 1
    while n > l:
        l = l ** 2
        count += 1
    if n > 8172563489612398569287356987162387946897236498761239874612987346:
        a = 10 ** (int(len(str(n)) / 2))
        for i in range(count * 1000):
            a -= 1
            n1 = n - a ** 2
            if n1 < 0:
                #             a -= int(sqrt(a**2-n))
                #             print('fail', a)
                continue

            #         print(a)
            b = int(sqrt(float(n1))) + 1
            for j in range(count * 50):
                b -= 1
                n2 = n1 - b ** 2
                if n2 < 0:
                    #                   b -= int(sqrt(b**2-n1))
                    #                     print('fail b',b)
                    continue

                c = int(sqrt(float(n2))) + 1
                for z in range(count * 10):
                    c -= 1
                    n3 = n2 - c ** 2
                    if n3 < 0:
                        #                       c -= int(sqrt(c**2-n2))
                        #                         print('fail 2')
                        continue

                    d = int(sqrt(float(n3)))
                    if (n - (a ** 2 + b ** 2 + c ** 2 + d ** 2)) == 0:
                        return a, b, c, d

    a = int(sqrt(float(n))) + 1
    for i in range(count * 1000):
        a -= 1
        n1 = n - a ** 2
        if n1 < 0:
            #             a -= int(sqrt(a**2-n))
            #             print('fail', a)
            continue

        #         print(a)
        b = int(sqrt(float(n1))) + 1
        for j in range(count * 50):
            b -= 1
            n2 = n1 - b ** 2
            if n2 < 0:
                #                 b -= int(sqrt(b**2-n1))
                print('fail', b)
                if b < 0:
                    break
                continue

            c = int(sqrt(float(n2))) + 1
            for z in range(count * 10):
                c -= 1
                n3 = n2 - c ** 2
                if n3 < 0:
                    #                     c -= int(sqrt(c**2-n2))
                    print('fail 2')
                    if c < 0:
                        break
                    continue

                d = int(sqrt(float(n3)))
                if (n - (a ** 2 + b ** 2 + c ** 2 + d ** 2)) == 0:
                    return a, b, c, d