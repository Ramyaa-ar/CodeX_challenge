print("....................Hey There....................")

while True:

    exp=input("Enter ur expression>")
    if exp.lower()=='exit':
        break
    try:
        res=eval(exp)
        print(res)
    except Exception as e:
        print("syntactic error")
