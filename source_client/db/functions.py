from typing import Dict, Union, List
from datetime import timedelta, datetime
from sqlalchemy.orm.exc import NoResultFound

from . import session
from .models import Record, Alarm, RunTime


def get_latest_record() -> Dict[str, Union[str, float]]:
    try:
        obj = session.query(Record).order_by(Record.rtime.desc()).first()
        result = obj.to_dict()
    except NoResultFound:
        result = dict()
    except Exception:
        raise
    finally:
        session.rollback()
    return result


def get_record_between(sdt: datetime, edt: datetime = None) -> List[Dict[str, Union[str, float]]]:
    try:
        if edt is None:
            edt = datetime.now()
        objs = session.query(Record).filter(Record.rtime.between(sdt, edt)).all()
        result = [obj.to_dict() for obj in objs]
    except Exception:
        raise
    finally:
        session.rollback()
    return result
