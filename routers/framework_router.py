from fastapi import APIRouter, status
from models.framework import Framework, FrameworkUpdate
from crud.framework import get_framework, create_framework, remove_framework, update_framework_by_id
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from orm.framework_orm import SessionLocal
from typing import List

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/frameworks", response_model=List[Framework])
def get_all_frameworks(db: Session = Depends(get_db)):
    db_frameworks = get_framework(db)
    if not db_frameworks:
        raise HTTPException(status_code=404, detail="No Framework is found")
    return db_frameworks 

@router.post("/frameworks", response_model=Framework)
def create_frameworks(framework: Framework, db: Session = Depends(get_db)):
    response = create_framework(db=db, framework=framework)
    if response:
        return {'msg': 'Framework created successfully'}, 201
    else:
        raise HTTPException(status_code=400, detail="Could not create framework")

@router.get("/frameworks/{framework_id}", response_model=Framework)
def read_framework(framework_id: int, db: Session = Depends(get_db)):
    db_framework = get_framework(db, framework_id=framework_id)
    if db_framework is None:
        raise HTTPException(status_code=404, detail="Framework not found")
    return db_framework

@router.delete("/frameworks/{framework_id}", status_code=status.HTTP_200_OK)
def delete_framework(framework_id: int, db: Session = Depends(get_db)):
    db_framework = remove_framework(db, framework_id=framework_id)
    if db_framework:
        return {'msg': 'Framework deleted successfully'}
    else:
        raise HTTPException(status_code=404, detail="Framework not found")

@router.put("/frameworks/{framework_id}", response_model=Framework, response_model_exclude_unset=True, status_code=status.HTTP_200_OK)
def update_framework(framework_id: int, framework_update: FrameworkUpdate, db: Session = Depends(get_db)):
    db_framework = update_framework_by_id(db, framework_id=framework_id, framework_data=framework_update)
    if db_framework:
        return db_framework
    else:
        raise HTTPException(status_code=404, detail="Framework not found")
