"""Define parameters used by CLI app.

Parameters annotated definition as used by
`Typer` framework as parameters in components
and described through `Annotated` class.

Author: Petre Iordanescu (petre.iordanescu@gmail.com)
"""

import typer
from typing import NewType
from typing_extensions import Annotated


#TODO use type definition as importable
#  and reusable type in CLI commands
UserId = NewType('UserId', int)  # `UserId` type used for ...xxx...

some_id = UserId(524313)

#TODO Typer varian
param_x = Annotated[
        str,
        typer.Argument()
    ]  # `param_x` of str type and  Annotated rype used for ...xxx...


#TODO and when use type:
def get_user_name(user_id: UserId) -> str:
    """Test & proof of concept for new rype usage.
    """
    # passes type checking
    user_a = get_user_name(UserId(42351))# 

    # fails type checking; an int is not a UserId
    user_b = get_user_name(-1)




