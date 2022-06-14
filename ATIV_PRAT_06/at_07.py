# 7) Crie um programa que calcule a folha de pagamento de uma empresa,
# conforme as instruções a seguir:

# a) O usuário pode inserir continuamente os nomes dos empregados até
# que escolha a opção de finalizar o informe de dados;

# b) Após informar o nome de cada empregado, o usuário deverá informar
# o valor do salário da hora trabalhada desse empregado e quantas
# horas ele trabalhou;

# c) O programa deve calcular o salário bruto de cada empregado, a
# percentagem de imposto retido na fonte (com base na tabela abaixo),
# o valor do imposto retido na fonte e o salário líquido (pagamento bruto
# menos imposto retido na fonte);

# d) Depois que o usuário inserir os dados do último empregado, o
# programa deve exibir o salário bruto, salário líquido, percentual de
# imposto e valor do imposto para cada funcionário;

# e) Por último, o programa deve exibir a soma de todas as horas
# trabalhadas, o total da folha de pagamento bruta, o total de imposto e
# a folha de pagamento líquida total.

# Percentuais de imposto
# Salário bruto Percentual

# Até R$ 2.999,99 10%
# Entre R$ 3.000,00 e R$ 5.499,99 13%
# Entre R$ 5.500,00 e R$ 7.999,99 16%
# Acima de R$ 8.000,00 20%
import os

next_payment = True
payroll = {'total_worked_hours':0, 'total_gross_salary':0, 'total_salary_liquid':0, 'total_tax_percentage':0} # folha de pagamento

def calc_salary_employee(hourly_wage, worked_hours):
    gross_salary = (worked_hours * hourly_wage)

    def calc_salary_rate(rate):
        tax_percentage = gross_salary * rate
        salary_liquid = gross_salary - tax_percentage

        payroll['total_worked_hours'] += worked_hours
        payroll['total_gross_salary'] += gross_salary
        payroll['total_tax_percentage'] += tax_percentage
        payroll['total_salary_liquid'] += salary_liquid

        # criando menssagem padrao com dados do empregado
        message = '\n'
        message += f'Salário bruto R$ {round(gross_salary,2)} \n'
        message += f'Salário liquído R$ {round(salary_liquid,2)} \n'
        message += f'Valor taxa imposto R$ {round(tax_percentage,2)} de {(rate*100)}% \n'
        message += '\n --- TOTAL FOLHA DE PAGAMENTO --- \n'
        message += f'Total de horas: {payroll["total_worked_hours"]}  \n'
        message += f'Total salario liquido R$ {round(payroll["total_salary_liquid"],2)} \n'
        message += f'Total salario bruto R$ {round(payroll["total_gross_salary"],2)} \n'
        message += f'Total imposto pago R$ {round(payroll["total_tax_percentage"],2)} \n'
        # retornando dados da funcao com oresultado
        return message
    
    if gross_salary < 3000: # 10%
        result = calc_salary_rate(0.10)

    elif gross_salary >= 3000 and gross_salary < 5500: # 13%
        result = calc_salary_rate(0.13)

    elif gross_salary >= 5500 and gross_salary < 8000: # 16%
        result = calc_salary_rate(0.16)

    else: # Acima de R$ 8.000,00 20%
        result = calc_salary_rate(0.20)

    # retorno valores calculados e messagem pronta 
    return result


while next_payment == True:
    name_employee = input("Digite o nome do empregado: \n")
    hourly_wage = float(input("Digite o valor de salario por hora ganho: \n"))
    worked_hours = int(input("Digite o total de horas trabalhadas: \n"))

    # processando dados 
    calc = calc_salary_employee(hourly_wage, worked_hours)
    
    # mostrar dados de cada empregado
    os.system('clear')
    print(calc)

    print('\n')
    opt_to_finish = int(input('Digite o numero [0] para continuar, [1] para Sair. \n'))
    if opt_to_finish == 1:
        next_payment = False
        os.system('clear')
        print('\n ...SYSTEMA FINALIZADO COM SUCESSO... \n')
        message = ''
        message += '\n --- TOTAL FOLHA DE PAGAMENTO --- \n'
        message += f'Total de horas: {payroll["total_worked_hours"]}  \n'
        message += f'Total salario liquido R$ {round(payroll["total_salary_liquid"],2)} \n'
        message += f'Total salario bruto R$ {round(payroll["total_gross_salary"],2)} \n'
        message += f'Total imposto pago R$ {round(payroll["total_tax_percentage"],2)} \n'
        print(message)
        break
    os.system('clear')