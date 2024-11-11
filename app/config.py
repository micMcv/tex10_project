import os

class Config:
    #SECRET_KEY = "texsib"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:texsib@localhost:3306/tex10_goals"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
