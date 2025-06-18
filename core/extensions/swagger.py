# from flasgger import Swagger
# from flask import Flask

# from application.docs.template import swagger_config, swagger_template


# class SwaggerExtension:
#     _instance = None
#     swagger: Swagger = None

#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#             cls._instance.swagger = Swagger()
#         return cls._instance

#     def init_app(self, app: Flask) -> None:
#         self.swagger.init_app(app)
#         settings = {
#             "template": swagger_template,
#             "config": swagger_config,
#             "parse": True,
#         }
#         for attr, key in settings.items():
#             setattr(self.swagger, attr, key)
