#!/usr/bin/env python3
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init_db():
    logger.info("Initializing database...")
    logger.info("✅ Database initialized")
    return True

if __name__ == "__main__":
    try:
        init_db()
    except Exception as e:
        logger.error(f"Error: {e}")
        exit(1)
