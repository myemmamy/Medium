# HackerLand National Bank has a simple policy for warning clients about possible fraudulent account activity.
# If the amount spent by a client on a particular day is greater than or equal to 2x the client's median spending for a trailing number of days,
# they send the client a notification about potential fraud. The bank doesn't send the client any notifications until they have at least that trailing
# number of prior days' transaction data.
#
# Given the number of trailing days  and a client's total daily expenditures for a period of  days,
# determine the number of times the client will receive a notification over all  days.
# Exammple
# expenditure = [10,20,30,40,50]
# d = 3
# if keep sort, it will be very very slow,  so use disect which is bisection algorithm so it's fast

import bisect
def activityNotifications(expenditure, d):
    nums=0
    index=int(d/2)
    sortedarr = sorted(expenditure[:d])
    for i in range(d,len(expenditure)):
        median = sortedarr[index] if d % 2 != 0 else (sortedarr[index-1]+sortedarr[index])/2
        if expenditure[i] >= median*2:
            nums += 1
        del sortedarr[bisect.bisect(sortedarr,expenditure[i-d])-1]
        bisect.insort(sortedarr, expenditure[i])
    return nums

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)
    print(result)
