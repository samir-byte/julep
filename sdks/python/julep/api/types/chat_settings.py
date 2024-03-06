# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .chat_settings_preset import ChatSettingsPreset
from .chat_settings_response_format import ChatSettingsResponseFormat
from .chat_settings_stop import ChatSettingsStop

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ChatSettings(pydantic.BaseModel):
    frequency_penalty: typing.Optional[float] = pydantic.Field(
        description="(OpenAI-like) Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim."
    )
    length_penalty: typing.Optional[float] = pydantic.Field(
        description="(Huggingface-like) Number between 0 and 2.0. 1.0 is neutral and values larger than that penalize number of tokens generated."
    )
    logit_bias: typing.Optional[
        typing.Dict[str, typing.Optional[int]]
    ] = pydantic.Field(
        description=(
            "Modify the likelihood of specified tokens appearing in the completion.\n"
            "\n"
            "Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token.\n"
        )
    )
    max_tokens: typing.Optional[int] = pydantic.Field(
        description=(
            "The maximum number of tokens to generate in the chat completion.\n"
            "\n"
            "The total length of input tokens and generated tokens is limited by the model's context length.\n"
        )
    )
    presence_penalty: typing.Optional[float] = pydantic.Field(
        description="(OpenAI-like) Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim."
    )
    repetition_penalty: typing.Optional[float] = pydantic.Field(
        description="(Huggingface-like) Number between 0 and 2.0. 1.0 is neutral and values larger than that penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim."
    )
    response_format: typing.Optional[ChatSettingsResponseFormat] = pydantic.Field(
        description=(
            "An object specifying the format that the model must output.\n"
            "\n"
            'Setting to `{ "type": "json_object" }` enables JSON mode, which guarantees the message the model generates is valid JSON.\n'
            "\n"
            '**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.\n'
        )
    )
    seed: typing.Optional[int] = pydantic.Field(
        description=(
            "This feature is in Beta.\n"
            "If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same `seed` and parameters should return the same result.\n"
            "Determinism is not guaranteed, and you should refer to the `system_fingerprint` response parameter to monitor changes in the backend.\n"
        )
    )
    stop: typing.Optional[ChatSettingsStop] = pydantic.Field(
        description="Up to 4 sequences where the API will stop generating further tokens."
    )
    stream: typing.Optional[bool] = pydantic.Field(
        description="If set, partial message deltas will be sent, like in ChatGPT. Tokens will be sent as data-only [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format) as they become available, with the stream terminated by a `data: [DONE]` message. [Example Python code](https://cookbook.openai.com/examples/how_to_stream_completions)."
    )
    temperature: typing.Optional[float] = pydantic.Field(
        description="What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic."
    )
    top_p: typing.Optional[float] = pydantic.Field(
        description="Defaults to 1 An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered. We generally recommend altering this or temperature but not both."
    )
    min_p: typing.Optional[float] = pydantic.Field(
        description="Minimum probability compared to leading token to be considered"
    )
    preset: typing.Optional[ChatSettingsPreset] = pydantic.Field(
        description="Generation preset name (one of: problem_solving, conversational, fun, prose, creative, business, deterministic, code, multilingual)"
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
