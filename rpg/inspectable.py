from abc import ABC, abstractmethod
from copy import deepcopy


class Inspectable(ABC):
    """
    An abstract base class that represents an inspectable object.
    """
    def __init__(self, description: str) -> None:
        """
        Initializes the inspectable instance

        parameters:
        description (str): The message that the inspectable object will print.
        """
        self._description = description

    @property
    def description(self) -> str:
        """
        A getter for the description of the object

        returns:
        a deepcopy of the description in order to make it immutable.
        """
        return deepcopy(self._description)

    @abstractmethod
    def inspect(self) -> None:
        """
        Abstract method that has to be implemented by it'ssubclasses to
        provide the inspection.
        """
        pass
