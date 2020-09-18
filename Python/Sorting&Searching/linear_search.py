Array = ["James", "Joe", "Sam", "Gerald", "Cory"]
NSF = False
NS = input("Enername")

for i in Array:
    if i == NS:
        print("found")
        NSF = True
if NSF == False:
    print("Notfound adding name")
    Array.append(NS)


