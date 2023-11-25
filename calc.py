def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

if __name__ == "__main__":
    print(
        '''Operações disponíveis:
        1. Adição
        2. Subtração
        3. Multiplicação
        4. Divisão'''
    )

    input = input("Digite a operação desejada, com os operandos separados por espaço (Ex: 4 + 5, 7 / 8): ").split()
    operator = input[1]
    operands = [int(input[0]), int(input[2])]
    match operator:
        case "+":
            result = add(operands[0], operands[1])
            print(result)
        case "-":
            result = sub(operands[0], operands[1])
            print(result)
        case "*":
            result = mul(operands[0], operands[1])
            print(result)
        case "/":
            result = div(operands[0], operands[1])
            print(result)
        case _:
            print("Operação inválida!")
