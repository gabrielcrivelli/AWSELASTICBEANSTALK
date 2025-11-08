# Deployment Guide

## GitHub
1. git clone https://github.com/tu-usuario/retail-bi-scraper.git
2. Copiar archivos aquí
3. git add .
4. git commit -m "Initial commit"
5. git push origin main

## AWS
aws configure
eb init -p docker retail-bi-scraper --region us-east-1
eb create retail-bi-free --instance-type t2.micro --single
eb logs --stream
eb open
undefined