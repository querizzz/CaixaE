print('--------------------------')
print('     CAIXA ELETRÔNICO     ')
print('--------------------------')


print('NOTAS DISPONÍVEIS PARA SAQUE:R$ 5, 10, 50 e 100.')
saque = int(input("ENTRE COM O VALOR(R$) DO SAQUE:"))

if 10 <= saque <= 600:
    notascem = saque // 100
    saque = saque % 100

    notascinq = saque // 50
    saque = saque % 50

    notasdez = saque // 10
    saque = saque % 10

    notascinc = saque // 5
    saque = saque % 5

    

    if notascem > 0:
        print(notascem, "Notas de R$ 100")
    if notascinq > 0:
        print(notascinq, "Notas de R$ 50")
    if notasdez > 0:
        print(notasdez, "Notas de R$ 10")
    if notascinc > 0:
        print(notascinc, "Notas de R$ 5")

else:
        print('NÃO É POSSÍVEL REALIZAR O SAQUE')
