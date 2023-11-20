# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .recognize_id_card_request_body import RecognizeIdCardRequestBody


class RecognizeIdCardRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[RecognizeIdCardRequestBody] = None

    @staticmethod
    def builder() -> "RecognizeIdCardRequestBuilder":
        return RecognizeIdCardRequestBuilder()


class RecognizeIdCardRequestBuilder(object):

    def __init__(self) -> None:
        recognize_id_card_request = RecognizeIdCardRequest()
        recognize_id_card_request.http_method = HttpMethod.POST
        recognize_id_card_request.uri = "/open-apis/document_ai/v1/id_card/recognize"
        recognize_id_card_request.token_types = {AccessTokenType.TENANT}
        self._recognize_id_card_request: RecognizeIdCardRequest = recognize_id_card_request

    def request_body(self, request_body: RecognizeIdCardRequestBody) -> "RecognizeIdCardRequestBuilder":
        self._recognize_id_card_request.request_body = request_body
        self._recognize_id_card_request.body = request_body
        return self

    def build(self) -> RecognizeIdCardRequest:
        return self._recognize_id_card_request
