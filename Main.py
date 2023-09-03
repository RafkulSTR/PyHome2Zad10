coins = [0, 1, 1, 0, 1]
heads = sum(coins) # количество монеток, лежащих решкой
tails = len(coins) - heads # количество монеток, лежащих гербом
print(min(heads, tails))
