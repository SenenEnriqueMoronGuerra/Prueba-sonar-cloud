import requests
import json
import os
import boto3
import sys
from flask import Flask, request
from . import sonarcloud

url = "https://172.26.178.20:3443/api/v1/"

def get_headers():
	headers = {
	'Accept': 'application/json, text/plain, */*',
	'Connection': 'keep-alive',
	'Host': '172.26.178.20:3443',
	'Content-Type': 'application/json;charset=UTF-8',
	'Origin': 'https://172.26.178.20:3443',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'en-US,en;q=0.9',
	'Referer': 'https://172.26.178.20:3443/',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
	} 
	return headers