list=[1, 3]
for n in range(2, 500):
    fn=5*list[n-1]+list[n-2]
    list.append(fn)
list=[n for n in list if n%2!=0]
print(list[39])