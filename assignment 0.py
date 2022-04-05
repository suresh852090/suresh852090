
def user_name1(u_name): # to create username
    created_u_name = (u_name.lower() + "@" + "gmail" + "." + "com").strip()
    return created_u_name

def validity(mail): # to check the username
    if mail.count('@') == 1 and mail.count('.') == 1 and mail[0].isalpha():
        b = mail.index('@')
        c = mail.index('.')
        list = []
        list2 = []
        for i in range(0, b):
            list.append(mail[i])
        for j in range(b + 1, c):
            list2.append(mail[j])
        if len(list) >= 3 and len(list2) >= 4:
            if mail.count('.com') or mail.count('.in') == 1:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def v_password(p): # to verify password
    if 6 <= len(p) <= 17:
        list2 = []
        list3 = []
        list4 = []
        list5 = []
        for i in p:
            if i.islower():
                list2.append(i)#to get the lower character
            elif i.isupper():
                list3.append(i)#to get the upper character
            elif i.isnumeric():
                list4.append(i)# to get the numeric value
            else:
                list5.append(i.strip()) #to get  the special characters
        if len(list2) >= 1 and len(list3) == 1:
            if len(list4) >= 1 and len(list5) == 1:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def registration(): #to register
    db = open("C:\\Users\\pavan\\Desktop\\databse.txt", "a")
    name = input("Enter your name").strip()
    pass_1 = input("enter your password:").strip()
    created_username = user_name1(name)
    if (validity(created_username) == True) and (v_password(pass_1) == True):
        db.write(created_username + "," + pass_1 + "\n")
        print("Username:"+created_username+"\nPassword:"+pass_1)
    else:
        print("username & password is not valid!, create again")

def login():
    db = open("C:\\Users\\pavan\\Desktop\\databse.txt", "r+")
    uname = []
    ppassrord = []
    for x in db:
        a, b = x.split(",")
        b = b.strip()
        uname.append(a)
        ppassrord.append(b)
    data = dict(zip(uname, ppassrord))
    name_u = input("enter your user name").strip()
    pas_u = input("enetr your password").strip()
    if name_u in uname:
        if pas_u == data[name_u]:
            print("Login success\n"
                  "Hi, Welcome")
        else:
            print("Entered password is wrong\n")
    else:
        print("User do not exist")
        l = int(input("If you want to create new user enter 1"))
        if l == 1:
            registration()
        else:
            print("Thank you! see you again")
login()