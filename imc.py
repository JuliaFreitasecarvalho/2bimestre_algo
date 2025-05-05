def calcularora_imc(pessoas):
    imc=pessoas["peso"]/pessoas["altura"]*pessoas["altura"]
    resultado= f"0 IMC {pessoas["nome"]} é {imc:.2f}"
    #comando ternário
    saudavel= 18.5 < imc < 25

    return{
        "nome": pessoas["nome"],
        "imc": imc,
        "resultado": resultado,
        "saudavel": saudavel 
    }

pessoa1={
    "nome":"José",
    "peso": 110,
    "altura": 1.75
    }
pessoa2={
    "nome": "Júlia",
    "peso": 46,
    "altura": 1.58
}
print(calcularora_imc(pessoa1))
print(calcularora_imc(pessoa2))