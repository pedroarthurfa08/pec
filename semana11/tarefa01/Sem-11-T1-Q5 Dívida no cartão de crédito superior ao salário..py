'''Pedro recebe um salário mensal e tem aumentos salariais de 5% uma vez por ano no mês de março. Pedro também tem uma dívida no cartão de crédito com uma taxa de juros de 15% ao mês. Considerando que a situação se refere ao mês de outubro do ano de 2016, faça um programa leia o valor do salário e o valor da dívida e calcula, simulando a evolução do salário e da dívida de Pedro, em que mês e ano a dívida com o cartão de crédito será superior ao seu próprio salário.
Represente os meses como inteiros de 1 a 12.
Dica: Controle essas quatro variáveis:
“dívida” que aumenta todo mês; “salário” que aumenta apenas se o número do mês for 3 (março); “mês” que é incrementado sempre, mas que retorna a 1 quando passar de 12; “ano” que só é incrementado quando o mês retornar a 1.'''
def calcular_mes_ano_dia(salario, divida):
    mes = 10
    ano = 2016
    while divida <= salario:
        divida *= 1.15
        if mes == 3:
            salario *= 1.05
        mes += 1
        if mes > 12:
            mes = 1
            ano += 1
    return mes, ano
def main():
    try:
        salario = float(input("Insira o valor do seu salário: "))
        divida = float(input("Insira o valor da sua divida: "))
        mes, ano = calcular_mes_ano_dia(salario, divida)
        print(f"Em {mes}/{ano}, Pedro quitará sua dívida.")
    except ValueError:
        print()
if __name__ == "__main__":
    main()
