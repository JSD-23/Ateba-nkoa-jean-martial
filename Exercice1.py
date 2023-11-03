def lengthOfLastWord(s):
      if(len(s)>0):
            tableau=s.split()
            nombre=len(tableau)
            taille=len(tableau[nombre-1])
            return taille
      else:
       return 0
