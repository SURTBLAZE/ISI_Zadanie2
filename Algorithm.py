from abc import abstractmethod, ABC

from Field import Field


class Algorithm(ABC):
    @abstractmethod
    def run(self) -> Field | None:
        pass
