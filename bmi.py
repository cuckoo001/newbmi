height = input('请输入你的身高（cm)：')
weight = input('请输入你的体重(kg)：')
height = int(height)
weight = int(weight)
height = height / 100  #换成公尺
bmi = weight / height / height
if bmi < 18.5:
	print('你的bmi值为', bmi, '过轻')
	
elif bmi >= 18.5 and bmi < 24:
	print('你的bmi值为', bmi, '正常')
elif bmi >= 24 and bmi < 27:
	print('你的bmi值为', bmi, '稍重')
elif bmi >=27 and bmi < 30:
	print('你的bmi值为', bmi, '轻度肥胖')
elif bmi >= 30 and bmi < 35:
	print('你的bmi值为', bmi, '中度肥胖')
elif bmi >= 35: #写else:也可以
	print('你的bmi值为', bmi, '重度肥胖')

