import os
from PyPDF2 import PdfReader
import locale
from datetime import datetime
import psycopg2
import time
import shutil
from groq import Groq
import openpyxl
import sys
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(r"C:\rpa\Python")
from Classes.ZimbraMailer.ZimbraMailer.Zimbra import ZimbraMailer


def envia_email(assunto, mensagem, destinatarios, anexo=None):
    pass # Logica de negocio removida por seguranca corporativa



def executa_groq(caminho_arquivo, paginas_por_bloco=2):
    pass # Logica de negocio removida por seguranca corporativa



def processa_arquivos():
    pass # Logica de negocio removida por seguranca corporativa

def diretorio_json():
    pass # Logica de negocio removida por seguranca corporativa

def solicita_tabela_base():
    pass # Logica de negocio removida por seguranca corporativa



def movimenta_arquivos_backup():
    pass # Logica de negocio removida por seguranca corporativa

        

def executa_insert_pg(sql):
    pass # Logica de negocio removida por seguranca corporativa



def adicionar_dados_no_excel(arquivo_excel, dados):
    pass # Logica de negocio removida por seguranca corporativa



def buscar_arquivos():
    pass # Logica de negocio removida por seguranca corporativa
