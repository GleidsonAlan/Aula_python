import os
os.system('cls')

escola ={
    "aluno_001":{
        "nome":"Ana silva",
        "idade": 20,
        "notas":{
            "matematica": 8.5,
            "portugues": 9,
            "historia": 7
        },

    "contato":{
        "email":"ana@gmail.com",
        "telefone":"119878745"
        },   
    },

    "aluno_002":{
        "nome":"Emerson souza",
        "idade": 20,
        "notas":{
            "matematica": 8,
            "portugues": 10,
            "historia": 10
        },

    "contato":{
        "email":"emerson@gmail.com",
        "telefone":"1198119898"
        },   
},

}

print(escola["aluno_001"] ["notas"] ["matematica"] )
print(escola["aluno_002"] ["notas"] ["portugues"] )