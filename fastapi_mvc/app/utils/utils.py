# app/utils/utils.py
from multiprocessing import Pool
from typing import List
from app.logs.logger import logger

def add_lists(lists: List[List[int]]) -> List[int]:
    return [sum(lst) for lst in lists]

def process_payload(payload: List[List[int]]) -> List[int]:
    logger.debug(f"Processing payload: {payload}")
    try:
        with Pool() as pool:
            results = pool.map(sum, payload)
        logger.debug(f"Processing results: {results}")
        return results
    except Exception as e:
        logger.error(f"Error in multiprocessing pool: {e}")
        raise
