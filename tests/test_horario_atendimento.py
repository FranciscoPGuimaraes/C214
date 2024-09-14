import unittest
from unittest.mock import MagicMock
from c214.horarios import HorarioAtendimento
from tests.horariosMock import *


class test_horario_atendimento(unittest.TestCase):
    def setUp(self):
        # Criar um mock para o HorarioAtendimentoService
        self.mock_service = MagicMock()
        self.horario_atendimento = HorarioAtendimento(service=self.mock_service)

    # teste ok - Positivo
    def test_buscar_horario_chris(self):
        self.mock_service.busca_horario.return_value = HORARIOS_CHRIS
        resultado = self.horario_atendimento.buscar_horario(199)
        self.assertEqual(resultado["nomeDoProfessor"], "Prof. Chris")

    # teste ok - Positivo
    def test_buscar_predio_atendimento_laura(self):
        self.mock_service.busca_horario.return_value = HORARIOS_LAURA
        resultado = self.horario_atendimento.buscar_horario(139)
        self.assertEqual(resultado["predio"], 2)

    # teste ok - Negativo
    def test_buscar_horario_predio_fora_intervalo(self):
        self.mock_service.busca_horario.return_value = HORARIOS_XICO
        resultado = self.horario_atendimento.buscar_horario(198)
        self.assertEqual(resultado, "Predio não existe")

    # teste ok - Negativo
    def test_buscar_horario_professor_inexistente(self):
        self.mock_service.busca_horario.return_value = None
        resultado = self.horario_atendimento.buscar_horario(999)
        self.assertEqual(resultado, "Professor não encontrado")

    # teste ok - Positivo
    def test_buscar_sala(self):
        self.mock_service.busca_por_sala.return_value = SALA_10
        resultado = self.horario_atendimento.buscar_por_sala(10)
        self.assertEqual(resultado, {
            "sala": 10,
            "predio": 2,
            "horarios_livres": ["12:00", "13:00", "15:00"]
        })

    # teste ok - Negativo
    def test_buscar_sala_com_numero_inexistente(self):
        self.mock_service.busca_por_sala.return_value = None
        resultado = self.horario_atendimento.buscar_por_sala(170)
        self.assertEqual(resultado, "Sala não econtrada")

    # teste ok - Negativo
    def test_buscar_por_sala_predio_fora_do_intervalo(self):
        self.mock_service.busca_por_sala.return_value = SALA_27
        resultado = self.horario_atendimento.buscar_por_sala(27)
        self.assertEqual(resultado, "Predio não existe")

    #teste ok - positivo
    def test_buscar_horario_pedro(self):
        self.mock_service.busca_horario.return_value = HORARIOS_PEDRO
        resultado = self.horario_atendimento.buscar_horario(200)
        self.assertEqual(resultado["nomeDoProfessor"], "Prof. Pedro")
        self.assertEqual(resultado["predio"], 3)

    #positivo
    def test_inserir_horario(self):
        self.mock_service.inserir_horario.return_value = True
        resultado = self.horario_atendimento.inserir_horario(101, "08:00 - 10:00", "Integral", 4)
        self.assertEqual(resultado, True)

    #negativo
    def test_inserir_horario_invalido(self):
        self.mock_service.inserir_horario.return_value = False
        resultado = self.horario_atendimento.inserir_horario(12, "00", "Integral", 4)
        self.assertEqual(resultado, False)

    #negativo
    def test_inserir_horario_periodo_invalido(self):
        self.mock_service.inserir_horario.return_value = False
        resultado = self.horario_atendimento.inserir_horario(101, "08:00 - 10:00", "Madrugada", 4)
        self.assertEqual(resultado, "Periodo invalido")

    #negativo
    def test_inserir_horario_sala_invalida(self):
        self.mock_service.inserir_horario.return_value = "Sala inválida"
        resultado = self.horario_atendimento.inserir_horario(101, "08:00 - 10:00", "Integral", 40)
        self.assertEqual(resultado, "Sala inválida")

    # positivo
    def test_inserir_horario_noturno(self):
        self.mock_service.inserir_horario.return_value = True
        resultado = self.horario_atendimento.inserir_horario(121, "08:00 - 10:00", "Noturno", 9)
        self.assertEqual(resultado, True)

    def test_buscar_horario_ana(self):
        self.mock_service.busca_horario.return_value = HORARIOS_ANA
        resultado = self.horario_atendimento.buscar_horario(200)
        self.assertEqual(resultado["nomeDoProfessor"], "Prof. Ana")
        self.assertEqual(resultado["predio"], 3)

    def test_buscar_sala_20(self):
        self.mock_service.busca_por_sala.return_value = SALA_20
        resultado = self.horario_atendimento.buscar_por_sala(20)
        self.assertEqual(resultado, {
            "sala": 20,
            "predio": 3,
            "horarios_livres": []
        })
