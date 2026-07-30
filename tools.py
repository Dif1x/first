import random
import string

def randchis():
    min = int(input("Enter min: "))
    max = int(input("Enter max: "))
    chis = random.randint(min, max)
    print(chis)
def randpassword():
    global newpassword
    password = []
    dlina = int(input("Enter dlina: "))
    pool = string.ascii_letters + string.digits + string.punctuation
    for _ in range(dlina):
        item = random.choice(pool)
        password.append(item)
        newpassword = "".join(password)
    print(f"your password: {newpassword}")
