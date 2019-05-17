country = input("你的國家？")
age = input("你的年齡？")
age = int(age)
if country == "臺灣":
	if age >= 18:
		print("你可以在臺灣考駕照")
	else:
		print("你還不能在臺灣考駕照")
if country == "美國":
	if age >= 20:
		print("你可以在美國考駕照")
	else:
		print("你還不能在美國考駕照")

