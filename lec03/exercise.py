h = 0.5 
f_approx = [1] 
df = [0] 
ddf = lambda n: -f_approx(n) 

for i in range(0, 2): 
    # Eular method: f(x+h) = f(x) + df(x) 
    df.append(df[i] + ddf[i])
    f_approx.append[f_approx[i] + df[i]]
