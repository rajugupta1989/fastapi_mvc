# app/controllers/controller.py
from fastapi import APIRouter, HTTPException
from app.models.models import RequestModel, ResponseModel
from app.utils.utils import process_payload
from app.logs.logger import logger
from datetime import datetime

router = APIRouter()

@router.post("/process", response_model=ResponseModel)
async def process_data(request: RequestModel):
    start_time = datetime.utcnow()
    logger.debug(f"Received request: {request}")
    
    try:
        result = process_payload(request.payload)
    except Exception as e:
        logger.error(f"Error processing payload: {e}")
        raise HTTPException(status_code=400, detail=str(e))

    end_time = datetime.utcnow()
    response = ResponseModel(
        batchid=request.batchid,
        response=result,
        status="complete",
        started_at=start_time,
        completed_at=end_time
    )
    logger.debug(f"Response: {response}")
    return response
