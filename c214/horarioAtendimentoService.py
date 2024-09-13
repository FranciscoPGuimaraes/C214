from abc import ABC, abstractmethod
from typing import Optional

class HorarioAtendimentoService(ABC):

    @abstractmethod
    def busca_horario(self, professor_id: int) -> str:
        pass

    @abstractmethod
    def busca_por_sala(self, sala_id: int) -> str:
        pass

    @abstractmethod
    def busca_horarios_professor(self, nome_professor: str) -> Optional[str]:
        pass

