# contador.py

def es_par_o_impar(n):
    
    return f"{n} - par" if n % 2 == 0 else f"{n} - impar"

def cuenta_regresiva(n):
   
    if n < 0:
        return  
    print(es_par_o_impar(n))
    if n == 0:
        print("Fin de la cuenta regresiva")
        return
    cuenta_regresiva(n - 1)
	