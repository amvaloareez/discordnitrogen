import random
import string
text = """
███╗░░██╗██╗░██████╗░██╗░░░██╗
████╗░██║██║██╔════╝░██║░░░██║
██╔██╗██║██║██║░░██╗░██║░░░██║
██║╚████║██║██║░░╚██╗██║░░░██║
██║░╚███║██║╚██████╔╝╚██████╔╝
╚═╝░░╚══╝╚═╝░╚═════╝░░╚═════╝░
   """
print(text)

cb = input("The codes will be classic or boost? c/b: ")
amount = int(input('Amount of nitro codes to generate: '))
value = 1
while value <= amount:

 if cb == ("c"):
   
    code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    f = open('nitroC.txt', "a+")
    f.write(f'{code}\n')
    f.close()
    print(f'[GENERATED] {code}')
    value += 1

else:

      code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=24))
      f = open('nitroB.txt', "a+")
      f.write(f'{code}\n')
      f.close()
      print(f'[GENERATED] {code}')
      value += 1
