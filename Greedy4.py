
def change(n,koin_tersedia, coins_so_far):
    if sum(coins_so_far) == n:
        yield coins_so_far
    elif sum(coins_so_far) > n:
        pass
    elif koin_tersedia == []:
        pass
    else:
        for c in change(n, koin_tersedia[:], coins_so_far+[koin_tersedia[0]]):
            yield c
        for c in change(n, koin_tersedia[1:],coins_so_far):
            yield c
n = int(input())
coins = [1,2,5,10,25]

solutions = [s for s in change(n, coins, [])]
for s in solutions:
    print (s)

print (('solusi paling optimal:'), min(solutions, key=len))

