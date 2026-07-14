-- ====================== 第一部分：数据库和数据表创建语句（项目初始化） ======================
-- 创建消费数据库，如果不存在就新建
CREATE DATABASE IF NOT EXISTS consume_db DEFAULT CHARACTER SET utf8mb4;

-- 切换使用这个数据库
USE consume_db;

-- 创建消费账单数据表
CREATE TABLE IF NOT EXISTS `user_bill` (
  `id` INT PRIMARY KEY AUTO_INCREMENT COMMENT '自增编号',
  `consume_date` DATE NOT NULL COMMENT '消费日期',
  `consume_type` VARCHAR(20) NOT NULL COMMENT '消费分类',
  `money` DECIMAL(10,2) NOT NULL COMMENT '消费金额',
  `pay_method` VARCHAR(20) NOT NULL COMMENT '支付方式',
  `remark` VARCHAR(100) DEFAULT NULL COMMENT '备注信息'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ====================== 第二部分：数据分析查询语句（依次执行导出表格） ======================
-- 1、查询整张原始账单表，导出文件：01_all_original_bills.csv
SELECT * FROM user_bill;

-- 2、按消费分类统计总花费、消费次数，导出文件：02_category_spend_statistics.csv
SELECT 
consume_type AS 消费分类,
SUM(money) AS 总支出金额,
COUNT(id) AS 消费次数
FROM user_bill
GROUP BY consume_type
ORDER BY 总支出金额 DESC;

-- 3、按日期汇总每日开销，导出文件：03_daily_consumption_summary.csv
SELECT 
consume_date AS 消费日期,
SUM(money) AS 当日总花费
FROM user_bill
GROUP BY consume_date
ORDER BY consume_date ASC;

-- 4、按支付方式统计开销，导出文件：04_payment_method_statistics.csv
SELECT 
pay_method AS 支付方式,
SUM(money) AS 总支付金额,
COUNT(id) AS 使用次数
FROM user_bill
GROUP BY pay_method
ORDER BY 总支付金额 DESC;

-- 5、筛选单笔最贵的前10条消费记录，导出文件：05_top10_highest_expense.csv
SELECT * FROM user_bill
ORDER BY money DESC
LIMIT 10;

-- 6、单独查询餐饮外卖分类全部订单，导出文件：06_catering_takeout_orders.csv
SELECT * FROM user_bill
WHERE consume_type = '餐饮外卖';