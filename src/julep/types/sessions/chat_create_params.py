# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "ChatCreateParams",
    "Message",
    "MessageContentUnionMember2",
    "MessageContentUnionMember2Content",
    "MessageContentUnionMember2ContentModel",
    "MessageContentUnionMember2ContentModelImageURL",
    "ResponseFormat",
    "ResponseFormatSimpleCompletionResponseFormat",
    "ResponseFormatSchemaCompletionResponseFormat",
    "ToolChoice",
    "ToolChoiceNamedFunctionChoice",
    "ToolChoiceNamedFunctionChoiceFunction",
    "ToolChoiceNamedIntegrationChoice",
    "ToolChoiceNamedSystemChoice",
    "ToolChoiceNamedAPICallChoice",
    "Tool",
    "ToolFunction",
]


class ChatCreateParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]

    agent: Optional[str]

    frequency_penalty: Optional[float]

    length_penalty: Optional[float]

    logit_bias: Optional[Dict[str, float]]

    max_tokens: Optional[int]

    min_p: Optional[float]

    model: Optional[str]

    presence_penalty: Optional[float]

    recall: bool

    repetition_penalty: Optional[float]

    response_format: Optional[ResponseFormat]

    save: bool

    seed: Optional[int]

    stop: List[str]

    stream: bool

    temperature: Optional[float]

    tool_choice: Optional[ToolChoice]

    tools: Iterable[Tool]

    top_p: Optional[float]


class MessageContentUnionMember2Content(TypedDict, total=False):
    text: Required[str]

    type: Literal["text"]


class MessageContentUnionMember2ContentModelImageURL(TypedDict, total=False):
    url: Required[str]

    detail: Literal["low", "high", "auto"]


class MessageContentUnionMember2ContentModel(TypedDict, total=False):
    image_url: Required[MessageContentUnionMember2ContentModelImageURL]
    """The image URL"""

    type: Literal["image_url"]


MessageContentUnionMember2: TypeAlias = Union[MessageContentUnionMember2Content, MessageContentUnionMember2ContentModel]

_MessageReservedKeywords = TypedDict(
    "_MessageReservedKeywords",
    {
        "continue": Optional[bool],
    },
    total=False,
)


class Message(_MessageReservedKeywords, total=False):
    content: Required[Union[str, List[str], Iterable[MessageContentUnionMember2]]]

    role: Required[Literal["user", "assistant", "system", "function", "function_response", "function_call", "auto"]]

    name: Optional[str]


class ResponseFormatSimpleCompletionResponseFormat(TypedDict, total=False):
    type: Literal["text", "json_object"]


class ResponseFormatSchemaCompletionResponseFormat(TypedDict, total=False):
    json_schema: Required[object]

    type: Literal["json_schema"]


ResponseFormat: TypeAlias = Union[
    ResponseFormatSimpleCompletionResponseFormat, ResponseFormatSchemaCompletionResponseFormat
]


class ToolChoiceNamedFunctionChoiceFunction(TypedDict, total=False):
    name: Required[str]


class ToolChoiceNamedFunctionChoice(TypedDict, total=False):
    function: Required[ToolChoiceNamedFunctionChoiceFunction]


class ToolChoiceNamedIntegrationChoice(TypedDict, total=False):
    integration: Optional[object]


class ToolChoiceNamedSystemChoice(TypedDict, total=False):
    system: Optional[object]


class ToolChoiceNamedAPICallChoice(TypedDict, total=False):
    api_call: Optional[object]


ToolChoice: TypeAlias = Union[
    Literal["auto", "none"],
    ToolChoiceNamedFunctionChoice,
    ToolChoiceNamedIntegrationChoice,
    ToolChoiceNamedSystemChoice,
    ToolChoiceNamedAPICallChoice,
]


class ToolFunction(TypedDict, total=False):
    description: Optional[str]

    name: Optional[object]

    parameters: Optional[object]


class Tool(TypedDict, total=False):
    function: Required[ToolFunction]
    """Function definition"""

    name: Required[str]

    api_call: Optional[object]

    integration: Optional[object]

    system: Optional[object]

    type: Literal["function", "integration", "system", "api_call"]
