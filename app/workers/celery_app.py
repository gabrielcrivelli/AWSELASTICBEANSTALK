from celery import Celery
import os
redis_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379/1")
celery_app = Celery("retail_bi", broker=redis_url, backend=redis_url)
celery_app.conf.update(task_serializer="json", accept_content=["json"], result_serializer="json")
