idnumber = input("Enter Student ID: ")
email = input("Enter Email ID: ")
password = input("Enter Password: ")
referral = input("Enter Referral Code: ")
valid = True
if len(idnumber) != 7:
    valid = False
elif idnumber[0:3] != "CSE":
    valid = False
elif idnumber[3] != "-":
    valid = False
elif not (idnumber[4].isdigit() and idnumber[5].isdigit() and idnumber[6].isdigit()):
    valid = False

if "@" not in email or "." not in email:
    valid = False
elif email[0] == "@" or email[-1] == "@":
    valid = False
elif not email.endswith(".edu"):
    valid = False

if len(password) < 8:
    valid = False
elif not password[0].isupper():
    valid = False
elif not (password[1].isdigit() or password[2].isdigit() or password[3].isdigit() or
          password[4].isdigit() or password[5].isdigit() or password[6].isdigit() or
          password[7].isdigit()):
    valid = False

if len(referral) != 6:
    valid = False
elif referral[0:3] != "REF":
    valid = False
elif not (referral[3].isdigit() and referral[4].isdigit()):
    valid = False
elif referral[5] != "@":
    valid = False

if valid:
    print("APPROVED")
else:
    print("REJECTED")
