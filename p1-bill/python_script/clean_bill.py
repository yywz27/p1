# 导入工具包
import pandas as pd
from datetime import datetime

# 固定文件路径（已经锁定文件夹，直接写文件名即可）
input_file = "bill_data.xlsx"
output_file = "cleaned_bill.xlsx"

def clean_bill_data():
    # 1.读取原始表格数据
    df = pd.read_excel(input_file, sheet_name="bill")
    print("✅ 原始数据读取成功，总条数：", df.shape[0])

    # 打印全部列名，用来核对（防止名字写错）
    print("\n表格所有表头名称：")
    print(df.columns.tolist())

    # 打印数据整体情况
    print("\n===== 数据基础信息 =====")
    print(df.info())
    print("\n===== 空白单元格统计 =====")
    print(df.isnull().sum())

    # 2.删除完全一模一样的重复行
    df = df.drop_duplicates()
    print(f"\n去重之后剩余数据条数：{df.shape[0]}")

    # 3.填充空白内容（列名和Excel完全对应，不会再KeyError）
    df["消费日期"] = df["消费日期"].ffill()       # 日期空白就沿用上面一行日期
    df["消费分类"] = df["消费分类"].fillna("未分类")
    df["金额(元)"] = df["金额(元)"].fillna(0)     # 金额空白填充0
    df["支付方式"] = df["支付方式"].fillna("未知")
    df["备注"] = df["备注"].fillna("无备注")

    # 4.统一日期格式为 2026/1/1 → 2026-01-01
    df["消费日期"] = pd.to_datetime(df["消费日期"]).dt.strftime("%Y-%m-%d")

    # 5.剔除金额为负数的异常错误数据
    df = df[df["金额(元)"] >= 0]

    # 6.重置id序号，保证连续不乱
    df = df.reset_index(drop=True)
    df["id"] = df.index + 1

    # 7.导出清洗好的新Excel文件
    df.to_excel(output_file, index=False, sheet_name="clean_bill")
    print(f"\n🎉 全部清洗完成！已生成文件：{output_file}")
    print("最终有效数据条数：", df.shape[0])

# 执行清洗函数
if __name__ == "__main__":
    clean_bill_data()

# 防止运行完窗口直接闪退
input("\n按下回车键关闭窗口")
