import json

from c214.horarioAtendimentoService import HorarioAtendimentoService
from tests.horariosMock import HORARIOS


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
        for horario_json in HORARIOS:
            dados = json.loads(horario_json)
            if dados["sala"] == sala:
                return {
                    "nomeDoProfessor": dados["nomeDoProfessor"],
                    "horarioDeAtendimento": dados["horarioDeAtendimento"],
                    "periodo": dados["periodo"],
                    "sala": dados["sala"],
                    "predio": dados["predio"]
                }

        return "Sala sem atendimento"

    def buscar_horarios_professor(self, nome_professor: str):
        json_response = self.service.busca_horarios_professor(nome_professor)

        if not json_response:
            return "Professor não encontrado"

        dados = json.loads(json_response)

        if dados["nomeDoProfessor"].lower() == nome_professor.lower():
            return {
                "nomeDoProfessor": dados["nomeDoProfessor"],
                "horarioDeAtendimento": dados["horarioDeAtendimento"],
                "periodo": dados["periodo"],
                "sala": dados["sala"],
                "predio": dados["predio"]
            }
        else:
            return "Nome do professor não encontrado"

