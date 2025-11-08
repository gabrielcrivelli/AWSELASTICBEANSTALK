# Retail BI Scraper
Comparador de precios en retailers argentinos

## Quick Start
docker-compose -f docker/docker-compose.yml up
## Deploy AWS
eb init -p docker retail-bi-scraper --region us-east-1
eb create retail-bi-free --instance-type t2.micro --single
eb open

## URLs
- / → Dashboard
- /search → Búsqueda
- /api/health → Health check
- /api/docs → Swagger API