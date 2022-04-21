n, m = map(int, input().split())
wanted_candles = list(map(int, input().split()))
index_array = []
length = len(wanted_candles)
for i in range(len(wanted_candles)):
    index_array.append(i)
j = 0
while(len(wanted_candles) != 1):
    if(wanted_candles[0] > m):
        temp1 = wanted_candles[0]-m
        wanted_candles.remove(wanted_candles[0])
        wanted_candles.append(temp1)
        temp2 = index_array[0]
        index_array.remove(index_array[0])
        index_array.append(temp2)
    else:
        wanted_candles.remove(wanted_candles[0])
        index_array.remove(index_array[0])
    j += 1
print(index_array[0]-1)
