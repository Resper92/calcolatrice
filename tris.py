griglia = [["","",""],["","",""],["","",""]]

tentativi = 0

while tentativi <=9:
    tentativi +=1
    if tentativi % 2 == 0:
        simbolo = "X"
    else:
        simbolo = "O"
    
        
    asse_x = int(input("inserisci asse x : "))
    asse_y = int(input("inserisci asse y :"))
    
    griglia[asse_y][asse_x] = simbolo
    for riga in griglia:
       grig=" | ".join(riga)
       print(grig)
        
        
