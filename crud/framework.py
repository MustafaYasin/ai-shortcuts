from sqlalchemy.orm import Session
from orm.framework_orm import FrameworkDB
from models.framework import Framework, FrameworkUpdate


def get_framework(db: Session, framework_id: int=None):
    if framework_id is None:
        return db.query(FrameworkDB).all()
    return db.query(FrameworkDB).filter(FrameworkDB.id == framework_id).first()

def create_framework(db: Session, framework: Framework):
    db_framework = FrameworkDB(**framework.dict())
    db.add(db_framework)
    db.commit()
    db.refresh(db_framework)
    return db_framework

# Update a framework in the database with new data
def update_framework_by_id(db: Session, framework_id: int, framework_data: FrameworkUpdate):
    db_framework = db.query(FrameworkDB).filter(FrameworkDB.id == framework_id).first()
    if db_framework is None:
        return None  

    # Update model instance with new data
    for key, value in framework_data.dict().items():
        setattr(db_framework, key, value)

    db.commit()
    db.refresh(db_framework)
    return db_framework

# Delete a framework from the database
def remove_framework(db: Session, framework_id: int):
    db_framework = db.query(FrameworkDB).filter(FrameworkDB.id == framework_id).first()
    if db_framework is None:
        return None  # Or handle as needed, e.g., raise an exception
    print(db_framework)
    db.delete(db_framework)
    db.commit()
    return db_framework
