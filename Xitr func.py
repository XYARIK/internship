t=0
fn=0
list=[]
for n in range(2, 10000):
    t=str(n)[::-1].lstrip("0")
    t=int(t[::-1])
    fn=t/n
    if fn not in list:
        list.append(fn)

print(list)