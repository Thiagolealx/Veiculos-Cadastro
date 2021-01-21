from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi

from . import appbuilder, db
from .models import Rodas, Modelo, Marca, Veiculo,Infracao, Condutor, HistoricoCondutor

class VeiculoView(ModelView):
    datamodel = SQLAInterface(Veiculo)
    related_views = [Veiculo]

class RodasView(ModelView):
    datamodel = SQLAInterface(Rodas)
    related_views = [Veiculo]

class ModeloView(ModelView):
    datamodel = SQLAInterface(Modelo)
    related_views = [Veiculo]

class MarcaView(ModelView):
    datamodel = SQLAInterface(Marca)
    related_views = [Veiculo]

class CondutorView(ModelView):
    datamodel = SQLAInterface(Condutor)
    related_views = [Condutor]

class InfracaoView(ModelView):
    datamodel = SQLAInterface(Infracao)
    related_views = [Condutor]

class HistoricoCondutorView(ModelView):
    datamodel = SQLAInterface(HistoricoCondutor)
    list_columns = ["nome_completo", "marca", "modelo"]
    related_views = [Condutor]


appbuilder.add_view(
    VeiculoView, "Veiculo", icon="fa-folder-open-o", category="Veiculo"
)
appbuilder.add_separator("Veiculo")
appbuilder.add_view(
    RodasView, "Rodas", icon="fa-folder-open-o", category="Veiculo"
)
appbuilder.add_view(
    MarcaView, "Marca", icon="fa-folder-open-o", category="Veiculo"
)
appbuilder.add_view(
    ModeloView, "Modelo", icon="fa-folder-open-o", category="Veiculo"
)


appbuilder.add_view(
    CondutorView, "Condutor", icon="fa-folder-open-o", category="Condutor"
)
appbuilder.add_separator("Condutor")
appbuilder.add_view(
    InfracaoView, "Infração", icon="fa-folder-open-o", category="Condutor"
)
appbuilder.add_view(
    HistoricoCondutorView, "Historico Condutor", icon="fa-folder-open-o", category="Condutor"
)


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )


db.create_all()
