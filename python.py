nome = input("Qual seu nome?: ")
idade = int(input("Quantos anos você tem?: "))
opiniao = input("Na sua opinião, o samp deveria ser extinto?: ")

print(f"Olá {nome}, tudo bem? Seja bem-vindo!")
print(f"Você tem {idade} anos, não é?")

if opiniao.upper() == "SIM":
    print("Você concorda que o SAMP seja extinto! :) ")
elif opiniao.upper() == "NÃO" or "NAO":
    print("Você não concorda que o SAMP seja extinto! :( ")