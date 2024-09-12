import json

from c214.horarioAtendimentoService import HorarioAtendimentoService


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

    def buscar_por_sala(self, sala: int):
        salas_com_atendimento = [22, 15, 12, 7]

        if sala not in salas_com_atendimento:
            return "Sala sem atendimento"
        else:
            json_response = self.service.busca_por_sala(sala)
            dados = json.loads(json_response)

            return {
                "nomeDoProfessor": dados["nomeDoProfessor"],
                "horarioDeAtendimento": dados["horarioDeAtendimento"],
                "periodo": dados["periodo"],
                "sala": dados["sala"],
                "predio": dados["predio"]
            }