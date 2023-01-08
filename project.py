i = input("Enter a sentence")

count = 1
li = list(i.split(" "))

j  = 0

while(j<len(i)):
	if(i[j] == " "):  
		count+=1
	j += 1	

realCount = (count)
main = " "
for v in range(realCount):
	main = main+li[v][0]

print("Acronym is: ",main.upper())
