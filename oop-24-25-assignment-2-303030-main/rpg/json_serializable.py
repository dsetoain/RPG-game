from abc import ABC, abstractmethod
from typing import Dict, Any


class JsonSerializable(ABC):
    def to_JSON(self) -> Dict[str, Any]:
        """
        Serializes the object's attributes into a JSON-friendly format.
        """
        serialized_data = {}
        for key, value in self.__dict__.items():
            if isinstance(value, (int, float, str, bool, type(None),
                                  list, dict, tuple)):
                serialized_data[key] = value
            else:
                raise TypeError(f"Attribute {key} of type {type(value)} "
                                "is not serializable.")
        return serialized_data

    @abstractmethod
    def from_json(self, data: Dict[str, Any]) -> 'JsonSerializable':
        """
        Abstract method that all subclasses must implement.
        """
        pass
