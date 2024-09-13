# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "Message",
    "ContentUnionMember2",
    "ContentUnionMember2Content",
    "ContentUnionMember2ContentModel",
    "ContentUnionMember2ContentModelImageURL",
]


class ContentUnionMember2Content(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class ContentUnionMember2ContentModelImageURL(BaseModel):
    url: str

    detail: Optional[Literal["low", "high", "auto"]] = None


class ContentUnionMember2ContentModel(BaseModel):
    image_url: ContentUnionMember2ContentModelImageURL
    """The image URL"""

    type: Optional[Literal["image_url"]] = None


ContentUnionMember2: TypeAlias = Union[ContentUnionMember2Content, ContentUnionMember2ContentModel]


class Message(BaseModel):
    content: Union[str, List[str], List[ContentUnionMember2]]

    role: Literal["user", "assistant", "system", "function", "function_response", "function_call", "auto"]

    continue_: Optional[bool] = FieldInfo(alias="continue", default=None)

    name: Optional[str] = None
