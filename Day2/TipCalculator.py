print ("Welcome to the tip calculator.")
totbill= float(input("What was the total bill ? \n$"))
pourctip = int(input("What percentage tip would you like to give ? 10, 12, or 15 ? \n"))
if pourctip in [10, 12, 15]:
    pourctip = 1+pourctip/100
    people = int(input("How many people to split the bill ? \n"))
    print("Each person should pay : " + str("{:.2F}".format(totbill/people*pourctip)))
else :
    print("error")

##

