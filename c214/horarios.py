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
        elif 11 <= sala <= 20:
            predio = 3
        elif 21 <= sala <= 25:
            predio = 6
        else:
            return "Predio não existe"

        return {
            "nomeDoProfessor": dados["nomeDoProfessor"],
            "horarioDeAtendimento": dados["horarioDeAtendimento"],
            "periodo": dados["periodo"],
            "sala": dados["sala"],
            "predio": predio
        }

    def buscar_professor_pelo_horario(self, hora):
        for horario_json in HORARIOS:
            dados = json.loads(horario_json)
            if dados["horarioDeAtendimento"] == hora:
                return {
                    "nomeDoProfessor": dados["nomeDoProfessor"],
                    "horarioDeAtendimento": dados["horarioDeAtendimento"],
                    "periodo": dados["periodo"],
                    "sala": dados["sala"],
                    "predio": dados["predio"]
                }

        return "Nenhum professor disponível/Horario digitado incorretamente"

    def buscar_professor(self, professor: str):
        for horario_json in HORARIOS:
            dados = json.loads(horario_json)
            if dados["nomeDoProfessor"] == professor:
                return {
                    "nomeDoProfessor": dados["nomeDoProfessor"],
                    "horarioDeAtendimento": dados["horarioDeAtendimento"],
                    "periodo": dados["periodo"],
                    "sala": dados["sala"],
                    "predio": dados["predio"]
                }

        return "Nome do Professor Incorreto"

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

        return "Sala sem atendimento/digitada de forma incorreta"

    def buscar_por_predio(self, predio):
        for horario_json in HORARIOS:
            dados = json.loads(horario_json)
            if dados["predio"] == predio:
                return {
                    "nomeDoProfessor": dados["nomeDoProfessor"],
                    "horarioDeAtendimento": dados["horarioDeAtendimento"],
                    "periodo": dados["periodo"],
                    "sala": dados["sala"],
                    "predio": dados["predio"]
                }

        return "Predio não existe/digitado de forma incorreta"

