from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient
import requests
import pandas as pd
import numpy as np
from datetime import date
from datetime import timedelta

def displayText():
    print( "Recommend Function!")