logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
user = []
userleft = True
while userleft :
    name = input("What is your name : ")
    bid = int(input("What is your bid : $"))
    user.append([name,bid])
    more = input("Are there any other bidders ? Type 'yes' or 'no' : ")
    if more == "no":
        userleft = False
print("Auction finished the winner is : " + max(user)[0])
