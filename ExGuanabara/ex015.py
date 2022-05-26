diasAlugados = int(input("Quantos dias alugados? "))
kmRodados = int(input("Quantos Km rodados? "))
print(f"O total a pagar é de R${(diasAlugados*60)+(kmRodados*0.15):.2f}")
