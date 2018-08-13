print("Calcolatrice\nby alex3025\n")
save_result = False

def result_show():
	if save_result == True:
		print("\nRisultato: " + result_2)
	elif save_result == False:
		print("\nRisultato: " + result_1)
		
while True:
	try:
		if save_result == False:
			num1 = float(input("Inserire il primo numero: "))
		operator = input("Inserire il segno di operazione: ")
		num2 = float(input("Inserire il secondo numero: "))
		
		if operator == "+":
			if save_result == False:
				result_1 = str(num1 + num2)
				result_show()
			elif save_result == True:
				result_2 = str(float(result_1) + num2)
				result_show()
		elif operator == "-":
			if save_result == False:
				result_1 = str(num1 - num2)
				result_show()
			elif save_result == True:
				result_2 = str(float(result_1) - num2)
				result_show()
		elif operator == "*":
			if save_result == False:
				result_1 = str(num1 * num2)
				result_show()
			elif save_result == True:
				result_2 = str(float(result_1) * num2)
				result_show()
		elif operator == "/":
			if save_result == False:
				result_1 = str(num1 / num2)
				result_show()
			elif save_result == True:
				result_2 = str(float(result_1) / num2)
				result_show()
		else:
			print("\nSegno di operazione errato!\n")
	except ZeroDivisionError:
		print("\nImpossibile dividere per zero!\n")
	save_result = input("\nVuoi salvare il risultato per il calcolo successivo? (si/no): ")
	
	if save_result == True:
		print("\nIl primo numero è stato sostituito con il risultato dell'operazione precedente.\n")
	elif save_result == False:
		print("\nIl risultato non verrà memorizzato.\n")
