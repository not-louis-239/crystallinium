from __future__ import annotations

from typing import Any, TypeAlias
from abc import ABC, abstractmethod

_JSONObject: TypeAlias = dict[str, Any]

class JSONConvertible(ABC):
    @abstractmethod
    def to_json(self) -> _JSONObject:
        raise NotImplementedError

    @abstractmethod
    @classmethod
    def from_json(cls, json_data: _JSONObject) -> JSONConvertible:
        raise NotImplementedError
