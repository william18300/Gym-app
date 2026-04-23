from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

app = Flask(__name__)

app.config[]