from pydantic import BaseModel, PydanticValueError, ValidationError, validator

class NotABarError(PydanticValueError):
    code = 'not_a_bar'
    msg_template = 'value is not "bar", got "{wrong_value}"'

class Model(BaseModel):
    foo: str

    @validator('foo')
    def must_be_bar(cls, v):
        if v != 'bar':
            raise NotABarError(wrong_value=v)
        return v

try:
    Model(foo='ber')
except ValidationError as e:
    print(e.json())
"""
[
  {
    "loc": ["foo"],
    "msg": "value is not \"bar\", got \"ber\"",
    "type": "value_error.not_a_bar",
    "ctx": {
      "wrong_value": "ber"
    }
  }
]
"""
