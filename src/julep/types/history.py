# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "History",
    "Entry",
    "EntryContent",
    "EntryContentUnionMember0",
    "EntryContentUnionMember0Content",
    "EntryContentUnionMember0ContentModel",
    "EntryContentUnionMember0ContentModelImageURL",
    "EntryContentTool",
    "EntryContentToolFunction",
    "EntryContentChosenFunctionCall",
    "EntryContentChosenFunctionCallFunction",
    "EntryContentChosenIntegrationCall",
    "EntryContentChosenSystemCall",
    "EntryContentChosenAPICall",
    "EntryContentToolResponse",
    "EntryContentUnionMember8",
    "EntryContentUnionMember8UnionMember0",
    "EntryContentUnionMember8UnionMember0Content",
    "EntryContentUnionMember8UnionMember0ContentModel",
    "EntryContentUnionMember8UnionMember0ContentModelImageURL",
    "EntryContentUnionMember8Tool",
    "EntryContentUnionMember8ToolFunction",
    "EntryContentUnionMember8ChosenFunctionCall",
    "EntryContentUnionMember8ChosenFunctionCallFunction",
    "EntryContentUnionMember8ChosenIntegrationCall",
    "EntryContentUnionMember8ChosenSystemCall",
    "EntryContentUnionMember8ChosenAPICall",
    "EntryContentUnionMember8ToolResponse",
    "Relation",
]


class EntryContentUnionMember0Content(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class EntryContentUnionMember0ContentModelImageURL(BaseModel):
    url: str

    detail: Optional[Literal["low", "high", "auto"]] = None


class EntryContentUnionMember0ContentModel(BaseModel):
    image_url: EntryContentUnionMember0ContentModelImageURL
    """The image URL"""

    type: Optional[Literal["image_url"]] = None


EntryContentUnionMember0: TypeAlias = Union[EntryContentUnionMember0Content, EntryContentUnionMember0ContentModel]


class EntryContentToolFunction(BaseModel):
    description: Optional[str] = None

    name: Optional[object] = None

    parameters: Optional[object] = None


class EntryContentTool(BaseModel):
    id: str

    created_at: datetime

    function: EntryContentToolFunction
    """Function definition"""

    name: str

    updated_at: datetime

    api_call: Optional[object] = None

    integration: Optional[object] = None

    system: Optional[object] = None

    type: Optional[Literal["function", "integration", "system", "api_call"]] = None


class EntryContentChosenFunctionCallFunction(BaseModel):
    name: str


class EntryContentChosenFunctionCall(BaseModel):
    id: str

    function: EntryContentChosenFunctionCallFunction

    type: Optional[Literal["function"]] = None


class EntryContentChosenIntegrationCall(BaseModel):
    id: str

    integration: object

    type: Optional[Literal["integration"]] = None


class EntryContentChosenSystemCall(BaseModel):
    id: str

    system: object

    type: Optional[Literal["system"]] = None


class EntryContentChosenAPICall(BaseModel):
    id: str

    api_call: object

    type: Optional[Literal["api_call"]] = None


class EntryContentToolResponse(BaseModel):
    id: str

    output: object


class EntryContentUnionMember8UnionMember0Content(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class EntryContentUnionMember8UnionMember0ContentModelImageURL(BaseModel):
    url: str

    detail: Optional[Literal["low", "high", "auto"]] = None


class EntryContentUnionMember8UnionMember0ContentModel(BaseModel):
    image_url: EntryContentUnionMember8UnionMember0ContentModelImageURL
    """The image URL"""

    type: Optional[Literal["image_url"]] = None


EntryContentUnionMember8UnionMember0: TypeAlias = Union[
    EntryContentUnionMember8UnionMember0Content, EntryContentUnionMember8UnionMember0ContentModel
]


class EntryContentUnionMember8ToolFunction(BaseModel):
    description: Optional[str] = None

    name: Optional[object] = None

    parameters: Optional[object] = None


class EntryContentUnionMember8Tool(BaseModel):
    id: str

    created_at: datetime

    function: EntryContentUnionMember8ToolFunction
    """Function definition"""

    name: str

    updated_at: datetime

    api_call: Optional[object] = None

    integration: Optional[object] = None

    system: Optional[object] = None

    type: Optional[Literal["function", "integration", "system", "api_call"]] = None


class EntryContentUnionMember8ChosenFunctionCallFunction(BaseModel):
    name: str


class EntryContentUnionMember8ChosenFunctionCall(BaseModel):
    id: str

    function: EntryContentUnionMember8ChosenFunctionCallFunction

    type: Optional[Literal["function"]] = None


class EntryContentUnionMember8ChosenIntegrationCall(BaseModel):
    id: str

    integration: object

    type: Optional[Literal["integration"]] = None


class EntryContentUnionMember8ChosenSystemCall(BaseModel):
    id: str

    system: object

    type: Optional[Literal["system"]] = None


class EntryContentUnionMember8ChosenAPICall(BaseModel):
    id: str

    api_call: object

    type: Optional[Literal["api_call"]] = None


class EntryContentUnionMember8ToolResponse(BaseModel):
    id: str

    output: object


EntryContentUnionMember8: TypeAlias = Union[
    List[EntryContentUnionMember8UnionMember0],
    EntryContentUnionMember8Tool,
    EntryContentUnionMember8ChosenFunctionCall,
    EntryContentUnionMember8ChosenIntegrationCall,
    EntryContentUnionMember8ChosenSystemCall,
    EntryContentUnionMember8ChosenAPICall,
    str,
    EntryContentUnionMember8ToolResponse,
]

EntryContent: TypeAlias = Union[
    List[EntryContentUnionMember0],
    EntryContentTool,
    EntryContentChosenFunctionCall,
    EntryContentChosenIntegrationCall,
    EntryContentChosenSystemCall,
    EntryContentChosenAPICall,
    str,
    EntryContentToolResponse,
    List[EntryContentUnionMember8],
]


class Entry(BaseModel):
    id: str

    content: EntryContent

    created_at: datetime

    role: Literal["user", "assistant", "system", "function", "function_response", "function_call", "auto"]

    source: Literal["api_request", "api_response", "tool_response", "internal", "summarizer", "meta"]

    timestamp: float

    token_count: int

    tokenizer: str

    name: Optional[str] = None


class Relation(BaseModel):
    head: str

    relation: str

    tail: str


class History(BaseModel):
    created_at: datetime

    entries: List[Entry]

    relations: List[Relation]

    session_id: str
