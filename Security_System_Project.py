import random 
import os 
import smtplib
from email.message import EmailMessage 

def choice1_in_action():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("|-----------REGISTER------------~|")
    print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
    print()
    usrnme=input("Enter username : ").strip()
    if len(usrnme)==0:
        while len(usrnme)==0:
            print("Username is empty, it is mandatory field")
            usrnme=input("Enter username : ")
    print()
    passwd=input(f"Enter password for username {usrnme} : ")
    if len(passwd)==0:
        while len(passwd)==0:
            print("Password is empty, it is mandatory field")
            passwd=input(f"Enter password for username {usrnme} : ")
    with open("user_info.txt","w") as f:
        f.write(f"username : {usrnme}\npassword : {passwd}")
    f.close()
    print()
    print("Registration Successfully Completed")
    print()
# checking file exist or not
def check_file_exist():
    if os.path.exists("user_info.txt"):
        return True
    else:
        return False
# getting user data
def get_user_data():
    with open("user_info.txt","r") as f2:
        usr_dt=f2.readlines()
    f2.close()
    real_usr=usr_dt[0].strip()[11:]
    real_pass=usr_dt[1][11:]
    return [real_usr,real_pass]
# check if username is correct
def check_correct_username(real_usr):
    user_name=input("Enter your username : ")
    while len(user_name)==0:
        print("Username is empty, please enter it")
        user_name=input("Enter your username : ")
    print()
    if user_name==real_usr:
        return True
    return False
# check if password is correct
def check_correct_pass(real_pass):
    user_pass=input("Enter your password : ")
    while len(user_pass)==0:
        print("Password is empty, please enter it")
        user_pass=input("Enter your password : ")
    print()
    if user_pass==real_pass:
        return True
    return False

def choice2_in_action():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("|-------------LOGIN--------------|")
    print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
    print()
    if check_file_exist():
        l_data=get_user_data()
        real_usr=l_data[0]
        real_pass=l_data[1]
        if check_correct_username(real_usr):
            if check_correct_pass(real_pass):
                print("Logged in Successfully")
                print()
            else:
                print("Password Incorrect")
                print()
        else:
            print("Username Incorrect")
            print()
    else:
        print("Not Registered Yet, Please Register first")
        print()
def change_user_data(username,password):
    with open("user_info.txt","w") as f:
        f.write(f"username : {username}\npassword : {password}")
    f.close()


def choice3_in_action():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("|-------------LOGIN--------------|")
    print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
    print()
    if check_file_exist():
        l_data=get_user_data()
        real_usr=l_data[0]
        real_pass=l_data[1]
        if check_correct_username(real_usr):
            if check_correct_pass(real_pass):
                new_user=input("Enter new username : ")
                print("Wait Changing username ............")
                print()
                change_user_data(new_user,real_pass)
            else:
                print("Password Incorrect")
                print()
        else:
            print("Username did not match")
            print()
        
    else:
        print("Not Registered Yet, Please Register first")
        print()
def send_otp_email(random_number,usr):
    sender_email="sender_email"
    rec_email="rec_email"
    subject="Password Recovery Email"
    msg=f"Recovery OTP for your username {usr} is {random_number}"
    final_msg=f"{subject}\n\n{msg}"
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(sender_email,"read comment and paste code here") # first change the setting for allowing two step authentication for email then create app password and copy the code
    server.sendmail(sender_email,rec_email,final_msg)
    print("OTP sent succesfully")
def choice4_in_action():
    print("________________________________________")
    print("|----------to change password----------|")
    print("| enter method 1:  | enter method 2:   |")
    print("| use OTP          | use old password  |")
    print("|______________________________________|")
    print()
    method=input("Enter method either 1 or 2 : ")
    method=int(method)
    if method!=1 and method!=2:
        while True:
            method=input("Enter method either 1 or 2 : ")
            if method=='1' or method=='2':
                break
    method=int(method)
    if check_file_exist():
        l_data=get_user_data()
        real_usr=l_data[0]
        real_pass=l_data[1]
        if check_correct_username(real_usr):
            if method==2:
                if check_correct_pass(real_pass):
                    new_pass=input("Enter new password : ")
                    print("Wait Changing password ............")
                    print()
                    change_user_data(real_usr,new_pass)
                else:
                    print("Password Incorrect")
                    print()
            elif method==1:
                n=random.randint(4,7)
                random_number = random.sample(range(0, 10),n)
                string=""
                for i in random_number:
                    string+=str(i)
                # email sending mechanism 
                send_otp_email(string,real_usr)
                auth=input("enter otp: ")
                print()
                if auth==string:
                    new_passwd=input("enter new password: ")
                    while(len(new_passwd)==0):
                        print("Password field is empty, it is mandatory field")
                        new_passwd=input("enter new password: ")
                    print("Wait Changing password ............")
                    change_user_data(real_usr,new_passwd)
                    print("\nPassword changed successfully")
                else:
                    print("OTP does not match")

        else:
            print("Username did not match")
            print()

    else:
        print("Not Registered Yet, Please Register first")
        print()

print("----------WELCOME TO THE SECURITY SYSTEMS-----------")
print(" __________________________________________________")
print("|__________________1. REGISTER_____________________|")
print("|__________________2. LOGIN________________________|")
print("|__________________3. Change username______________|")
print("|__________________4. Change password______________|")
print("|__________________5. Back and END_________________|")
print()
while True:
    choice=input("Enter your choice: ")
    choice=int(choice)
    if choice==1:
        choice1_in_action()
    elif choice==2:
        choice2_in_action()
    elif choice==3:
        choice3_in_action()
    elif choice==4:
        choice4_in_action()
    elif choice==5:
        break
