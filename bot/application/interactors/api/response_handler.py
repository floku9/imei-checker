from typing import TypeVar, Callable, Coroutine, Any, Type, Union, Optional, overload
from pydantic import BaseModel
from aiohttp import ClientResponse
from functools import wraps

from utils.exceptions import RequestException

T = TypeVar("T", bound=BaseModel)


@overload
def handle_api_response(pydantic_model: Type[T]) -> Callable[
    [Callable[..., Coroutine[Any, Any, tuple[ClientResponse, dict]]]],
    Callable[..., Coroutine[Any, Any, T]],
]: ...


@overload
def handle_api_response(pydantic_model: None = ...) -> Callable[
    [Callable[..., Coroutine[Any, Any, tuple[ClientResponse, dict]]]],
    Callable[..., Coroutine[Any, Any, dict]],
]: ...


def handle_api_response(
    pydantic_model: Optional[Type[T]] = None,
) -> Callable[
    [Callable[..., Coroutine[Any, Any, tuple[ClientResponse, dict]]]],
    Callable[..., Coroutine[Any, Any, Union[T, dict]]],
]:
    """
    Decorator function that handles the response from an API call, parsing the response into
    a Pydantic model if provided, or returning the raw JSON response.

    The decorator takes an optional `pydantic_model` parameter, which is a Pydantic model class.
    If provided, the decorator will parse the JSON response into an instance of the specified model.
    If not provided, the decorator will return the raw JSON response.

    The decorator also handles errors, raising a `RequestException` if the API response
    is not successful (i.e. the status code is not in the 2xx range).

    """

    def decorator(
        func: Callable[..., Coroutine[Any, Any, tuple[ClientResponse, dict]]]
    ) -> Callable[..., Coroutine[Any, Any, Union[T, dict]]]:
        @wraps(func)
        async def wrapper(*args, **kwargs) -> Union[T, dict]:
            response, json_response = await func(*args, **kwargs)

            if not response.ok:
                raise RequestException(status_code=response.status, error_info=json_response)

            if pydantic_model is not None:
                return pydantic_model.parse_obj(json_response)

            return json_response

        return wrapper

    return decorator
