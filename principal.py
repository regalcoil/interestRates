pp = int(input("Principal $: "))
ii = float(input("Interest %: ")) / 100
tt = int(input("Years: "))
nn = int(input("Periods: "))

aa = 0

def intro():
	choice = input("Would you like 'simple' or 'compound' interest: ")
	choice.lower()
	if choice == "simple":
		simple()
	elif choice == "compound":
		compound()
	else:
		intro()
	print(" ")

def simple():
	i = 1
	while i < tt:
		print("Year " + str(i) + " $" + str(pp * (1+(ii*i))))
		i = i + 1
	aa = pp * (1+(ii*tt))
	print("Year " + str(tt) + " $" + str(aa))


def compound():
	i = 1
	while i < tt:
		print("Year " + str(i) + " $" + str(pp * (1+(ii/nn))**(nn*i)))
		i = i + 1
	aa = pp * (1+(ii/nn))**(nn*tt)
	print("Year " + str(tt) + " $" + str(aa))

intro()