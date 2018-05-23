# coding: utf-8

from . import db


class Metadata(db.Model):
    __tablename__ = 'metadata'

    id = db.Column(db.BigInteger, primary_key=True)
    s_no = db.Column(db.String(255))
    service = db.Column(db.String(255))
    s_map_type = db.Column(db.String(255))
    s_source_type = db.Column(db.String(255))
    s_target_type = db.Column(db.String(255))
    s_map_len = db.Column(db.String(255))
    s_alloc_date = db.Column(db.String(255))
    s_cancel_date = db.Column(db.String(255))
    s_provider = db.Column(db.String(255))
    m_isli = db.Column(db.String(255))
    m_source_name = db.Column(db.String(255))
    m_source_name_type = db.Column(db.String(255))
    m_source_type = db.Column(db.String(255))
    m_source_flag = db.Column(db.String(255))
    m_source_part = db.Column(db.String(255))
    m_all_target_name = db.Column(db.String(255))
    m_target_name_type = db.Column(db.String(255))
    m_all_flag = db.Column(db.String(255))
    m_target_type = db.Column(db.String(255))
    m_target_part = db.Column(db.String(255))
    m_alloc_date = db.Column(db.String(255))
    m_cancel_date = db.Column(db.String(255))
    m_cancel_reason = db.Column(db.String(255))
    m_registrant = db.Column(db.String(255))
