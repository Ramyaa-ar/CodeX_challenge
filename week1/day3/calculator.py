print("....................Hey There....................")

def calc(a,b,op):
    if op=='+':
        return a+b
    elif op=='-':
        return a-b
    elif op=='*':
        return a*b
    elif op=='/':
        return a/b
    elif op=='%':
        return a % b
    else:
        return "Invalid operation"
print("Enter the values")
a,b=int(input()),int(input())
print("enter the operation")
op=input()
result=calc(a,b,op)
print(result)
