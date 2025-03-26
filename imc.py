def calculo_imc (peso,altura):
    imc = (peso / altura**2)
    return imc

def classificao_imc(imc):
    if imc < 18.5:
        return "Baixo peso"
    elif 18.5 <= imc < 24.9:
        return "Peso adequado"
    elif 24.9 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "obesidade grau 1"
    elif 35 <= imc < 39.9:
        return "obesidade grau 2"
    elif 40 <= imc:
        return "obesidade grau 3"


peso = float(input(f"escreva seu peso: ")) 

altura = float(input(f"escreva sua altura: ") )

imc = calculo_imc(peso,altura)
print (classificao_imc(imc))