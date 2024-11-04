def fib(n):
    global step_count
    step_count += 1
    if n<=1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def seq(n):
    seq=[]
    for n in range(n):
        seq.append(fib(n))
    return seq

n=int(input("Enter the number:- "))
step_count=0
result=fib(n)
print(f"Fibonacci({n}) = {fib(n)} , Steps = {step_count}")
print(f"Sequence = {seq(n)}")