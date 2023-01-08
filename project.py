i = input("Enter a sentence")

count = 1
li = list(b.split(" "))

j  = 0

while(j<len(i)):
	if(i[j] == " "):  
		count+=1
	j += 1	

realCount = (count+1)
main = " "
for v in range(realCount):
	main = main+li[v][0]

print("Acronym is: ",main.upper())
