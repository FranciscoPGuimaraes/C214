import json

from c214.horarioAtendimentoService import HorarioAtendimentoService


class HorarioAtendimento:
    def __init__(self, service: HorarioAtendimentoService) -> None:
        self.service = service

    def buscar_horario(self, professor_id: int):
        json_response = self.service.busca_horario(professor_id)
        if json_response:
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
        return "Professor não encontrado"

    def buscar_por_sala(self, sala: int):
        horario_json = self.service.busca_por_sala(sala)

        if horario_json:
            dados = json.loads(horario_json)
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
                "sala": dados["sala"],
                "predio": predio,
                "horarios_livres": dados["horarios_livres"]
            }

        return "Sala não econtrada"

    def inserir_horario(self, professor_id: int, horario_atendimento: str, periodo: str, sala: int):
        if 1 > sala > 25: return "Sala inválida"
        if periodo not in ["Integral", "Noturno"]: return "Periodo invalido"

        novo_horario = {
            "professor_id": professor_id,
            "horarioDeAtendimento": horario_atendimento,
            "periodo": periodo,
            "sala": sala
        }

        horario_json = json.dumps(novo_horario)

        return self.service.inserir_horario(professor_id, horario_json)
