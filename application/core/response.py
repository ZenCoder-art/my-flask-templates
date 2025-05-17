from typing import Dict, Optional

from flask import jsonify, request


class ResponseBuilder:
    response = {
        200: {"type": "OK", "message": "资源请求成功"},
        201: {"type": "CREATED", "message": "资源创建成功"},
        204: {"type": "NO_CONTENT", "message": "资源删除成功"},
        400: {"type": "BAD_REQUEST", "message": "请求参数无效"},
        401: {"type": "UNAUTHORIZED", "message": "身份认证失败"},
        403: {"type": "FORBIDDEN", "message": "访问被拒绝"},
        404: {"type": "NOT_FOUND", "message": "资源不存在"},
        500: {"type": "INTERNAL_ERROR", "message": "服务器内部错误"},
    }

    @staticmethod
    def success(
        data: dict | list = None,
        message: str = "Success",
        status_code: int = 200,
        success_type: str = "OK",
    ) -> tuple:
        """构建标准成功响应"""
        response = {
            "code": status_code,
            "message": message,
            "data": data,
            "success_type": success_type,
        }
        if hasattr(request, "request_id"):
            response["request_id"] = request.request_id
        return jsonify(response), status_code

    @staticmethod
    def error(
        code: int,
        message: str,
        error_type: str = None,
        details: Optional[Dict] | str | list = None,
    ) -> tuple:
        """构建标准错误响应"""
        response = {
            "code": code,
            "error_type": error_type,
            "message": message,
            "details": details,
        }
        if hasattr(request, "request_id"):
            response["request_id"] = request.request_id
        return jsonify(response), code
