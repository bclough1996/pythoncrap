#Greet the Customer 
print("Hello Alien Visitor, Welcome to Albert the Alien's Fiber Optic Megastore")
#Inputs by the User
CName = input("Please Enter Your Company's Name:")
FOLength = input("Please State the Length of Fiber Optic Needed: ")

#Logic
  
fFOLength = float(FOLength)
Cost = float()
if(fFOLength > 500):
        Cost = float(.50)
elif(fFOLength > 250):
         Cost = float(.70)
elif(fFOLength > 100):
        Cost = float(.80)
else:
         Cost = float(.87)
    
Total = float
Total = fFOLength * Cost
#Display
print("Total amount:" + str(Total))
print(f"Thank You {CName.title()}  for Your Continued Patronage")
