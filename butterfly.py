import pandas as pd
import plotly.graph_objects as go

# 数据
data = {
    "Rank": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    "value": [
        17.82, 17.34, 17.20, 17.08, 16.46, 16.39, 16.23, 15.87, 15.83, 15.65,
        15.47, 15.47, 15.39, 15.04, 15.04, 15.02, 15.00, 14.95, 14.88, 14.86
    ],
    "headgroup": [
        "CHL", "CHL", "LHL", "CHL", "CHL", "CHL", "CHL", "CHL", "CHL", "CHL",
        "CHL", "LHL", "CHL", "LHL", "LHL", "CHL", "CHL", "CHL", "CHL", "CHL"
    ],
    "tail": [
        "Tail 10", "Tail 10", "Tail 10", "Tail 10", "Tail 10", "Tail 10", "Tail 10",
        "Tail 15", "Tail 10", "Tail 2", "Tail 10", "Tail 9", "Tail 7", "Tail 5",
        "Tail 8", "Tail 10", "Tail 3", "Tail 11", "Tail 11", "Tail 10"
    ],
    "amino_acid": [
        "Cha", "Asn", "Cha", "Ser", "Sem", "Trp", "Thr", "Orn", "Gln", "Lys",
        "Tyr", "Lys", "Hcy", "Cha", "Cha", "Met", "Pen", "Asn", "His", "Ser"
    ]
}

# 将数据转换为 DataFrame
df = pd.DataFrame(data)

# 创建 Butterfly 图
fig = go.Figure()

# 左侧柱状图（headgroup）
fig.add_trace(
    go.Bar(
        y=df["headgroup"],
        x=df["value"],
        orientation="h",
        name="Headgroup",
        marker=dict(color="#D8BFD8"),  # 紫色
    )
)

# 右侧柱状图（amino_acid）
fig.add_trace(
    go.Bar(
        y=df["amino_acid"],
        x=-df["value"],  # 负值用于反向显示
        orientation="h",
        name="Amino Acid",
        marker=dict(color="#98FB98"),  # 淡绿色
    )
)

# 更新布局
fig.update_layout(
    title="Butterfly Chart: Headgroup vs Amino Acid",
    xaxis=dict(
        title="Value",
        tickvals=[-20, -15, -10, -5, 0, 5, 10, 15, 20],
        ticktext=["20", "15", "10", "5", "0", "5", "10", "15", "20"],
    ),
    yaxis=dict(title="Groups"),
    barmode="overlay",
    bargap=0.5,
    template="plotly_white",
)

# 显示图表
fig.show()

# 导出图表为 SVG 格式
fig.write_image("butterfly_chart.svg", format="svg")