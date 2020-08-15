import re
import pandas
import xlsxwriter


def pass_check(text):
    pattern = re.compile(r"(^[A-Z]+[a-z]+[_@#$%^&*]+[0-9]+$)")
    a = pattern.findall(text)
    try:
        if a[0] == text:
            return True
        else:
            return False
    except IndexError:
        print("Invalid Password")


def SignUp():
    excel_data = pandas.read_excel('user_log.xlsx', sheet_name='user')
    name = excel_data["Name"].to_list()
    passwd = excel_data["Password"].to_list()
    user_name = input("Enter Your Name:- ")

    if user_name not in name or name == []:
        print("New User want to Sign up!![y/n]")
        want = input("Enter:- ")
        if 'y' == want:
            name.append(user_name)
            print("Enter password, It should start with Capital Letter, have a special character and must contain digits.")
            user_pass = input("Enter Password:- ")
            pws = pass_check(user_pass)
            if pws == True:
                passwd.append(user_pass)

                user = pandas.DataFrame(
                    {"Name": name, "Password": passwd})
                writer = pandas.ExcelWriter(
                    "user_log.xlsx", engine="xlsxwriter")
                user.to_excel(writer, sheet_name='user')
                writer.save()
                print("You have Succesfully Signed Up")
                return True

            else:
                print("try again")
                SignUp()
        else:
            print("As your Wish!!")
            return "Exit"

    elif user_name in name:
        user_pass = input("Enter Password:- ")
        if user_pass in passwd:
            return True
        else:
            return False


if __name__ == "__main__":
    SignUp()
