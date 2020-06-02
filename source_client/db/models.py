from typing import Dict, Union, List
from datetime import timedelta, datetime

from sqlalchemy import Column, Integer, Float, DateTime, TEXT
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.ext.declarative import declarative_base

from . import session


Base = declarative_base()


def dt2str(dt: datetime):
    return dt.strftime('%Y-%m-%d %H:%M:%S')


def _to_dict(obj) -> Dict[str, Union[str, float]]:
    result = {
        'record_time': dt2str(obj.rtime),
        'CH01': obj.CH01,
        'CH02': obj.CH02,
        'CH03': obj.CH03,
        'CH04': obj.CH04
        }
    return result


class RunTime(Base):
    __tablename__ = 'run_time'
    open_time = Column('OPEN', DateTime, primary_key=True)
    close_time = Column('CLOSE', DateTime)

    def _to_dict(self):
        return {
            'open_time': dt2str(self.open_time),
            'close_time': dt2str(self.close_time)
            }


class Record(Base):
    __tablename__ = 'record'
    rtime = Column('record_time', DateTime, primary_key=True)
    CH01 = Column('CH01', Float)
    CH02 = Column('CH02', Float)
    CH03 = Column('CH03', Float)
    CH04 = Column('CH04', Float)

    def to_dict(self) -> Dict[str, Union[str, float]]:
        return _to_dict(self)


class Alarm(Base):
    __tablename__ = 'alarm'
    rtime = Column('record_time', DateTime, primary_key=True)
    CH01 = Column('CH01', Float)
    CH02 = Column('CH02', Float)
    CH03 = Column('CH03', Float)
    CH04 = Column('CH04', Float)

    def to_dict(self) -> Dict[str, Union[str, float]]:
        return _to_dict(self)
