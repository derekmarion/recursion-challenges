def factorial(x):
	if x == 0:
		return 1
	return x * factorial(x - 1)

def palindrome(string):
	if len(string) <= 1:
		return True
	elif string[0] == string[-1]:
		return palindrome(string[1:-1])
	else:
		return False

def bottles(num, end):
	if num == 0:
		print("No more bottles of beer on the wall, no more bottles of beer.")
		print(f"Go to the store and buy some more, {end} bottles of beer on the wall.")	
		return "Great success!"
	if num != 1:
		print(f"{num} bottles of beer on the wall, {num} bottles of beer.")
	else:
		print(f"{num} bottle of beer on the wall, {num} bottle of beer.")
	if num > 0:
		print(f"Take one down and pass it around, {num -1} bottles of beer on the wall.")
	return bottles(num - 1, end)

def roman_num(num, i, output):
	romanNumeralToArabic = {
		"I": 1,
		"IV": 4,
		"V": 5,
		"IX": 9,
		"X": 10,
		"XL": 40,
		"L": 50,
		"C": 100,
		"CD": 400,
		"D": 500,
		"CM": 900,
		"M": 1000,
	}
	romanNumeralPriorityOrder = [
		"M",
		"CM",
		"D",
		"CD",
		"C",
		"L",
		"XL",
		"X",
		"IX",
		"V",
		"IV",
		"I",
	]
	numeral = romanNumeralPriorityOrder[i]
	quantity = num // romanNumeralToArabic[numeral] #note use of // division operator to enforce int. otherwise will return float and break logic
	if quantity > 0:
		k = quantity
		while k > 0:
			output += numeral
			num -= romanNumeralToArabic[numeral]
			k -= 1
		if num == 0: #Base case
			return output
		else:
			return roman_num(num, i + 1, output)
	else:
		return roman_num(num, i + 1, output)