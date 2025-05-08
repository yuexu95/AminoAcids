import pandas as pd
import plotly.graph_objects as go
import re

# 原始数据
raw_data = [
    {"name": "ChaCHL10", "value": 17.823187},
    {"name": "AsnCHL10", "value": 17.339807},
    {"name": "ChaLHL10", "value": 17.198474},
    {"name": "SerCHL10", "value": 17.081255},
    {"name": "SemCHL10", "value": 16.461272},
    {"name": "TrpCHL10", "value": 16.393441},
    {"name": "ThrCHL10", "value": 16.231615},
    {"name": "OrnCHL15", "value": 15.874429},
    {"name": "GlnCHL10", "value": 15.827665},
    {"name": "LysCHL2", "value": 15.648245},
    {"name": "TyrCHL10", "value": 15.471389},
    {"name": "LysLHL9", "value": 15.468624},
    {"name": "HcyCHL7", "value": 15.392988},
    {"name": "ChaLHL5", "value": 15.043027},
    {"name": "ChaLHL8", "value": 15.042258},
    {"name": "MetCHL10", "value": 15.016678},
    {"name": "PenCHL3", "value": 14.996076},
    {"name": "AsnCHL11", "value": 14.954605},
    {"name": "HisCHL11", "value": 14.883025},
    {"name": "Ser0CHL10", "value": 14.859583},
]

# 将原始数据转换为 DataFrame
df = pd.DataFrame(raw_data)

# 定义解析函数，将 name 拆分为 amino_acid、headgroup 和 tail
def parse_name(name):
    match = re.match(r"([A-Za-z0-9]+)(CHL|LHL)(\d+)", name)
    if match:
        return pd.Series([match.group(1), match.group(2), match.group(3)])
    else:
        return pd.Series([None, None, None])

# 应用解析函数
df[["amino_acid", "headgroup", "tail"]] = df["name"].apply(parse_name)

# 按 value 降序取前 20 行
df_top = df.sort_values(by="value", ascending=False).head(20)

# 按 amino_acid 聚合并计算总 value
amino_acid_values = (
    df_top.groupby("amino_acid")["value"].sum().sort_values(ascending=False)
)

# 按 amino_acid 的总 value 降序调整 labels
labels = list(amino_acid_values.index) + list(
    pd.unique(df_top[["headgroup", "tail"]].values.ravel())
)

# 创建 label 映射
label_map = {k: i for i, k in enumerate(labels)}

# 构建 Sankey 图的 source、target 和 value
sources = []
targets = []
values = []

# amino_acid → headgroup
for _, row in df_top.iterrows():
    sources.append(label_map[row["amino_acid"]])
    targets.append(label_map[row["headgroup"]])
    values.append(row["value"])

# headgroup → tail
for _, row in df_top.iterrows():
    sources.append(label_map[row["headgroup"]])
    targets.append(label_map[row["tail"]])
    values.append(row["value"])

# 绘制 Sankey 图
fig = go.Figure(
    data=[
        go.Sankey(
            node=dict(
                pad=15,
                thickness=20,
                line=dict(color="black", width=0.5),
                label=labels,
            ),
            link=dict(
                source=sources,
                target=targets,
                value=values,
                hovertemplate="Source: %{source.label}<br>Target: %{target.label}<br>Value: %{value}<extra></extra>",
            ),
        )
    ]
)

# 设置图表标题和样式
fig.update_layout(title_text="Top 20 Pathways by Value", font_size=12)
fig.show()