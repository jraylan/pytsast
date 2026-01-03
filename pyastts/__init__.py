"""
PyASTTS - Python TypeScript AST Generator

Create TypeScript AST nodes from Python and serialize to JSON
for processing by the TypeScript compiler API.
"""

from pyastts.core.base import Node
from pyastts.core.serializer import Serializer
from pyastts.core.syntax_kind import SyntaxKind
from pyastts import factory
from pyastts.cli import generate_typescript, generate_typescript_inline

__all__ = [
    "Node",
    "Serializer",
    "factory",
    "SyntaxKind",
    "generate_typescript",
    "generate_typescript_inline",
]

__version__ = "0.1.0"
