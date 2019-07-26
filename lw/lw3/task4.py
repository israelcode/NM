x = [0.0, 0.5, 1.0, 1.5, 2.0]
y = [1.0, 1.3776, 1.5403, 1.5707, 1.5839]
x0 = 1.0

k = 0
for i, j in zip(x, x[1:]):
    if i <= x0 <= j:
        break
    k += 1



result1 = (y[k + 1] - y[k]) / (x[k + 1] - x[k])
result2 = (y[k + 2] - y[k + 1]) / (x[k + 2] - x[k + 1]) - result1
result2 = result2 / (x[k + 2] - x[k])    
ans1 = result1 + result2 * (2 * x0 - x[k] - x[k + 1])

result1 = (y[k + 2] - y[k + 1]) / (x[k + 2] - x[k + 1])
result2 = (y[k + 1] - y[k]) / (x[k + 1] - x[k])    
ans2 = 2 * (result1 - result2) / (x[k + 2] - x[k])
    

print('Первая производная', ans1)
print('Вторая производная', ans2)

