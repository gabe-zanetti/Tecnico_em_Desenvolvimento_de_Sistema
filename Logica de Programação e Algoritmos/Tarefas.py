tarefas=[]
for i in range(0,6):
    descricao=input("Escreva a descrição: ")
    prioridade=input("Escreva a priotidade(alta, media, baixa): ")
    status=input("Escreva o status(pendente ou concluido): ")

    tarefa={
        'Descrição': descricao,
        'Prioridade': prioridade,
        'Status': status
    }

    tarefas.append(tarefa)

if(tarefa[prioridade] == "alta" and tarefa[status] == "pendente"):
    print(tarefa)

