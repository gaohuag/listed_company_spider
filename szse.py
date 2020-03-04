import csv

import xlrd

import sql_process


def process_xlsx(csv_file_name, xlsx_name,
                 csv_head=['industry_code', 'industry_type', 'company_code', 'company_full_name_CH', 'stock_codeA',
                           'stock_codeB']):
    data = xlrd.open_workbook(xlsx_name)
    table = data.sheets()[0]
    nrows = table.nrows  # 行数
    ncols = table.ncols  # 列数

    data_head = table.row_values(0)  # 第一行数据

    industry_no = data_head.index('所属行业')
    company_code_NO = data_head.index('公司代码')
    company_full_name_CH_NO = data_head.index('公司全称')
    stock_codeA_NO = data_head.index('A股代码')
    stock_codeB_NO = data_head.index('B股代码')
    province_NO = data_head.index('省    份')
    city_NO = data_head.index('城     市')
    web_site_NO = data_head.index('公司网址')
    stock_A_listed_time_NO = data_head.index('A股上市日期')
    register_address_NO = data_head.index('注册地址')
    company_name_NO = data_head.index('公司简称')

    for i in range(1, nrows):
        company_data = []
        row_values = table.row_values(i)  # 某一行数据
        industry = row_values[industry_no]
        industry_code = industry[:1]
        industry_type = industry[1:]
        company_code = row_values[company_code_NO]
        company_full_name_CH = row_values[company_full_name_CH_NO]
        stock_codeA = row_values[stock_codeA_NO]
        stock_codeB = row_values[stock_codeB_NO]
        stock_A_listed_time = row_values[stock_A_listed_time_NO]
        web_site = row_values[web_site_NO]
        city = row_values[city_NO]
        province = row_values[province_NO]
        register_address = row_values[register_address_NO]
        company_name = row_values[company_name_NO]


        if len(stock_codeA) < 3:
            stock_codeA = ''

        if len(stock_codeB) < 3:
            stock_codeB = ''

        sql_process.insert_into_table_credit_file_info(industry_code=industry_code, company_code=company_code,
                                                       industry_type=industry_type,
                                                       company_full_name_CH=company_full_name_CH,
                                                       stock_codeA=stock_codeA,
                                                       stock_codeB=stock_codeB,
                                                       city=city,
                                                       province=province,
                                                       web_site=web_site,
                                                       register_address=register_address,
                                                       stock_A_listed_time=stock_A_listed_time,
                                                       company_name=company_name)

        # 按照顺序准备即将写入csv文件的数据
        for csv_head_info in csv_head:
            # eval():将字符串str当成有效的表达式来求值并返回计算结果。
            company_data.append(eval(csv_head_info))

        # 将数据写入csv文件中
        with open(csv_file_name, 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(company_data)
