import mysql.connector

# Função para conectar ao banco de dados


def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="he182555@",
        database="crm"
    )

# Função para adicionar um cliente


def adicionar_cliente():
    conn = conectar()
    cursor = conn.cursor()

    nome = input("Nome: ")
    email = input("Email: ")
    telefone = input("Telefone: ")

    cursor.execute(
        "INSERT INTO clientes (nome, email, telefone) VALUES (%s, %s, %s)", (nome, email, telefone))
    conn.commit()

    print("Cliente adicionado com sucesso!")
    cursor.close()
    conn.close()

# Função para visualizar todos os clientes


def visualizar_clientes():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()

    if not clientes:
        print("Nenhum cliente encontrado.")
    else:
        for cliente in clientes:
            print(f"ID: {cliente[0]}, Nome: {cliente[1]}, Email: {
                  cliente[2]}, Telefone: {cliente[3]}")

    cursor.close()
    conn.close()

# Função para atualizar as informações de um cliente


def atualizar_cliente():
    conn = conectar()
    cursor = conn.cursor()

    id = input("Digite o ID do cliente a ser atualizado: ")

    cursor.execute("SELECT * FROM clientes WHERE id = %s", (id,))
    cliente = cursor.fetchone()

    if cliente:
        nome = input(f"Novo Nome (atual: {cliente[1]}): ") or cliente[1]
        email = input(f"Novo Email (atual: {cliente[2]}): ") or cliente[2]
        telefone = input(
            f"Novo Telefone (atual: {cliente[3]}): ") or cliente[3]

        cursor.execute(
            "UPDATE clientes SET nome = %s, email = %s, telefone = %s WHERE id = %s", (nome, email, telefone, id))
        conn.commit()

        print("Informações do cliente atualizadas com sucesso!")
    else:
        print("Cliente não encontrado!")

    cursor.close()
    conn.close()

# Função para deletar um cliente


def deletar_cliente():
    conn = conectar()
    cursor = conn.cursor()

    id = input("Digite o ID do cliente a ser deletado: ")

    cursor.execute("DELETE FROM clientes WHERE id = %s", (id,))
    conn.commit()

    if cursor.rowcount:
        print("Cliente deletado com sucesso!")
    else:
        print("Cliente não encontrado!")

    cursor.close()
    conn.close()

# Função principal do sistema


def main():
    while True:
        print("\nSistema de CRM")
        print("1. Adicionar cliente")
        print("2. Visualizar clientes")
        print("3. Atualizar cliente")
        print("4. Deletar cliente")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_cliente()
        elif opcao == '2':
            visualizar_clientes()
        elif opcao == '3':
            atualizar_cliente()
        elif opcao == '4':
            deletar_cliente()
        elif opcao == '5':
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
