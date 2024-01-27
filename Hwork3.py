# 1. ჯეირანის პროგრამა

# from random import randint

# hscore = 0
# cscore = 0

# while True:
#     hchoice = int(input("""
#     Choose Number:
#     1. Stone
#     2. Sciss
#     3. Paper
#     """))
#     cchoice = randint(1,3)
#     print(f'Score {hscore} : {cscore}' )

#     if hscore != 3 and cscore != 3:
#             if hchoice == cchoice:
#                 continue
#             elif (hchoice == 1 and cchoice == 2) or (hchoice == 2 and cchoice == 3) or (hchoice == 3 and cchoice == 1):
#                 hscore += 1
#             else:
#                 cscore += 1

#     elif hscore == 3:
#          print('You Win!')
#          break
#     else:
#          print('Computer Wins!')
#          break


# ///////////////////////////////////////////////

# 2. გამრავლების ტაბულა


# userwish = int(input("User Number: "))

# for i in range(1,userwish):
#     print(i, end="\t")
# print()

# for j in range(2,userwish):
#     for k in range(1,userwish):
#         print(j*k, end ="\t")
#     print("\n")


# /////////////////////////////////////////////////
# 3. საბანკო ანგარიში

# bank = 3000
# while bank >=0:
#     message = int(input("Gaweuli xarji: "))
#     if message == 0:
#         print(bank)
#         break
#     if bank - message >= 0:
#         bank -= message
#         print(bank)
#     else:
#         print('Arasakmarisi tanxa')
        
    

# /////////////////////////////////////////////
# 4. თუთიყუშის პროგრამა

# message=' '
# while message !='quit':
#     message=input("User said Whaaat?!: ")
#     if message=='quit':
#         break
#     print('User Said!'+message)