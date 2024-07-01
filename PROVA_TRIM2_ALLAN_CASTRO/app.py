
mes = input("Defina o Mês: ")

dia = int(input("Defina o dia: "))


if mes in ('Janeiro', 'Fevereiro', 'Março'):
    estacao_do_ano = 'Verão'

elif mes in ('Abril', 'Maio', 'Junho'):
    estacao_do_ano = 'Outono'

elif mes in ('Julho', 'Agosto', 'Setembro'):
    estacao_do_ano = 'Inverno'

else:
    estacao_do_ano = 'Primavera'



if (mes == 'March') and (dia > 19):
    estacao_do_ano = 'Outono'

elif (mes == 'June') and (dia > 20):
    estacao_do_ano = 'Inverno'

elif (mes == 'September') and (dia > 21):
    estacao_do_ano = 'Primavera'

elif (mes == 'December') and (dia > 20):
    estacao_do_ano = 'Verão'


print("A estação é", estacao_do_ano) 
