from app.workers.celery_app import celery_app
@celery_app.task(bind=True)
def scrape_task(self, product: str, retailer: str):
    return {"product": product, "retailer": retailer, "status": "completed"}
