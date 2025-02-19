from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VerifyTransactionRequest(_message.Message):
    __slots__ = ("user", "credit_card", "billing_address", "items", "gift_wrapping", "terms_accepted")
    USER_FIELD_NUMBER: _ClassVar[int]
    CREDIT_CARD_FIELD_NUMBER: _ClassVar[int]
    BILLING_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    GIFT_WRAPPING_FIELD_NUMBER: _ClassVar[int]
    TERMS_ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    user: UserInfo
    credit_card: CreditCardInfo
    billing_address: BillingAddress
    items: _containers.RepeatedCompositeFieldContainer[Item]
    gift_wrapping: bool
    terms_accepted: bool
    def __init__(self, user: _Optional[_Union[UserInfo, _Mapping]] = ..., credit_card: _Optional[_Union[CreditCardInfo, _Mapping]] = ..., billing_address: _Optional[_Union[BillingAddress, _Mapping]] = ..., items: _Optional[_Iterable[_Union[Item, _Mapping]]] = ..., gift_wrapping: bool = ..., terms_accepted: bool = ...) -> None: ...

class UserInfo(_message.Message):
    __slots__ = ("name", "contact")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONTACT_FIELD_NUMBER: _ClassVar[int]
    name: str
    contact: str
    def __init__(self, name: _Optional[str] = ..., contact: _Optional[str] = ...) -> None: ...

class CreditCardInfo(_message.Message):
    __slots__ = ("card_number", "expiration_date", "cvv")
    CARD_NUMBER_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    CVV_FIELD_NUMBER: _ClassVar[int]
    card_number: str
    expiration_date: str
    cvv: str
    def __init__(self, card_number: _Optional[str] = ..., expiration_date: _Optional[str] = ..., cvv: _Optional[str] = ...) -> None: ...

class BillingAddress(_message.Message):
    __slots__ = ("street", "city", "state", "zip", "country")
    STREET_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ZIP_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    street: str
    city: str
    state: str
    zip: str
    country: str
    def __init__(self, street: _Optional[str] = ..., city: _Optional[str] = ..., state: _Optional[str] = ..., zip: _Optional[str] = ..., country: _Optional[str] = ...) -> None: ...

class Item(_message.Message):
    __slots__ = ("name", "quantity")
    NAME_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    name: str
    quantity: int
    def __init__(self, name: _Optional[str] = ..., quantity: _Optional[int] = ...) -> None: ...

class VerifyTransactionResponse(_message.Message):
    __slots__ = ("is_verified",)
    IS_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    is_verified: bool
    def __init__(self, is_verified: bool = ...) -> None: ...
