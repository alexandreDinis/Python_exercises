#[0,25], (25,50], (50,75], (75,100]

inter = float(input())

if inter >= 0 and inter <= 25.00000:
    print("Intervalo [0,25]") 
elif inter > 25.00000 and inter <= 50.00000:
    print("Intervalo (25,50]") 
elif inter > 50.00000 and inter <= 75.0000000:
    print("Intervalo (50,75]") 
elif inter > 75.0000000 and inter <= 100.0000000:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")




