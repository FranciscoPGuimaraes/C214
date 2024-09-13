import unittest
from unittest.mock import MagicMock
from c214.horarios import HorarioAtendimento
from tests.horariosMock import *


class TestHorarioAtendimento(unittest.TestCase):
    def setUp(self):
        # Criar um mock para o HorarioAtendimentoService
        self.mock_service = MagicMock()
        self.horario_atendimento = HorarioAtendimento(service=self.mock_service)

    #teste ok
    def test_buscar_horario_chris(self):
        self.mock_service.busca_horario.return_value = HORARIOS_CHRIS
        resultado = self.horario_atendimento.buscar_horario(4)
        self.assertEqual(resultado["nomeDoProfessor"], "Prof. Chris")

    #teste ok
    def test_buscar_predio_atendimento_laura(self):
        self.mock_service.busca_horario.return_value = HORARIOS_LAURA
        resultado = self.horario_atendimento.buscar_horario(7)
        self.assertEqual(resultado["predio"], 2)

    #teste ok
    def test_buscar_dados_completos_professor_xico(self):
        self.mock_service.busca_horario.return_value = HORARIOS_XICO
        resultado = self.horario_atendimento.buscar_horario(12)
        self.assertEqual(resultado, {
            "nomeDoProfessor": "Prof. Xico",
            "horarioDeAtendimento": "10:00 - 12:00",
            "periodo": "Integral",
            "sala": 12,
            "predio": 3
            })

    #teste ok
    def test_buscar_sala_sem_atendimento(self):
        resultado = self.horario_atendimento.buscar_por_sala(10)
        self.assertEqual(resultado, 'Sala sem atendimento')

    #teste ok
    def test_buscar_professor_na_sala(self):
        self.mock_service.busca_por_sala.return_value = HORARIOS_PEDRO
        resultado = self.horario_atendimento.buscar_por_sala(15)
        self.assertEqual(resultado["nomeDoProfessor"], 'Prof. Pedro')


    def test_buscar_dados_incompletos_professor_chris(self):
        self.mock_service.busca_horario.return_value = HORARIOS_XICO
        resultado = self.horario_atendimento.buscar_horario(12)
        self.assertEqual(resultado["nomeDoProfessor"], "Prof. Xico")
        self.assertEqual(resultado["horarioDeAtendimento"], "10:00 - 12:00")
        self.assertNotEqual(resultado["periodo"], "Noturno")
        self.assertEqual(resultado["sala"], 12)
        self.assertEqual(resultado["predio"], 3)

    #teste ok
    def test_busca_prof_nome_errado_test(self):
        self.mock_service.busca_horarios_professor.return_value = HORARIOS_CHRIS
        resultado = self.horario_atendimento.buscar_horarios_professor("Prof. Crhis")
        self.assertEqual(resultado, "Nome do professor não encontrado")

    #teste ok
    def test_buscar_horarios_professor_inexistente(self):
        self.mock_service.busca_horarios_professor.return_value = None
        resultado = self.horario_atendimento.buscar_horarios_professor(None)

        self.assertNotEqual(resultado["nomeDoProfessor"], "Professor encontrado")

    def test_buscar_horarios_inexistente(self):
        self.mock_service.busca_horarios_professor.return_value = HORARIOS_ANA
        resultado = self.horario_atendimento.buscar_horarios_professor("Prof. Ana")

        self.assertNotEqual(resultado["horarioDeAtendimento"], "13h")

    def test_buscar_predio_invalido(self):
        self.mock_service.busca_horarios_professor.return_value = HORARIOS_ANA
        resultado = self.horario_atendimento.buscar_horarios_professor("Prof. Ana")

        self.assertNotEqual(resultado["predio"], "predio1")