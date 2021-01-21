
from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Rodas(Model):
    id = Column(Integer, primary_key=True)
    nome = Column(String(25), unique=True, nullable=False)

    def __repr__(self):
        return self.nome

class Marca(Model):
    id = Column(Integer, primary_key=True)
    nome = Column(String(25), unique=True, nullable=False)

    def __repr__(self):
        return self.nome

class Modelo(Model):
    id = Column(Integer, primary_key=True)
    nome = Column(String(25), unique=True, nullable=False)

    def __repr__(self):
        return self.nome

class Veiculo(Model):
    id = Column(Integer, primary_key=True)
    condutor = Column(String(200),unique=True, nullable=False)
    cor = Column(String(25), unique=True, nullable=False)
    placa = Column(String(25), unique=True, nullable=False)
    ano = Column(Integer,unique=True, nullable=False)
    modelo_id = Column(Integer, ForeignKey("modelo.id"), nullable=False)
    modelo = relationship("Modelo")
    rodas_id = Column(Integer, ForeignKey("rodas.id"), nullable=False)
    rodas = relationship("Rodas")
    marca_id = Column(Integer, ForeignKey("marca.id"), nullable=False)
    marca = relationship("Marca")


    def __repr__(self):
        return self.condutor

class Infracao(Model):
    id = Column(Integer,primary_key=True)
    descricao = Column(String(250), unique=True, nullable=False)
    numero = Column(Integer,unique=True)



    def __repr__(self):
        return self.descricao

class Condutor(Model):
    id = Column(Integer,primary_key=True)
    nome_completo = Column(String(250), unique=True,nullable=False)
    cpf = Column(Integer,unique=True, nullable=False)
    rg = Column(Integer, unique=True,nullable=False)
    cnh = Column(Integer,unique=True, nullable=False)
    endereco = Column(String(250),nullable=False)
    tipo_sanguinio = Column(String(5))
    infracao_id = Column(Integer, ForeignKey("infracao.id"), nullable=False)
    infracao = relationship("Infracao")

    def __repr__(self):
        return self.nome_completo

class HistoricoCondutor(Model):
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return self.id

assoc_veiculo_condutor = (
    "veiculo_condutor",
    Model.metadata,
    Column("id", Integer, primary_key=True),
    Column("veiculo_id", Integer, ForeignKey("veiculo.id")),
    Column("condutor_id", Integer, ForeignKey("condutor.id")),
)
