"""
Binding pattern AST nodes - Object and Array destructuring.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar, Sequence

from pyastts.core.base import Node
from pyastts.core.types import Undefined, undefined

if TYPE_CHECKING:
    from pyastts.nodes.common import Identifier
    from pyastts.nodes.expressions import Expression


class ObjectBindingPattern(Node):
    """
    Represents an object binding pattern: { a, b: c }.

    TypeScript: ts.factory.createObjectBindingPattern(elements)
    """

    factory_name: ClassVar[str] = "createObjectBindingPattern"

    elements: Sequence["BindingElement"]


class ArrayBindingPattern(Node):
    """
    Represents an array binding pattern: [a, b, c].

    TypeScript: ts.factory.createArrayBindingPattern(elements)
    """

    factory_name: ClassVar[str] = "createArrayBindingPattern"

    elements: Sequence["BindingElement | Node"]  # OmittedExpression allowed


class BindingElement(Node):
    """
    Represents a binding element: a or a = default or ...rest.

    TypeScript: ts.factory.createBindingElement(dotDotDotToken?, propertyName?,
      name, initializer?)
    """

    factory_name: ClassVar[str] = "createBindingElement"

    dot_dot_dot_token: Node | Undefined = undefined
    property_name: "Identifier | str | Node | Undefined" = undefined
    name: "Identifier | ObjectBindingPattern | ArrayBindingPattern | str"
    initializer: "Expression | Undefined" = undefined
