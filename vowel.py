#enter the variable
variable=(input())
l=variable.isalpha()
if(l==True):
  if( variable=="a" or variable=="e" or variable=="i" or variable=="o" or variable=="u"):
      print("Vowel")
  else:
      print("Consonant")
else:
    print("invalid")

