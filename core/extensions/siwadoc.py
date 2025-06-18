# from flask import Flask
# from flask_siwadoc import SiwaDoc


# class SiwaDocExtension:
#     # 设置单例模式
#     _instance = None
#     siwadoc: SiwaDoc

#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#             cls._instance.siwadoc = SiwaDoc()
#         return cls._instance

#     def init_app(self, app: Flask):
#         self.siwadoc.init_app(app)
#         settings = {
#             "title": app.config["TITLE"],
#             "description": app.config["DESCRIPTION"],
#             "ui": app.config["SIWA_UI"],
#             "version": app.config["VERSION"],
#         }
#         for attr, key in settings.items():
#             setattr(self.siwadoc, attr, key)
