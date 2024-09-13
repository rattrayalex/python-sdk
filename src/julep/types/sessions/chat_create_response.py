# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "ChatCreateResponse",
    "ChunkChatResponse",
    "ChunkChatResponseChoice",
    "ChunkChatResponseChoiceDelta",
    "ChunkChatResponseChoiceDeltaContentUnionMember2",
    "ChunkChatResponseChoiceDeltaContentUnionMember2Content",
    "ChunkChatResponseChoiceDeltaContentUnionMember2ContentModel",
    "ChunkChatResponseChoiceDeltaContentUnionMember2ContentModelImageURL",
    "ChunkChatResponseChoiceLogprobs",
    "ChunkChatResponseChoiceLogprobsContent",
    "ChunkChatResponseChoiceLogprobsContentTopLogprob",
    "ChunkChatResponseDoc",
    "ChunkChatResponseDocOwner",
    "ChunkChatResponseDocSnippet",
    "ChunkChatResponseUsage",
    "MessageChatResponse",
    "MessageChatResponseChoice",
    "MessageChatResponseChoiceSingleChatOutput",
    "MessageChatResponseChoiceSingleChatOutputMessage",
    "MessageChatResponseChoiceSingleChatOutputMessageContentUnionMember2",
    "MessageChatResponseChoiceSingleChatOutputMessageContentUnionMember2Content",
    "MessageChatResponseChoiceSingleChatOutputMessageContentUnionMember2ContentModel",
    "MessageChatResponseChoiceSingleChatOutputMessageContentUnionMember2ContentModelImageURL",
    "MessageChatResponseChoiceSingleChatOutputMessageToolCall",
    "MessageChatResponseChoiceSingleChatOutputMessageToolCallChosenFunctionCall",
    "MessageChatResponseChoiceSingleChatOutputMessageToolCallChosenFunctionCallFunction",
    "MessageChatResponseChoiceSingleChatOutputMessageToolCallChosenIntegrationCall",
    "MessageChatResponseChoiceSingleChatOutputMessageToolCallChosenSystemCall",
    "MessageChatResponseChoiceSingleChatOutputMessageToolCallChosenAPICall",
    "MessageChatResponseChoiceSingleChatOutputLogprobs",
    "MessageChatResponseChoiceSingleChatOutputLogprobsContent",
    "MessageChatResponseChoiceSingleChatOutputLogprobsContentTopLogprob",
    "MessageChatResponseChoiceMultipleChatOutput",
    "MessageChatResponseChoiceMultipleChatOutputMessage",
    "MessageChatResponseChoiceMultipleChatOutputMessageContentUnionMember2",
    "MessageChatResponseChoiceMultipleChatOutputMessageContentUnionMember2Content",
    "MessageChatResponseChoiceMultipleChatOutputMessageContentUnionMember2ContentModel",
    "MessageChatResponseChoiceMultipleChatOutputMessageContentUnionMember2ContentModelImageURL",
    "MessageChatResponseChoiceMultipleChatOutputMessageToolCall",
    "MessageChatResponseChoiceMultipleChatOutputMessageToolCallChosenFunctionCall",
    "MessageChatResponseChoiceMultipleChatOutputMessageToolCallChosenFunctionCallFunction",
    "MessageChatResponseChoiceMultipleChatOutputMessageToolCallChosenIntegrationCall",
    "MessageChatResponseChoiceMultipleChatOutputMessageToolCallChosenSystemCall",
    "MessageChatResponseChoiceMultipleChatOutputMessageToolCallChosenAPICall",
    "MessageChatResponseChoiceMultipleChatOutputLogprobs",
    "MessageChatResponseChoiceMultipleChatOutputLogprobsContent",
    "MessageChatResponseChoiceMultipleChatOutputLogprobsContentTopLogprob",
    "MessageChatResponseDoc",
    "MessageChatResponseDocOwner",
    "MessageChatResponseDocSnippet",
    "MessageChatResponseUsage",
]


class ChunkChatResponseChoiceDeltaContentUnionMember2Content(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class ChunkChatResponseChoiceDeltaContentUnionMember2ContentModelImageURL(BaseModel):
    url: str

    detail: Optional[Literal["low", "high", "auto"]] = None


class ChunkChatResponseChoiceDeltaContentUnionMember2ContentModel(BaseModel):
    image_url: ChunkChatResponseChoiceDeltaContentUnionMember2ContentModelImageURL
    """The image URL"""

    type: Optional[Literal["image_url"]] = None


ChunkChatResponseChoiceDeltaContentUnionMember2: TypeAlias = Union[
    ChunkChatResponseChoiceDeltaContentUnionMember2Content, ChunkChatResponseChoiceDeltaContentUnionMember2ContentModel
]


class ChunkChatResponseChoiceDelta(BaseModel):
    content: Union[str, List[str], List[ChunkChatResponseChoiceDeltaContentUnionMember2]]

    role: Literal["user", "assistant", "system", "function", "function_response", "function_call", "auto"]

    continue_: Optional[bool] = FieldInfo(alias="continue", default=None)

    name: Optional[str] = None


class ChunkChatResponseChoiceLogprobsContentTopLogprob(BaseModel):
    token: str

    logprob: float

    bytes: Optional[List[int]] = None


class ChunkChatResponseChoiceLogprobsContent(BaseModel):
    token: str

    logprob: float

    top_logprobs: List[ChunkChatResponseChoiceLogprobsContentTopLogprob]

    bytes: Optional[List[int]] = None


class ChunkChatResponseChoiceLogprobs(BaseModel):
    content: Optional[List[ChunkChatResponseChoiceLogprobsContent]] = None


class ChunkChatResponseChoice(BaseModel):
    delta: ChunkChatResponseChoiceDelta
    """The message generated by the model"""

    index: int

    finish_reason: Optional[Literal["stop", "length", "content_filter", "tool_calls"]] = None

    logprobs: Optional[ChunkChatResponseChoiceLogprobs] = None


class ChunkChatResponseDocOwner(BaseModel):
    id: str

    role: Literal["user", "agent"]


class ChunkChatResponseDocSnippet(BaseModel):
    content: str

    index: int


class ChunkChatResponseDoc(BaseModel):
    id: str

    owner: ChunkChatResponseDocOwner

    snippets: List[ChunkChatResponseDocSnippet]

    distance: Optional[float] = None

    title: Optional[str] = None


class ChunkChatResponseUsage(BaseModel):
    completion_tokens: Optional[int] = None

    prompt_tokens: Optional[int] = None

    total_tokens: Optional[int] = None


class ChunkChatResponse(BaseModel):
    id: str

    choices: List[ChunkChatResponseChoice]

    created_at: datetime

    docs: Optional[List[ChunkChatResponseDoc]] = None

    jobs: Optional[List[str]] = None

    usage: Optional[ChunkChatResponseUsage] = None
    """Usage statistics for the completion request"""


class MessageChatResponseChoiceSingleChatOutputMessageContentUnionMember2Content(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class MessageChatResponseChoiceSingleChatOutputMessageContentUnionMember2ContentModelImageURL(BaseModel):
    url: str

    detail: Optional[Literal["low", "high", "auto"]] = None


class MessageChatResponseChoiceSingleChatOutputMessageContentUnionMember2ContentModel(BaseModel):
    image_url: MessageChatResponseChoiceSingleChatOutputMessageContentUnionMember2ContentModelImageURL
    """The image URL"""

    type: Optional[Literal["image_url"]] = None


MessageChatResponseChoiceSingleChatOutputMessageContentUnionMember2: TypeAlias = Union[
    MessageChatResponseChoiceSingleChatOutputMessageContentUnionMember2Content,
    MessageChatResponseChoiceSingleChatOutputMessageContentUnionMember2ContentModel,
]


class MessageChatResponseChoiceSingleChatOutputMessageToolCallChosenFunctionCallFunction(BaseModel):
    name: str


class MessageChatResponseChoiceSingleChatOutputMessageToolCallChosenFunctionCall(BaseModel):
    id: str

    function: MessageChatResponseChoiceSingleChatOutputMessageToolCallChosenFunctionCallFunction

    type: Optional[Literal["function"]] = None


class MessageChatResponseChoiceSingleChatOutputMessageToolCallChosenIntegrationCall(BaseModel):
    id: str

    integration: object

    type: Optional[Literal["integration"]] = None


class MessageChatResponseChoiceSingleChatOutputMessageToolCallChosenSystemCall(BaseModel):
    id: str

    system: object

    type: Optional[Literal["system"]] = None


class MessageChatResponseChoiceSingleChatOutputMessageToolCallChosenAPICall(BaseModel):
    id: str

    api_call: object

    type: Optional[Literal["api_call"]] = None


MessageChatResponseChoiceSingleChatOutputMessageToolCall: TypeAlias = Union[
    MessageChatResponseChoiceSingleChatOutputMessageToolCallChosenFunctionCall,
    MessageChatResponseChoiceSingleChatOutputMessageToolCallChosenIntegrationCall,
    MessageChatResponseChoiceSingleChatOutputMessageToolCallChosenSystemCall,
    MessageChatResponseChoiceSingleChatOutputMessageToolCallChosenAPICall,
]


class MessageChatResponseChoiceSingleChatOutputMessage(BaseModel):
    content: Union[str, List[str], List[MessageChatResponseChoiceSingleChatOutputMessageContentUnionMember2]]

    role: Literal["user", "assistant", "system", "function", "function_response", "function_call", "auto"]

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    name: Optional[str] = None

    tool_calls: Optional[List[MessageChatResponseChoiceSingleChatOutputMessageToolCall]] = None


class MessageChatResponseChoiceSingleChatOutputLogprobsContentTopLogprob(BaseModel):
    token: str

    logprob: float

    bytes: Optional[List[int]] = None


class MessageChatResponseChoiceSingleChatOutputLogprobsContent(BaseModel):
    token: str

    logprob: float

    top_logprobs: List[MessageChatResponseChoiceSingleChatOutputLogprobsContentTopLogprob]

    bytes: Optional[List[int]] = None


class MessageChatResponseChoiceSingleChatOutputLogprobs(BaseModel):
    content: Optional[List[MessageChatResponseChoiceSingleChatOutputLogprobsContent]] = None


class MessageChatResponseChoiceSingleChatOutput(BaseModel):
    index: int

    message: MessageChatResponseChoiceSingleChatOutputMessage

    finish_reason: Optional[Literal["stop", "length", "content_filter", "tool_calls"]] = None

    logprobs: Optional[MessageChatResponseChoiceSingleChatOutputLogprobs] = None


class MessageChatResponseChoiceMultipleChatOutputMessageContentUnionMember2Content(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class MessageChatResponseChoiceMultipleChatOutputMessageContentUnionMember2ContentModelImageURL(BaseModel):
    url: str

    detail: Optional[Literal["low", "high", "auto"]] = None


class MessageChatResponseChoiceMultipleChatOutputMessageContentUnionMember2ContentModel(BaseModel):
    image_url: MessageChatResponseChoiceMultipleChatOutputMessageContentUnionMember2ContentModelImageURL
    """The image URL"""

    type: Optional[Literal["image_url"]] = None


MessageChatResponseChoiceMultipleChatOutputMessageContentUnionMember2: TypeAlias = Union[
    MessageChatResponseChoiceMultipleChatOutputMessageContentUnionMember2Content,
    MessageChatResponseChoiceMultipleChatOutputMessageContentUnionMember2ContentModel,
]


class MessageChatResponseChoiceMultipleChatOutputMessageToolCallChosenFunctionCallFunction(BaseModel):
    name: str


class MessageChatResponseChoiceMultipleChatOutputMessageToolCallChosenFunctionCall(BaseModel):
    id: str

    function: MessageChatResponseChoiceMultipleChatOutputMessageToolCallChosenFunctionCallFunction

    type: Optional[Literal["function"]] = None


class MessageChatResponseChoiceMultipleChatOutputMessageToolCallChosenIntegrationCall(BaseModel):
    id: str

    integration: object

    type: Optional[Literal["integration"]] = None


class MessageChatResponseChoiceMultipleChatOutputMessageToolCallChosenSystemCall(BaseModel):
    id: str

    system: object

    type: Optional[Literal["system"]] = None


class MessageChatResponseChoiceMultipleChatOutputMessageToolCallChosenAPICall(BaseModel):
    id: str

    api_call: object

    type: Optional[Literal["api_call"]] = None


MessageChatResponseChoiceMultipleChatOutputMessageToolCall: TypeAlias = Union[
    MessageChatResponseChoiceMultipleChatOutputMessageToolCallChosenFunctionCall,
    MessageChatResponseChoiceMultipleChatOutputMessageToolCallChosenIntegrationCall,
    MessageChatResponseChoiceMultipleChatOutputMessageToolCallChosenSystemCall,
    MessageChatResponseChoiceMultipleChatOutputMessageToolCallChosenAPICall,
]


class MessageChatResponseChoiceMultipleChatOutputMessage(BaseModel):
    content: Union[str, List[str], List[MessageChatResponseChoiceMultipleChatOutputMessageContentUnionMember2]]

    role: Literal["user", "assistant", "system", "function", "function_response", "function_call", "auto"]

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    name: Optional[str] = None

    tool_calls: Optional[List[MessageChatResponseChoiceMultipleChatOutputMessageToolCall]] = None


class MessageChatResponseChoiceMultipleChatOutputLogprobsContentTopLogprob(BaseModel):
    token: str

    logprob: float

    bytes: Optional[List[int]] = None


class MessageChatResponseChoiceMultipleChatOutputLogprobsContent(BaseModel):
    token: str

    logprob: float

    top_logprobs: List[MessageChatResponseChoiceMultipleChatOutputLogprobsContentTopLogprob]

    bytes: Optional[List[int]] = None


class MessageChatResponseChoiceMultipleChatOutputLogprobs(BaseModel):
    content: Optional[List[MessageChatResponseChoiceMultipleChatOutputLogprobsContent]] = None


class MessageChatResponseChoiceMultipleChatOutput(BaseModel):
    index: int

    messages: List[MessageChatResponseChoiceMultipleChatOutputMessage]

    finish_reason: Optional[Literal["stop", "length", "content_filter", "tool_calls"]] = None

    logprobs: Optional[MessageChatResponseChoiceMultipleChatOutputLogprobs] = None


MessageChatResponseChoice: TypeAlias = Union[
    MessageChatResponseChoiceSingleChatOutput, MessageChatResponseChoiceMultipleChatOutput
]


class MessageChatResponseDocOwner(BaseModel):
    id: str

    role: Literal["user", "agent"]


class MessageChatResponseDocSnippet(BaseModel):
    content: str

    index: int


class MessageChatResponseDoc(BaseModel):
    id: str

    owner: MessageChatResponseDocOwner

    snippets: List[MessageChatResponseDocSnippet]

    distance: Optional[float] = None

    title: Optional[str] = None


class MessageChatResponseUsage(BaseModel):
    completion_tokens: Optional[int] = None

    prompt_tokens: Optional[int] = None

    total_tokens: Optional[int] = None


class MessageChatResponse(BaseModel):
    id: str

    choices: List[MessageChatResponseChoice]

    created_at: datetime

    docs: Optional[List[MessageChatResponseDoc]] = None

    jobs: Optional[List[str]] = None

    usage: Optional[MessageChatResponseUsage] = None
    """Usage statistics for the completion request"""


ChatCreateResponse: TypeAlias = Union[ChunkChatResponse, MessageChatResponse]
