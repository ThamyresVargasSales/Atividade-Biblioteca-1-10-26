from fastapi import FastAPI

app = FastAPI(title="API do IFMA Campus Timon")

#Questão 9:
alunos = [
    {"id": 1, "nome": "Ana Clara Silva", "curso": "Sistemas para Internet", "turno": "Matutino", "situacao_academica": "Matriculado"},
    {"id": 2, "nome": "Lucas Gabriel Sousa", "curso": "Eletromecânica", "turno": "Vespertino", "situacao_academica": "Matriculado"},
    {"id": 3, "nome": "Beatriz Oliveira", "curso": "Administração", "turno": "Noturno", "situacao_academica": "Matriculado"},
    {"id": 4, "nome": "João Pedro Santos", "curso": "Sistemas para Internet", "turno": "Matutino", "situacao_academica": "Trancado"},
    {"id": 5, "nome": "Mariana Costa", "curso": "Edificações", "turno": "Vespertino", "situacao_academica": "Concluído"},
    {"id": 6, "nome": "Gabriel Alves", "curso": "Eletromecânica", "turno": "Noturno", "situacao_academica": "Matriculado"}
]

# Questão 8:
@app.get("/")
def inicio():
    return {"mensagem": "API do IFMA Campus Timon está funcionando!"}

# Questão 9:
@app.get("/alunos")
def listar_alunos():
    return alunos

# Questão 10:
@app.get("/resumo")
def obter_resumo():
    cursos_unicos = list(set(aluno["curso"] for aluno in alunos))
    turnos_unicos = list(set(aluno["turno"] for aluno in alunos))
    
    return {
        "total_alunos": len(alunos),
        "quantidade_cursos": len(cursos_unicos),
        "turnos_disponiveis": turnos_unicos
    }