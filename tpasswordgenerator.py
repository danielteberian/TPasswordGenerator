import random
import string
import sys

pass_lng = int(input("ENTER DESIRED PASSWORD LENGTH: "))
pass_chrs = string.ascii_letters + string.digits + string.punctuation

passwd = []

for x in range(pass_lng):
   passwd.append(random.choice(pass_chrs))
print("\nGENERATED PASSWORD:\n" + "\n" + ''.join(passwd))
