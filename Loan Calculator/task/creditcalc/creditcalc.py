import argparse
from math import ceil, log, floor


def is_plural(x):
    if x > 1:
        return True
    else:
        return False


def years(x):
    if is_plural(x):
        return f"{x} years"
    else:
        return f"{x} year"


def months(x):
    if is_plural(x):
        return f"{x} months"
    else:
        return f"{x} month"


parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
args = parser.parse_args()
tp = args.type
D = args.payment
P = args.principal
n = args.periods
i = args.interest


def judge(a, b, c, d):
    if d is None:
        return False
    if a is None:
        return "D"
    if b is None:
        return "P"
    if c is None:
        return "n"


def judge_positive(a, b, c, d):
    a_lst = [a, b, c, d]
    result = True
    for j in a_lst:
        if j is not None and j.isdigit() and float(j) < 0:
            result *= False
        else:
            result *= True
    return result


def floating(x):
    try:
        return float(x)
    except:
        return x


lst = list((D, P, n, i))
lst.count(None)
if len(lst) - lst.count(None) < 3 or tp not in ["annuity", "diff"] or not judge_positive(D, P, n, i):
    print("Incorrect parameters")
elif tp == "annuity":
    question = judge(D, P, n, i)

    lst = [floating(j) for j in lst]
    D = lst[0]
    P = lst[1]
    n = lst[2]
    i = lst[3] / 1200
    if question == 'n':
        month = ceil(log(D / (D - i * P), (1 + i)))
        year = month // 12
        last_month = month % 12
        if year == 0:
            print(f"It will take {months(last_month)} to repay this loan!")
        elif month == 0:
            print(f"It will take {years(year)} to repay this loan!")
        else:
            print(f"It will take {years(year)} and {months(last_month)} to repay this loan!")
        overpayment = D * month - P
        print(f"Overpayment = {overpayment}")

    elif question == "D":
        monthly_payment = ceil(P * i * (1 + i) ** n / ((1 + i) ** n - 1))
        last = P % monthly_payment
        if last == 0:
            print(f"Your monthly payment = {monthly_payment}")
        # else:
        #     print(f"Your monthly payment = {monthly_payment} and the last payment = {last}.")
        overpayment = monthly_payment * n - P
        print(f"Overpayment = {overpayment}")


    elif question == "P":
        P = floor(D / ((i * (1 + i) ** n) / ((1 + i) ** n - 1)))
        print(f"Your loan principal = {P}!")
        overpayment = D*n - P
        print(f"Overpayment = {overpayment}")
elif tp == "diff":
    if D is None:
        P = float(P)
        n = int(n)
        i = float(i) / 1200
        D = [0] * int(n)
        for j in range(n):
            D[j] = ceil(P / n + i * (P - (P * (j+1 - 1) / n)))
        overpayment = sum(D) - P
        for j in range(n):
            print(f"Month {j + 1}: payment is {D[j]}")
        print(f"Overpayment = {overpayment}")


    else:
        print("Incorrect parameters:D should not use with diff")
