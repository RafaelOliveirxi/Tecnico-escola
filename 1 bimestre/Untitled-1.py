def vulnerable_function():
    # Solicita ao usuário que insira uma string
    user_input = input("Digite algo (não mais que 10 caracteres): ")

    # Definindo um buffer de tamanho fixo
    buffer = [0] * 10

    # Verifica se a entrada é maior que o buffer permitido
    if len(user_input) > len(buffer):
        print("Aviso: A entrada excede o limite do buffer. Entrada será truncada.")
    
    # Preenche o buffer com a entrada do usuário (potencial overflow)
    for i in range(min(len(user_input), len(buffer))):  # Garantindo que não ultrapasse o tamanho do buffer
        buffer[i] = user_input[i]

    # Exibe o buffer preenchido
    print(f'Buffer preenchido: {buffer}')

# Chama a função
vulnerable_function()
