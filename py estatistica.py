# Programa que faça o tratamento de uma base dados, ou entrada, e retorne a estatística descritiva.

# ler base de dados
# Retornar Tamanho da Amostra, Média Aritmética, Média harmônica, Média geométrica, Moda, Mediana, Desvio Padrão,
# Erro Padrão, Variância, Coeficiente de variação, Minimo, Máximo, Quartis, Assimetria, Curtose.

import statistics

db = []

print("-------- Estatística Descritiva ---------")
print("Obs: Este programa atualmente analisa apenas dados quantitativos.")
print()

tentenov = True

while tentenov is True:
    entrada1 = input("Escolha como deseja realizar a Estatística Descritiva de dados quantitativos: (Digite a ou b)"
                     "\n[a] Deseja a partir de uma base de dados já importada em arquivo .txt."
                     "\n[b] Deseja inserir os dados.\n")
    if entrada1 != 'a' and entrada1 != 'b':
        tentenov = True
        print('Tente Novamente (Digite a ou b)')
    else:
        tentenov = False

if entrada1 == 'a':
    with open('Memoriadb.txt', 'r') as banco_dados:
        for i in banco_dados:
            trat = i.split('\n')
            db.append(float(trat[0]))

if entrada1 == 'b':
    insercao = [float(i) for i in
                input("Insira a base de dados separada por vírgula: (Exemplo: 1, 2, 3, 4..)\n").split(", ")]
    db += insercao

tentenov2 = True

while tentenov2 is True:
    entrada2 = input("Executar programa? (Digite s ou n)"
                     "\n[s] Sim"
                     "\n[n] Não\n")

    if entrada2 != 's' and entrada2 != 'n':
        tentenov2 = True
        print('Tente Novamente (Digite s ou n)')
    else:
        tentenov2 = False

if entrada2 == 's':
    # Tamanho da Amostra
    tam_amostra = len(db)

    # Minimo
    minimo = min(db)

    # Máximo
    maximo = max(db)

    # Mediana
    db.sort()
    meio = tam_amostra//2
    if (tam_amostra % 2) == 0:
        mediana = (db[meio] + db[meio-1]) / 2
    else:
        mediana = db[meio]

    # Quartis
    quartis = statistics.quantiles(db, n=4)

    # Média Aritmética
    media = sum(db) / tam_amostra

    # Variância
    variancia = statistics.variance(db)

    # Desvio Padrão
    desviopd = statistics.stdev(db)

    # Erro Padrão
    erro_p = desviopd / (tam_amostra**(1/2))

    # Assimetria Pearson
    assimetria = (3*(media - mediana)) / desviopd

    # Curtose
    percentis = statistics.quantiles(db, n=100)
    curtose = (quartis[2] - quartis[0]) / (2*(percentis[89]-percentis[9]))

    # Média Harmônica
    media_harm = statistics.harmonic_mean(db)

    # Média Geométrica
    media_geo = statistics.geometric_mean(db)

    print()
    print(f'Tamanho da Amostra: {tam_amostra:.4f}')
    print(f'Mínimo: {minimo:.4f}')
    print(f'Máximo: {maximo:.4f}')
    print(f'Média: {media:.4f}')
    print(f'Mediana: {mediana:.4f}')
    print(f'Variância: {variancia:.4f}')
    print(f'Desvio Padrão: {desviopd:.4f}')
    print(f'Média Harmônica: {media_harm:.4f}')
    print(f'Média Geométrica: {media_geo:.4f}')
    print(f'Primeiro Quartil (25%): {quartis[0]:.4f}')
    print(f'Terceiro Quartil (75%): {quartis[2]:.4f}')
    print(f'Erro Padrão: {erro_p:.4f}')
    print(f'Assimetria (2º Coef. Pearson): {assimetria}')
    print(f'Curtose: {curtose}')

else:
    print('Programa Encerrado')
