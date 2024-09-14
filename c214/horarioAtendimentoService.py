from abc import ABC, abstractmethod

class HorarioAtendimentoService(ABC):

    @abstractmethod
    def busca_horario(self, professor_id: int) -> str:
        pass

    @abstractmethod
    def busca_por_sala(self, sala_id: int) -> str:
        pass

    @abstractmethod
    def inserir_horario(self, professor_id: int, horarios) -> bool:
        pass

    @abstractmethod
    def reservar_sala(self, sala_id: int, horario: str) -> bool:
        pass