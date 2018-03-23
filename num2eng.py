from math import floor

def float_to_string(number, precision=30):
    return '{0:.{prec}f}'.format(number, prec=precision,).rstrip('0').rstrip('.') or '0'

def num2EngWords(num , join = True):
	unit= ["","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"]
	teen= ["","ELEVEN","TWELVE","THIRTEEN","FOURTEEN","FIFTEEN","SIXTEEN","SEVENTEEN","EIGHTEEN","NINTEEN"]
	ten= ["","TEN","TWENTY","THIRTY","FOURTY","FIFTY","SIXTY","SEVENTY","EIGHTY","NINTY"]
	           #     3+1       6+1       9+1       12+1          15+1          18+1       21+1            24+1       27+1         30+1 
	thousand=["","THOUSAND","MILLION","BILLION","TRILLION","QUADRILLION","QUINTILLION","SEXTILLION","SEPTILLION","OCTILLION","NONILLION"]

	num2words = []
	decimalNum2words = []

	if type(num) == float:
		decimalNum = (num) - (int(num))
		decimalNum = '{:f}'.format(decimalNum)
		decimalNum = decimalNum[2:]	
		num =  int(num)
		print(num)
		decimalNum = decimalNum.rstrip('0')
		if len(decimalNum)>1:
			for i in decimalNum:
				if int(i) ==0:
					decimalNum2words.append("ZERO")
				else:
					decimalNum2words.append(unit[int(i)])
		elif len(decimalNum)==1:
			if int(decimalNum)!=0:
				decimalNum2words.append(unit[int(decimalNum)])
			else:
				pass			
		else:
			pass		
	if num == 0:
		num2words.append("ZERO")
	else:
		numInStr = str(num)
		numLen  = len(numInStr)
		groups = floor((numLen+2)/3)	
		numInStr = numInStr.zfill(groups*3)
		for i in range(0,len(numInStr),3):
			h,t,u = int(numInStr[i]),int(numInStr[i+1]),int(numInStr[i+2])
			g = groups - (i/3)-1
			g = int(g)
			if h >= 1 :
				num2words.append(unit[h])
				num2words.append("HUNDRED")
			if t>1:
				num2words.append(ten[t])
				if u>=1:
					num2words.append(unit[u])
			elif t==1:
				if u>=1:
					num2words.append(teen[u])
				else:
					num2words.append(ten[t])
			else:
				if u>=1:
					num2words.append(unit[u])
			if g>=1 and (h+t+u)>0:
				num2words.append(thousand[g]+ ',')
#decimal
	b = (' '.join(decimalNum2words) )
	if join:
		a = (' '.join(num2words))
		if not b:
			return(a)
		else:
			return(a+' point '+b)	
	if not b:
		return(num2words)
	else:			
		return(num2words +['.']+ decimalNum2words)
												
n =float(input().strip())
print(num2EngWords(n, join=False))



					


