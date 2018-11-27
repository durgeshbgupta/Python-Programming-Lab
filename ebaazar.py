from easygui import *
import sys

while 1:
    msgbox("Welcome to e bazar")

    msg ="In which category you want to buy items?"
    title = "Gmart Bazaar"
    choices=["Mobiles", "Clothes", "Computer Accesories", "TV Appliances"]
    choice = choicebox(msg, title, choices)
     
    msgbox("You chose: " + str(choice), "Confirm your choice")

    msg = "Do you want to continue?"
    title = "Please Confirm"
    if choice=="Mobiles":
        msgbox("Welcome to Mobiles bazaar")
        msg="Which Mobiles?"
    	title= "Gmart Mobiles Bazaar"
    	choices= ["Y 1---price=12500", "Y 2---price=20000", "Y 3---price=15200", "Y 4---price---17500"]
    	choice= choicebox(msg, title, choices)

        msgbox("You chose: " + str(choice), "Confirm your choice")

        msg = "Is it your final choice(Press continue to deliver at your default address)?"
        title = "Please Confirm"
        msgbox("Thank you for buying at Gmart Bazaar")
    elif choice=="Clothes":
        msgbox("Welcome to Clothes bazaar")
        msg="What type of Clothes?"
    	title= "Gmart  Clothes Bazaar"
    	choices= ["Shirt Mens-L size-----Rs 500","Shirt Children-M size-----Rs 1000","Jeans Pant forMens-----Rs2500","Jeans Pant for Children-----Rs2700"]
    	choice= choicebox(msg, title, choices)

        msgbox("You chose: " + str(choice), "Confirm your choice")

        msg = "Is it your final choice(Press continue to deliver at your default address)?"
        title = "Please Confirm"
        msgbox("Thank you for buying at Gmart Bazaar")
    elif choice=="Computer Accesories":
        msgbox("Welcome to Computer Accesories bazaar")
        msg="Which Computer Accesories?"
    	title= "Gmart  Computer Accesories Bazaar"
    	choices= ["Monitor			 Price=18000", "CPU price=27000"]
    	choice= choicebox(msg, title, choices)

        msgbox("You chose: " + str(choice), "Confirm your choice")

        msg = "Is it your final choice(Press continue to deliver at your default address)?"
        title = "Please Confirm"
        msgbox("Thank you for buying at Gmart  Bazaar")
    elif choice=="TV Appliances":
        msgbox("Welcome to TV Appliances bazaar")
        msg="Choose your item?"
    	title="Gmart  TV Appliances Bazaar"
    	choices= ["Sony TV Special Edition pack of 5 ---- price=Rs49000 ", "Whirpool Appliances Pack of 10----- price=Rs55000"]
    	choice= choicebox(msg, title, choices)

        msgbox("You chose: " + str(choice), "Confirm your choice")

        msg = "Is it your final choice(Press continue to deliver at your default address)?"
        title = "Please Confirm"
        msgbox("Thank you for buying at Gmart  Bazaar")

    if ccbox(msg, title):    
        pass  
    else:
        sys.exit(0)			
