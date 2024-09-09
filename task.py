from flask import Flask

app=Flask(__name__)

@app.route('/hi/<a>')
def fun1(a):
    return 'Hello '+a



@app.route('/larg/<int:a>/<int:b>/<int:c>')
def fun2(a,b,c):
    if a>b and a>c:
        return 'Largect is : '+str(a)
    elif b>a and b>c:
        return 'Largest is : '+str(b)
    elif c>a and c>b:
        return 'Largest is : '+str(c)

    else:
        return 'All are equal' 
    
@app.route('/rev/<int:a>')
def fun3(a):
    r=0
    while a>0:
        no=a%10
        r=(r*10)+no
        a=a//10
    return 'Reverse is : '+str(r)



@app.route('/strrev/<a>')
def fun4(a):
    # r=""
    # for a in str(a)[::-1]:
    #     r=r+str(a)
    return 'Reverse is '+a[::-1]
app.run()