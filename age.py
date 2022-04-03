driving = input('請問您是否開過車？')
if driving != '有' and '沒有':
	print('抱歉！只能輸入 有/沒有')
	raise SystemExit   #觸發（raise）系統離開的錯誤(SystemExit)

age = input('請問您的年齡？')
age = int(age)  #Casting
if driving == '有':
	if age >= 18:
		print('你通過測驗了')
	else:
		print('抓到！偷開車喔～')
elif driving == '沒有':
	if age >= 18:
		print('你可以考駕照了，怎麼還不去考？')
	else:
		print('再過幾年就能考駕照了')
