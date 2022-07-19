#Escreva um programa, que leia um conjunto de 20 fichas correspondente a alunos
#e armazene-as em vetores, cada uma contendo, a altura, a nota (de 0 ate 10), ano
#de nascimento e o codigo do sexo de uma pessoa (codigo = ’M’ se for masculino
#e ’F’ se for feminino), e calcule e imprima:
#A maior e a menor altura da turma;
#A quantidade de mulheres com altura acima da media da altura das mulheres;
#A quantidade de homens com nota inferior a media das mulheres;
#O percentual de pessoas que nasceram em cada ano inserido;

from re import I


altura,nota,anodenascimento,codigo,anos,anos2,porcentagem = [],[],[],[],[],[],[]
maior,menor,mediaalturaF,medianotaF,medianotaM,M,F,FAcima,MAbaixo,pos = 0.0,100.0,0.0,0.0,0.0,0,0,0,0,0
for item in range(20):
    altura.append(float(input(f"Digite a altura do aluno {item+1}: ")))
    nota.append(float(input(f"Digite a nota do aluno {item+1}: ")))
    anodenascimento.append(int(input(f"Digite o ano de nascimento do aluno {item+1}: ")))
    codigo.append(input(f"Digite o codigo do sexo do aluno {item+1}: "))

#Inicio maior e menor altura
for item in range(20):
    if maior<altura[item]:
        maior = altura[item]
    if menor>altura[item]:
        menor = altura[item]
#Fim maior e menor altura

#Inicio media das mulheres e homens
for item in range(20):
    if codigo[item]=='F':
        mediaalturaF = mediaalturaF + altura[item]
        medianotaF = medianotaF + nota[item]
        F += 1
    elif codigo[item]=='M':
        medianotaM = medianotaM + nota[item]
        M +=1

mediaalturaF = mediaalturaF/F
medianotaF = medianotaF/F
medianotaM = medianotaM/M
#Fim media das mulheres e homens

#A quantidade de mulheres com altura acima da media da altura das mulheres;
#A quantidade de homens com nota inferior a media das mulheres;
for item in range(20):
    if codigo[item]=='F':
        if altura[item]>mediaalturaF:
            FAcima += 1
    elif codigo[item]=='M':
        if nota[item]<medianotaF:
            MAbaixo += 1

#O percentual de pessoas que nasceram em cada ano inserido;
for item in range(20):
    if anodenascimento[item] not in anos:
        anos.append(anodenascimento[item])
        anos2.append(0)
        porcentagem.append(0)

for item in range(20):
    if anodenascimento[item] in anos:
        pos = anos.index(anodenascimento[item])
        anos2[pos] += 1

for item in range(20):
    porcentagem[item] = (20 - anos2[item]) / 20 * 100


#Mostrar informações na tela
print(f"A maior e menor altura da turma respectivamente é: {maior} {menor}")
print(f"A quantidade de mulheres com altura acima da media da altura das mulheres: {FAcima}")
print(f"A quantidade de homens com nota inferior a media das mulheres: {MAbaixo}")
print(f"O percentual de pessoas que nasceram em cada ano inserido:")
for item in range(len(anos)):
    print(f"{anos[item]} = {porcentagem[item]}%")