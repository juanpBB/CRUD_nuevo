from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
import database as dbase 
from product import Producto  