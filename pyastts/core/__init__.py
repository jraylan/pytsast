"""
Core module - Base types and serialization infrastructure.
"""

from pyastts.core.base import Node, NodeList
from pyastts.core.types import (
    LiteralValue,
    Undefined,
    undefined,
    SerializedLiteral,
    SerializedNumber,
    SerializedFactory,
    SerializedUndefined,
    SerializedNode,
)
from pyastts.core.serializer import Serializer
from pyastts.core.syntax_kind import SyntaxKind, NodeFlags

__all__ = [
    "Node",
    "NodeList",
    "LiteralValue",
    "Undefined",
    "undefined",
    "SerializedFactory",
    "SerializedLiteral",
    "SerializedNode",
    "SerializedNumber",
    "SerializedUndefined",
    "Serializer",
    "SyntaxKind",
    "NodeFlags",
]
