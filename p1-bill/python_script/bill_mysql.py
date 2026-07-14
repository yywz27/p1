# 导入所需库
import pandas as pd
from sqlalchemy import create_engine

# 数据库连接配置
engine = create_engine("mysql+pymysql://root:021212@localhost:3306/consume_db")

# 读取Excel文件
df = pd.read_excel(r"C:\Users\86185\Desktop\p1-bill\cleaned_bill.xlsx")

# 列名映射匹配数据库字段
df = df.rename(columns={
    "id": "id",
    "消费日期": "consume_date",
    "消费分类": "consume_type",
    "金额(元)": "money",
    "支付方式": "pay_method",
    "备注": "remark"
})

# 数据写入MySQL表
df.to_sql(
    name="user_bill",
    con=engine,
    index=False,
    if_exists="append"
)

print("数据导入完成")
