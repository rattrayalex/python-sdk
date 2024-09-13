# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .tool import Tool
from .message import Message
from ..._models import BaseModel

__all__ = [
    "ChatInput",
    "ResponseFormat",
    "ResponseFormatSimpleCompletionResponseFormat",
    "ResponseFormatSchemaCompletionResponseFormat",
    "ToolChoice",
    "ToolChoiceNamedFunctionChoice",
    "ToolChoiceNamedFunctionChoiceFunction",
    "ToolChoiceNamedIntegrationChoice",
    "ToolChoiceNamedSystemChoice",
    "ToolChoiceNamedAPICallChoice",
]


class ResponseFormatSimpleCompletionResponseFormat(BaseModel):
    type: Optional[Literal["text", "json_object"]] = None


class ResponseFormatSchemaCompletionResponseFormat(BaseModel):
    json_schema: object

    type: Optional[Literal["json_schema"]] = None


ResponseFormat: TypeAlias = Union[
    ResponseFormatSimpleCompletionResponseFormat, ResponseFormatSchemaCompletionResponseFormat, None
]


class ToolChoiceNamedFunctionChoiceFunction(BaseModel):
    name: str


class ToolChoiceNamedFunctionChoice(BaseModel):
    function: ToolChoiceNamedFunctionChoiceFunction


class ToolChoiceNamedIntegrationChoice(BaseModel):
    integration: Optional[object] = None


class ToolChoiceNamedSystemChoice(BaseModel):
    system: Optional[object] = None


class ToolChoiceNamedAPICallChoice(BaseModel):
    api_call: Optional[object] = None


ToolChoice: TypeAlias = Union[
    Literal["auto", "none"],
    ToolChoiceNamedFunctionChoice,
    ToolChoiceNamedIntegrationChoice,
    ToolChoiceNamedSystemChoice,
    ToolChoiceNamedAPICallChoice,
    None,
]


class ChatInput(BaseModel):
    messages: List[Message]

    agent: Optional[str] = None

    frequency_penalty: Optional[float] = None

    length_penalty: Optional[float] = None

    logit_bias: Optional[Dict[str, float]] = None

    max_tokens: Optional[int] = None

    min_p: Optional[float] = None

    model: Optional[str] = None

    presence_penalty: Optional[float] = None

    recall: Optional[bool] = None

    remember: Optional[bool] = None

    repetition_penalty: Optional[float] = None

    response_format: Optional[ResponseFormat] = None

    save: Optional[bool] = None

    seed: Optional[int] = None

    stop: Optional[List[str]] = None

    stream: Optional[bool] = None

    temperature: Optional[float] = None

    tool_choice: Optional[ToolChoice] = None

    tools: Optional[List[Tool]] = None

    top_p: Optional[float] = None
