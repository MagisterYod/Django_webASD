import oracledb


oracledb.init_oracle_client(lib_dir='C:\\app\product\instantclient_12_2')
connection = oracledb.connect(user='ORACLEASD', password='OracleASD', dsn='piteservice')
cursor = connection.cursor()


def sql_get_po6(date):
    cur_get_po6 = cursor.var(oracledb.CURSOR)
    cursor.callproc('ZSU.EXPORTFULLREPORT.GET_PO6', [date, cur_get_po6])
    return cur_get_po6


def sql_insert_or_update_budget_result_month(p_date):
    cursor.callproc('ZSU.INSERT_OR_UPDATE_BUDGET_MONTH', [p_date])


def sql_get_budget_result_shift(date, shift):
    cur_get_result_shift = cursor.var(oracledb.CURSOR)
    cursor.callproc('ZSU.GET_BUDGET_RESULT_SHIFT', [date, shift, cur_get_result_shift])
    return cur_get_result_shift


def sql_get_budget_result_24hours(date):
    cur_get_result_hours = cursor.var(oracledb.CURSOR)
    cursor.callproc('ZSU.GET_BUDGET_RESULT_HOURS', [date, cur_get_result_hours])
    return cur_get_result_hours


def sql_get_budget_result_month(date):
    cur_get_result_month = cursor.var(oracledb.CURSOR)
    cursor.callproc('ZSU.GET_BUDGET_RESULT_MONTH', [date, cur_get_result_month])
    return cur_get_result_month


def sql_insert_po6_month(
        p_date,
        p_control_id,
        p_truck_id,
        p_volumewp,
        p_top,
        p_trp,
        p_krp,
        p_regp,
        p_obp,
        p_ingp,
        p_bvrp
):
    cursor.callproc(
        'ZSU.INSERT_OR_UPDATE_PO6_MONTH',
        [
            p_date,
            p_control_id,
            p_truck_id,
            p_volumewp,
            p_top,
            p_trp,
            p_krp,
            p_regp,
            p_obp,
            p_ingp,
            p_bvrp
        ])


def sql_get_17_tasks_reports():
    cur_get_17_tasks_reports = cursor.var(oracledb.CURSOR)
    cursor.callproc('ZSU.GET_17_TASKS_REPORTS', [cur_get_17_tasks_reports])
    return cur_get_17_tasks_reports


def sql_update_17_overexc(id, overexc):
    cursor.callproc('ZSU.UPDATE_17_OVEREXC', [id, overexc])


def sql_get_dsk_report(date):
    cur_get_dsk_report = cursor.var(oracledb.CURSOR)
    cursor.callproc('ZSU.REPORTS.GET_DSK', [date, cur_get_dsk_report])
    return cur_get_dsk_report


def sql_get_walking_report_crew_new(date):
    cur_get_walking_report_crew_new = cursor.var(oracledb.CURSOR)
    cursor.callproc('ZSU.ASDFORM.GET_WALKING_REPORT_WEB', [date, cur_get_walking_report_crew_new])
    return cur_get_walking_report_crew_new


def sql_get_vehicle(date, shift):
    sql_get_vehicle_result = cursor.var(oracledb.CURSOR)
    cursor.callproc('ZSU.EXPORTFULLREPORT.GET_VEHICLE', [date, shift, sql_get_vehicle_result])
    return sql_get_vehicle_result


def sql_get_shovels(date, shift):
    sql_get_shovels_result = cursor.var(oracledb.CURSOR)
    cursor.callproc('ZSU.EXPORTFULLREPORT.GET_SHOVELS', [date, shift, sql_get_shovels_result])
    return sql_get_shovels_result


def sql_get_bulls(date, shift):
    sql_get_bulls_result = cursor.var(oracledb.CURSOR)
    cursor.callproc('ZSU.EXPORTFULLREPORT.GET_BULLS', [date, shift, sql_get_bulls_result])
    return sql_get_bulls_result


def sql_get_allstoppagesdet(date):
    sql_get_allstoppagesdet_result = cursor.var(oracledb.CURSOR)
    cursor.callproc('ZSU.GET_ALLSTOPPAGESDET', [date, sql_get_allstoppagesdet_result])
    return sql_get_allstoppagesdet_result


def sql_get_wellmetervalue(date, shift):
    sql_get_wellmetervalue_result = cursor.var(oracledb.CURSOR)
    cursor.callproc('ZSU.EXPORTFULLREPORT.GET_WELLMETERVALUE', [date, shift, sql_get_wellmetervalue_result])
    return sql_get_wellmetervalue_result
