// importar modulos snecesarios//
import string
import secrets


//denir el alfgabeto//
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters + digits + special_chars

//largo de contraseña//
pwd_length = 12

//generar cadena de contraseña//
pwd = ''
for i in range(pwd_length):
  pwd += ''.join(secrets.choice(alphabet))

print(pwd)

// generar restriccion de cumplimiento de contraseña//
while True:
  pwd = ''
  for i in range(pwd_length):
    pwd += ''.join(secrets.choice(alphabet))

  if (any(char in special_chars for char in pwd) and 
      sum(char in digits for char in pwd)>=2):
          break
print(pwd)