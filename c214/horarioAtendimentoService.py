from abc import ABC, abstractmethod

class HorarioAtendimentoService(ABC):

    @abstractmethod
    def busca_horario(self, professor_id: int) -> str:
        pass