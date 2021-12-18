import os

class Accounts():
    user_name=""
    password=""
    phone=""
    id=""
    age=""
    account_type=""
    def login(self,user_name,password):
        while True:
            with open("accountsfile",'r') as readfile:
                index = 0
                for line in readfile:
                    index += 1
                    if user_name in line :
                      print("user name success")
                      break
                for line in readfile:
                  index += 1
                  if password in line :
                    print("log in success")
                    return 1
                    break

                  else:
                        return 0

class admin(Accounts):
    def creat_account(self):

            with open("writefile.txt", 'a') as writefile:
                writefile.write(input("enter your name\n"))
                writefile.write("\n")
                writefile.write((input("enter your phone number\n")))
                writefile.write("\n")
                writefile.write(input("enter your password \n"))
                writefile.write("\n")
                writefile.write(input("enter your cash \n"))
                writefile.write("\n")
                writefile.write("-----------------------------------")
                print("created")
    def delete_account(self):
        with open("writefile.txt", 'r') as readfile:
            os.remove("writefile.txt")
            print("deleted")



print("")
ob1=Accounts()
ob2=admin()
while True:
    x=input("enter user name")
    y=input("enter password")
    if ob2.login(x,y) == 1 :
        print("WELCOME")
        ch=int(input("if you want create account enter 1 delete account 2"))
        if ch == 1:
            ob2.creat_account()
        if ch==2:
            ob2.delete_account()






