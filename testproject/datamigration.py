# This module is used to load data from XLSX to data base.
import xlrd
import MySQLdb
from testproject.settings import *
if __name__ == '__main__':
    database = MySQLdb.connect(host=MYSQL_HOST, user=MYSQL_USER, passwd=MYSQL_PWD, db=DB_NAME)
    cursor = database.cursor()
    xl_wordbook = xlrd.open_workbook('company_data.xlsx')
    sheet_names = xl_wordbook.sheet_names()
    first_sheet = sheet_names[0]
    month = 1
    firstxl_sheet = xl_wordbook.sheet_by_name(first_sheet)
    for xl_row in firstxl_sheet._cell_values[2:]:
        query_comp = """INSERT INTO companycrf_company (cname) VALUES ('{}')
            """.format(xl_row[0])
        cursor.execute(query_comp)
        database.commit()
    for sheet in sheet_names:
        xl_sheet = xl_wordbook.sheet_by_name(sheet)
        company_id=1
        for xl_row in xl_sheet._cell_values[2:]:
            query_parm = """INSERT INTO companycrf_param (Param1, Param2, Param3, Param4, Param5,
                Param6, Param7, Param8, Param9, Param10, month_num, company_id)
                VALUES ({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11})""".format(
                xl_row[1],xl_row[2],xl_row[3],xl_row[4],xl_row[5],xl_row[6],xl_row[7],xl_row[8],
                xl_row[9],xl_row[10], month, company_id)
            cursor.execute(query_parm)
            database.commit()
            company_id = company_id + 1
        month = month + 1