# Code generated by Lark OpenAPI.

from typing import Optional

from requests_toolbelt import MultipartEncoder

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8, CONTENT_TYPE
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from lark_oapi.core.utils import Files
from ..model.recognize_train_invoice_request import RecognizeTrainInvoiceRequest
from ..model.recognize_train_invoice_response import RecognizeTrainInvoiceResponse


class TrainInvoice(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def recognize(self, request: RecognizeTrainInvoiceRequest,
                  option: Optional[RequestOption] = None) -> RecognizeTrainInvoiceResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 添加 content-type
        if request.body is not None:
            form_data = MultipartEncoder(Files.parse_form_data(request.body))
            request.body = form_data
            option.headers[CONTENT_TYPE] = form_data.content_type

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: RecognizeTrainInvoiceResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                 RecognizeTrainInvoiceResponse)
        response.raw = resp

        return response
