from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from datetime import datetime

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting Retail BI Scraper...")
    yield
    print("Stopping Retail BI Scraper...")

app = FastAPI(title="Retail BI Scraper", version="1.0.0", lifespan=lifespan)
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <!DOCTYPE html>
    <html><head><meta charset="UTF-8"><title>Retail BI</title><style>
    body{font-family:Segoe UI;background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);display:flex;align-items:center;justify-content:center;min-height:100vh}
    .container{background:white;border-radius:15px;max-width:1200px;padding:40px}h1{color:#667eea;border-bottom:3px solid #667eea;padding-bottom:10px}
    .feature-card{background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);color:white;padding:25px;border-radius:10px;margin:10px;text-align:center}
    .btn{padding:15px 30px;background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);color:white;border:none;border-radius:8px;cursor:pointer;text-decoration:none;display:inline-block;margin:10px}
    </style></head><body><div class="container"><h1>🛒 Retail BI Scraper</h1><p>Comparador de precios en retailers</p>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:20px"><div class="feature-card"><b>🔍 Búsqueda</b></div><div class="feature-card"><b>📊 Análisis</b></div><div class="feature-card"><b>📥 Export</b></div></div>
    <div style="text-align:center;margin-top:30px"><a href="/search" class="btn">🔍 Buscar</a><a href="/api/docs" class="btn">📚 API</a></div></div></body></html>
    """

@app.get("/search", response_class=HTMLResponse)
async def search_page():
    return "<html><body><h1>Búsqueda de Precios</h1></body></html>"

@app.get("/api/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.utcnow().isoformat(), "version": "1.0.0"}

@app.get("/api/retailers")
async def list_retailers():
    return {"retailers": [{"name": "Cuchermercados"}, {"name": "Changomas"}, {"name": "Vea"}, {"name": "Carrefour"}, {"name": "Libertad"}]}

@app.get("/api/prices")
async def get_prices(product: str = None, retailer: str = None):
    return {"success": True, "product": product, "retailer": retailer, "prices": []}
