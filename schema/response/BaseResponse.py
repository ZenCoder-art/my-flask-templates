from pydantic import BaseModel, Field


class SuccessResponse(BaseModel):
    code: int = Field(200, description="响应状态码")
    message: str = Field("ok", description="响应信息")


class Unauthorized(BaseModel):
    code: int = Field(401, description="响应状态码")
    message: str = Field(
        default="身份未验证", description="请求未包含有效的身份验证信息"
    )


class Forbidden(BaseModel):
    code: int = Field(403, description="响应状态码")
    message: str = Field(default="无权限访问", description="您没有访问此资源的权限")


class NotFound(BaseModel):
    code: int = Field(404, description="响应状态码")
    message: str = Field(
        default="请求的路由未找到", description="请求的路由不存在,请尝试其他路由"
    )


class ValidationError(BaseModel):
    code: int = Field(422, description="响应状态码")
    message: str = Field(
        default="请求参数验证失败", description="请求参数不符合预期,请检查参数是否正确"
    )


class TooManyRequests(BaseModel):
    code: int = Field(429, description="响应状态码")
    message: str = Field(default="请求过于频繁", description="请稍后再试")


class ServerError(BaseModel):
    code: int = Field(500, description="响应状态码")
    message: str = Field(default="服务器内部错误", description="请稍后再试或联系管理员")
