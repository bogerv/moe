# coding:utf-8
from . import main
from flask import render_template, request


@main.route('/', methods=['GET', ])
def form():
    return render_template('form.html')


@main.route('/upload', methods=['POST', ])
def submit_isli():
    if request.method == 'POST':
        s_no = request.form['s_no']
        service = request.form['service']
        s_map_type = request.form['s_map_type']
        s_source_type = request.form['s_source_type']
        s_target_type = request.form['s_target_type']
        s_map_len = request.form['s_map_len']
        s_alloc_date = request.form['s_alloc_date']
        s_cancel_date = request.form['s_cancel_date']
        s_provider = request.form['s_provider']
        m_isli = request.form['m_isli']
        m_source_name = request.form['m_source_name']
        m_source_name_type = request.form['m_source_name_type']
        m_source_type = request.form['m_source_type']
        m_source_flag = request.form['m_source_flag']
        m_source_part = request.form['m_source_part']
        m_all_target_name = request.form['m_all_target_name']
        m_target_name_type = request.form['m_target_name_type']
        m_all_flag = request.form['m_all_flag']
        m_target_type = request.form['m_target_type']
        if len(request.files) > 0:
            m_target_part = request.files['m_target_part']
        m_alloc_date = request.form['m_alloc_date']
        m_cancel_date = request.form['m_cancel_date']
        m_cancel_reason = request.form['m_cancel_reason']
        m_registrant = request.form['m_registrant']

    return render_template('form.html')

