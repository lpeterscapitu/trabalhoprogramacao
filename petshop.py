import os
from peewee import *

arq = "petShop.db"
db = SqliteDatabase(arq)

class BaseModel (Model):
    class Meta :
        database = db

class Produto (BaseModel):
    nome = CharField()
    qtd_produtos = IntegerField()
    validade =  DateField()
    def __str__(self):
        return self.nome + str(self.qtd_produtos) + str(self.validade)

class Fornecedor (BaseModel):
    nome = CharField()
    cnpj = IntegerField()

    def __str__(self):
        return self.nome + str(self.cnpj)  

class Colaborador(BaseModel):
    nome = CharField()
    funcao = CharField()
    def __str__(self):
        return   self.funcao +  " " + self.nome  

class Venda (BaseModel):
    colaboradorzinho = ForeignKeyField(Colaborador)
    qtd_vendido = IntegerField
    def __str__(self):
         return str(self.colaboradorzinho) + "" + str(self.qtd_vendido)

class Veiculos (BaseModel):
    nome = CharField()
    placa = CharField()
    def __str__(self):
        return self.nome + self.placa

class Cliente (BaseModel):
    nome = CharField() 
    cpf = IntegerField()
    def __str__(self):
        return self.nome + " portador do cpf de número " + str(self.cpf)

class Paciente (BaseModel):
     animal = CharField()
     def __str__(self):
        return self.animal  

class Exame (BaseModel):
    req_exame = CharField()
    nome = CharField()
    def __str__(self):
        return  " fará exame de número " + self.req_exame + " de " + self.nome


class Consulta (BaseModel):
    data = DateField()
    pacientizinho = ForeignKeyField(Paciente)
    clienti = ForeignKeyField(Cliente)
    colaboradorr = ForeignKeyField(Colaborador)
    def __str__(self):
        return " o cliente " + str(self.clienti) + " paciente do médico " + str(self.colaboradorr) + " dono do  " + str(self.pacientizinho) + " nascido em " + str(self.data) 

class Atendimento (BaseModel):
    colaboradorzao = ForeignKeyField (Colaborador)
    def __str__(self):
        return str(self.colaboradorzao)

if os.path.exists(arq):
    os.remove (arq)

db.connect()
db.create_tables ([Produto,
                   Fornecedor,
                   Colaborador,
                   Venda,
                   Veiculos,
                   Cliente,
                   Paciente,
                   Exame,
                   Consulta,
                   Atendimento
])

produto1 = Produto.create(nome = "shampozinho", qtd_produtos= 14, validade= "14/07/2019")

fornecedor1 = Fornecedor.create(nome = "hedensholder", cnpj = 724 )

colaborador1 = Colaborador.create ( nome = "Miguel", funcao = " veterinário")

venda1 = Venda.create(qtd_vendido = 8, colaboradorzinho = colaborador1)

veiculos1 = Veiculos.create(nome = "crossfox", placa = "cd83-2")

cliente1 = Cliente.create(nome = "Eduardo", cpf = 214389)

paciente1 = Paciente.create(animal ="passarinho")

exame1 = Exame.create(req_exame = "número 3", nome = "de sangue")

consulta1 = Consulta.create (data = "12/11/2016", pacientizinho = paciente1, clienti = cliente1, colaboradorr = colaborador1)

atendimento1 = Atendimento.create (colaboradorzao = colaborador1)

print(consulta1)
print(exame1)
print(atendimento1)
print(veiculos1)
print(venda1)
print(fornecedor1)
print(produto1)