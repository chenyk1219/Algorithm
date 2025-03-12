import time


def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
    for cents in range(1, change + 1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
                newCoin = j
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
    return minCoins[change]


def printCoins(coinsUsed, change):
    cion = change
    while cion > 0:
        thisCoin = coinsUsed[cion]
        print(thisCoin)
        cion = cion - thisCoin


print(time.process_time())
amnt = 63
clist = [1, 5, 10, 21, 25]
coinUsed = [0] * 64
coinCount = [0] * 64
print(dpMakeChange(clist, amnt, coinCount, coinUsed))
printCoins(coinUsed, amnt)
print(coinUsed)
print(time.process_time())
