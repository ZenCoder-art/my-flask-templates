from typing import Any, Dict, List, Union

from pydantic import BaseModel, Field


class SuccessSchema(BaseModel):
    code: int = Field(..., description="状态码，通常为200表示成功", example=200)
    message: str = Field(..., description="响应信息", example="OK")
    data: Union[Dict[str, Any], List[Any]] = Field(
        ...,
        description="返回的数据，字典或列表",
        example=dict(),
    )
    success_type: str = Field(..., description="成功类型描述", example="success")
