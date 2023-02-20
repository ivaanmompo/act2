totalnotes = 0
qnotes = 0
qnotespositives = 0
while True:
    nota = int(input("Dis-me una nota: (Sols positius o negatius)"))
    if nota > 0:
        totalnotes+= nota
        qnotespositives+=1
    if nota == 0:
        print("Han de ser números enters positius o negatius. Torna a provar")
        continue
    qnotes+=1
    if qnotes == 10:
        break
    
if totalnotes > 0:
    print ("La mitja total sols dels numeros positius es: ", totalnotes/qnotespositives)
if totalnotes <= 0:
    print("La mija soles es de numeros positius")
