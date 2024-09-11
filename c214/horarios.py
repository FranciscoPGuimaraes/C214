import json
from horarioAtendimentoService import HorarioAtendimentoService

class HorarioAtendimento:
    def __init__(self, service: HorarioAtendimentoService) -> None:
        self.service = service

    def buscar_horario(self, professor_id: int):
        json_response = self.service.busca_horario(professor_id)
        dados = json.loads(json_response)

        sala = int(dados["sala"])
        if 1 <= sala <= 5:
            predio = 1
        elif 6 <= sala <= 10:
            predio = 2
        else:
            predio = 3

        return {
            "nomeDoProfessor": dados["nomeDoProfessor"],
            "horarioDeAtendimento": dados["horarioDeAtendimento"],
            "periodo": dados["periodo"],
            "sala": dados["sala"],
            "predio": predio
        }