from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/hi/<a>')
def fun1(a):
    return 'Hello '+a


##### largest in two input
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


##### REVERSE OF A INPUT
@app.route('/strrev/<a>')
def fun4(a):
    # r=""
    # for a in str(a)[::-1]:
    #     r=r+str(a)
    return 'Reverse is '+a[::-1]


####TEMPLATE DISPLAY
@app.route('/home',methods=['POST','GET'])
def home():
    if request.method=="POST":
        name=request.form["name"]
        place=request.form['place']
        print(name,place)
    return render_template('home.html')
    
@app.route('/page1')
def page1():
    return render_template('page1.html')
@app.route('/page2')
def page2():
    return render_template('page2.html')



### ELECTRICITY BILL
@app.route('/bill',methods=['POST','GET'])
def bill():
    charge=''
    if request.method=="POST":
        unit=int(request.form["unit"])
        if unit<=100:
            charge="no charges"
        elif unit<=200:  
            charge=(unit-100)*5
        else:
            charge=(unit-200)*10+500
    return render_template('bill.html',charge=charge)

#### monument of city
@app.route('/city',methods=['POST','GET'])
def city():
    mon=''
    if request.method=="POST":
        city=request.form["city"]
        if city=="delhi":
            mon="Red Fort"
        elif city=="agra":
            mon="Taj Mahal"
        elif city=="jaipur":
            mon="Jal Mahal"

        else:
            print(' no monument found')  
    return render_template('city.html',mon=mon)


##### date
@app.route('/day',methods=['POST','GET'])
def day():
    days=''
    if request.method=="POST":
        day=int(request.form["day"])
        if day==1:
            days=' sunday'
        elif day==2:
            days=' monday'
        elif day==3:
            days=' tuesday'
        elif day==4:
            days=' wednesday' 
        elif day==5:
            days=' thursday' 
        elif day==6:
            days=' friday' 
        elif day==7:
            days=' saturday' 

        else:
            days=' invalid input'

    return render_template('day.html',days=days)

##### Tax
@app.route('/tax',methods=['POST','GET'])
def tax():
    tax_percentage=''
    if request.method=="POST":
        costprice=int(request.form["costprice"])

        if costprice > 100000:
                tax_percentage = 0.15 * costprice
                # print("your tax is : ",tax_percentage)
        elif costprice > 50000:
                tax_percentage = 0.10 * costprice
                # print("your tax is : ",tax_percentage)
        else:
                tax_percentage = 0.05 * costprice
                # print("your tax is : ",tax_percentage)

    return render_template('tax.html',tax_percentage=tax_percentage)


#### Salary bonus
@app.route('/bonus',methods=['POST','GET'])
def bonus():
    bonus_amount=''
    if request.method=="POST":
        year=int(request.form["year"])
        salary=int(request.form["salary"])
        if year >5:
            bonus_amount = 0.05 * salary
            # print("Congratulations! You are eligible for a bonus.")
            # print("Your net bonus amount is : RS ",bonus_amount)
            # print("Your total amount is : RS ",bonus_amount+salary)
        else:
            # print("Sorry, you are not eligible for a bonus at this time.")
            bonus_amount = 'You are not eligible'

    return render_template('bonus.html',bonus_amount=bonus_amount)


@app.route('/lastdigit',methods=['POST','GET'])
def lastdigit():
    lastnum=''
    if request.method=="POST":
        lastdigit=int(request.form["lastdigit"])
        if lastdigit % 3 == 0:
            lastnum="The last digit of the number is divisible by 3."
        else:
            lastnum="The last digit of the number is not divisible by 3."
    return render_template('lastdigit.html',lastnum=lastnum)

    


app.run()


