from fastapi import APIRouter
router = APIRouter(prefix="/api", tags=["prices"])

@router.get("/prices")
async def search_prices(product: str, retailer: str = None):
    return {"success": True, "query": product, "results": []}
