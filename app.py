from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
import os 
from src.helper import download_embeddings
from pinecone import Pinecone 
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain_groq import ChatGroq
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain 
from langchain_core.prompts import ChatPromptTemplate
from src.prompt import *
import os 