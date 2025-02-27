from functools import wraps
from typing import Any, Callable, Coroutine, Optional, ParamSpec, Type, TypeVar, Union, overload

from aiohttp import ClientResponse
from pydantic import BaseModel

from utils.exceptions import RequestException

PydanticModel = TypeVar("PydanticModel", bound=BaseModel)
P = ParamSpec("P")


@overload
def handle_api_response(
    pydantic_model: Type[PydanticModel],
) -> Callable[
    [Callable[P, Coroutine[Any, Any, tuple[ClientResponse, dict]]]],
    Callable[P, Coroutine[Any, Any, PydanticModel]],
]: ...


@overload
def handle_api_response(
    pydantic_model: None = ...,
) -> Callable[
    [Callable[P, Coroutine[Any, Any, tuple[ClientResponse, dict]]]],
    Callable[P, Coroutine[Any, Any, dict]],
]: ...


def handle_api_response(
    pydantic_model: Optional[Type[PydanticModel]] = None,
) -> Callable[
    [Callable[P, Coroutine[Any, Any, tuple[ClientResponse, dict]]]],
    Callable[P, Coroutine[Any, Any, Union[PydanticModel, dict]]],
]:
    """
    Decorator function that handles the response from an API call, parsing the response into
    a Pydantic model if provided, or returning the raw JSON response.
    """

    def decorator(
        func: Callable[P, Coroutine[Any, Any, tuple[ClientResponse, dict]]],
    ) -> Callable[P, Coroutine[Any, Any, Union[PydanticModel, dict]]]:
        @wraps(func)
        async def wrapper(*args: P.args, **kwargs: P.kwargs) -> Union[PydanticModel, dict]:
            response, json_response = await func(*args, **kwargs)

            if not response.ok:
                raise RequestException(status_code=response.status, error_info=json_response)

            if pydantic_model:
                return pydantic_model.model_validate(json_response)

            return json_response

        return wrapper

    return decorator
