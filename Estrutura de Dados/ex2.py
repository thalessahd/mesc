"""
Considere declaração inicial de uma lista de alunos:

alunos = [{"nome":"Thalessa", "nomecompleto":"Thalessa Hungerbuhler Daroz"}]
"""
# 1) Insira também os campos email, tipo (se é aluno Especial ou Regular) e cr (coeficiente de rendimento do curso). 
# Insira um ou mais alunos hipotéticos para que a lista tenha mais informações.

def generateData():
    alunos = [
        {'nome':'Thalessa',
         'nomecompleto':'Thalessa Hungerbuhler Daroz', 
         'email':'thalessa.daroz@iduff.com.br',
         'tipo':'Especial',
          'cr':10.0},
        {'nome':'John',
         'nomecompleto':'John Kramer', 
         'email':'john.kramer@gmail.com',
         'tipo':'Regular',
          'cr':9.9},
        {'nome':'Amanda',
         'nomecompleto':'Amanda Young', 
         'email':'amanda.young@hotmail.com',
         'tipo':'Regular',
          'cr':8.5},
        {'nome':'Mark',
         'nomecompleto':'Mark Hoffman', 
         'email':'mark.hoffman@iduff.com.br',
         'tipo':'Regular',
          'cr':7.4},
        {'nome':'Allana', 
         'nomecompleto':'Allana Tatiane Malu Araújo', 
         'email':'allana.araujo@outlook.com',
         'tipo':'Regular',
          'cr':6.5},

    ]
    return alunos

# 2) Crie uma função para retornar a lista de emails da turma. Relembrando, para acessar um campo de um dicionário, 
# basta usar a chave. Por exemplo, para retornar o nome Thalessa aluna acima podemos escrever a expressão: 
# alunos[0]["nome"]


def getFieldData(values, fieldName):
    result = map(lambda x: x[fieldName], values)
    return list(result)

alunos = generateData()
print(getFieldData(alunos, 'email'))

# 3) Crie uma função para retornar os contatos de um dado tipo (Regular ou Especial). Por exemplo, para a nossa turma, 
# retornar uma lista com todos os alunos especiais só retornará a Thalessa, enquanto que a busca por regulares 
# deve retornar todos os demais.

def filterDataByType(values, type):
    result = filter(lambda x: x['tipo']==type, values)
    return list(result)

print(filterDataByType(alunos, 'Especial'))

# 4) Crie uma função para retornar a lista dos emails dos alunos regulares.

def getEmailsOfRegularStudents(values):
    result = filterDataByType(values, 'Regular')
    result = getFieldData(result, 'email')
    return list(result)

print(getEmailsOfRegularStudents(alunos))

# 5) Crie uma função para retornar a média dos alunos (soma dos cr's / quantidade de alunos).
from functools import reduce

def calculateStudentAverage(values):
    result = reduce(lambda x,y: x+y['cr'], values, 0)
    return round(result/len(values), 2)

print(calculateStudentAverage(alunos))

# 6) Sabendo que o endereço para acessar informações de um usuário no github é dado 
# pela url https://api.github.com/users/<nomedousuario&gt;, usando o identificador de cada endereço de email, 
# crie uma função para retornar uma lisa de endereços de usuários no github.

def generateGithubUsers(values):
    gitUrl = 'https://api.github.com/users/'
    result = map(lambda x: gitUrl + x['email'].split('@')[0], values)
    return list(result)

print(generateGithubUsers(alunos))