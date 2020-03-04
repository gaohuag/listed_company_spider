use spider_work;
drop table if exists listed_company;

create table if not exists financial_data(
`id` int(10) unsigned NOT NULL AUTO_INCREMENT,
-- stock_codeA
stock_codeA  varchar(20),
-- 报告期
report_period date,
-- 净利润同比(%)
retained_profits_on_year_basis DECIMAL(4,2),
-- 每股收益(元) 本期
earnings_per_share DECIMAL(10,2),
-- 每股收益(元) 同比(%)
earnings_per_share_on_year_basis DECIMAL(4,2),
-- 每股净资产 本期
net_asset_value_per_share DECIMAL(10,2),
-- 每股净资产 同比(%)
net_asset_value_per_share_on_year_basis DECIMAL(4,2),
-- 净资产收益率(%) 本期
roe DECIMAL(4,2),
-- 净资产收益率(%) 同比(%)
roe_on_year_basis DECIMAL(4,2),
-- 每股现金流(元) 本期
cash_flow_per_share  DECIMAL(10,2),
-- 每股现金流(元) 同比(%)
cash_flow_per_share_on_year_basis  DECIMAL(4,2),
-- 分配方案
allocation varchar(2000),
 PRIMARY KEY (`id`)
)DEFAULT CHARSET=utf8;
create table if not exists listed_company(
-- ID
id varchar(50) NOT NULL,       
-- 行业代码
industry_code varchar(1),
-- 上市公司代码
company_code varchar(10),
-- 行业种类
industry_type varchar(20),
-- 公司简称
company_name varchar(50),
-- 公司中文全称
company_full_name_CH varchar(100),
-- A股代码
stock_codeA varchar(20),
-- B股代码
stock_codeB varchar(50),
-- 省
province varchar(10),
-- 市
city varchar(10),
-- 公司网址
web_site varchar(50),
-- 注册地址
register_address varchar(200),
-- A股上市时间
stock_A_listed_time date,
-- 爬虫时间
update_date date,
-- 市盈率
pe_ttm DECIMAL(6,2),
pe_move DECIMAL(6,2),
pe_static DECIMAL(6,2),
pb  DECIMAL(6,2),
PRIMARY KEY (update_date, company_full_name_CH, company_code)
)DEFAULT CHARSET=utf8;
