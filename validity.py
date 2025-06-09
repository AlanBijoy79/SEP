VIP_Status=input("Do you have VIP Status ticket?(Enter Yes/No)").lower()=="yes"
Valid_ticket=input("Do you have Valid ticket?(Enter Yes/No)").lower()=="yes"
can_enter=VIP_Status or Valid_ticket
if can_enter:
    print("You can enter")
else:
    print("You cannot enter")