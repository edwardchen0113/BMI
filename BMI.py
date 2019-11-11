x = hight = input('請輸入您的身高(cm)：')
y = wight = input('請輸入您的體重(kg)：')
x = float(x)
y = float(y)
BMI = y / ((x / 100) * (x / 100))
print('您的BMI為：',BMI)
if BMI < 18.5:
    print('您的體重過輕')
elif BMI >= 18.5 and BMI < 24:
    print('您的體重正常')
elif BMI >= 23 and BMI < 27:
    print('您的體重過重')
elif BMI >= 27 and BMI < 30:
	print('您的體重屬輕度肥胖')
elif BMI >= 30 and BMI < 35:
    print('您的體重屬中度肥胖')
else:
    print('您的體重屬重度肥胖')