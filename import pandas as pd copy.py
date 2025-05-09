import pandas as pd
import plotly.graph_objects as go

# 数据
data = {
    "Rank": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    "value": [
        17.82,
        17.34,
        17.20,
        17.08,
        16.46,
        16.39,
        16.23,
        15.87,
        15.83,
        15.65,
        15.47,
        15.47,
        15.39,
        15.04,
        15.04,
        15.02,
        15.00,
        14.95,
        14.88,
        14.86,
    ],
    "headgroup": [
        "CHL",
        "CHL",
        "LHL",
        "CHL",
        "CHL",
        "CHL",
        "CHL",
        "CHL",
        "CHL",
        "CHL",
        "CHL",
        "LHL",
        "CHL",
        "LHL",
        "LHL",
        "CHL",
        "CHL",
        "CHL",
        "CHL",
        "CHL",
    ],
    "tail": [
        "Tail 10",
        "Tail 10",
        "Tail 10",
        "Tail 10",
        "Tail 10",
        "Tail 10",
        "Tail 10",
        "Tail 15",
        "Tail 10",
        "Tail 2",
        "Tail 10",
        "Tail 9",
        "Tail 7",
        "Tail 5",
        "Tail 8",
        "Tail 10",
        "Tail 3",
        "Tail 11",
        "Tail 11",
        "Tail 10",
    ],
    "amino_acid": [
        "Cha",
        "Asn",
        "Cha",
        "Ser",
        "Sem",
        "Trp",
        "Thr",
        "Orn",
        "Gln",
        "Lys",
        "Tyr",
        "Lys",
        "Hcy",
        "Cha",
        "Cha",
        "Met",
        "Pen",
        "Asn",
        "His",
        "Ser",
    ],
}

# 将数据转换为 DataFrame
df = pd.DataFrame(data)

# 创建节点标签
labels = (
    list(pd.unique(df["headgroup"]))
    + list(pd.unique(df["amino_acid"]))
    + list(pd.unique(df["tail"]))
)

# 创建 label 映射
label_map = {label: i for i, label in enumerate(labels)}

# 构建 Sankey 图的 source、target 和 value
sources = []
targets = []
values = []

# headgroup → amino_acid
for _, row in df.iterrows():
    sources.append(label_map[row["headgroup"]])
    targets.append(label_map[row["amino_acid"]])
    values.append(row["value"])

# amino_acid → tail
for _, row in df.iterrows():
    sources.append(label_map[row["amino_acid"]])
    targets.append(label_map[row["tail"]])
    values.append(row["value"])

# 定义颜色列表，15 个渐变色块
node_colors = [
    "#D8BFD8",  # 紫色
    "#C8C2E0",  # 淡紫色
    "#B8C8E8",  # 紫蓝色
    "#A8D0F0",  # 浅蓝色
    "#98D8F8",  # 天蓝色
    "#88E0E8",  # 蓝绿色
    "#78E8D8",  # 浅蓝绿色
    "#68F0C8",  # 浅绿色
    "#58F8B8",  # 亮绿色
    "#48E8A8",  # 淡绿色
    "#38D898",  # 绿色
    "#28C888",  # 深绿色
    "#C8A2C8",  # 紫粉色
    "#B090D0",  # 紫灰色
    "#A080C8",  # 深紫色
] * (
    len(labels) // 6 + 1
)  # 循环颜色，确保足够覆盖所有节点

link_colors = [
    "#DCDDDD",  # 浅灰色
] * (
    len(values) // 1 + 1
)  # 循环颜色，确保足够覆盖所有链

import pandas as pd
import plotly.graph_objects as go

# 数据
data = {
    "Rank": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    "value": [
        17.82,
        17.34,
        17.20,
        17.08,
        16.46,
        16.39,
        16.23,
        15.87,
        15.83,
        15.65,
        15.47,
        15.47,
        15.39,
        15.04,
        15.04,
        15.02,
        15.00,
        14.95,
        14.88,
        14.86,
    ],
    "headgroup": [
        "CHL",
        "CHL",
        "LHL",
        "CHL",
        "CHL",
        "CHL",
        "CHL",
        "CHL",
        "CHL",
        "CHL",
        "CHL",
        "LHL",
        "CHL",
        "LHL",
        "LHL",
        "CHL",
        "CHL",
        "CHL",
        "CHL",
        "CHL",
    ],
    "tail": [
        "Tail 10",
        "Tail 10",
        "Tail 10",
        "Tail 10",
        "Tail 10",
        "Tail 10",
        "Tail 10",
        "Tail 15",
        "Tail 10",
        "Tail 2",
        "Tail 10",
        "Tail 9",
        "Tail 7",
        "Tail 5",
        "Tail 8",
        "Tail 10",
        "Tail 3",
        "Tail 11",
        "Tail 11",
        "Tail 10",
    ],
    "amino_acid": [
        "Cha",
        "Asn",
        "Cha",
        "Ser",
        "Sem",
        "Trp",
        "Thr",
        "Orn",
        "Gln",
        "Lys",
        "Tyr",
        "Lys",
        "Hcy",
        "Cha",
        "Cha",
        "Met",
        "Pen",
        "Asn",
        "His",
        "Ser",
    ],
}

# 将数据转换为 DataFrame
df = pd.DataFrame(data)

# 创建节点标签
labels = (
    list(pd.unique(df["headgroup"]))
    + list(pd.unique(df["amino_acid"]))
    + list(pd.unique(df["tail"]))
)

# 计算每个节点的总流量（value）
node_values = pd.concat(
    [
        df.groupby("headgroup")["value"].sum(),
        df.groupby("amino_acid")["value"].sum(),
        df.groupby("tail")["value"].sum(),
    ]
)

# 创建节点标签并按总流量排序
labels = (
    pd.concat(
        [
            df.groupby("headgroup")["value"].sum(),
            df.groupby("amino_acid")["value"].sum(),
            df.groupby("tail")["value"].sum(),
        ]
    )
    .sort_values(ascending=False)
    .index.tolist()
)

# 创建 label 映射
label_map = {label: i for i, label in enumerate(labels)}

# 构建 Sankey 图的 source、target 和 value
sources = []
targets = []
values = []

# headgroup → amino_acid
for _, row in df.iterrows():
    sources.append(label_map[row["headgroup"]])
    targets.append(label_map[row["amino_acid"]])
    values.append(row["value"])

# amino_acid → tail
for _, row in df.iterrows():
    sources.append(label_map[row["amino_acid"]])
    targets.append(label_map[row["tail"]])
    values.append(row["value"])

# 定义颜色列表，15 个渐变色块
node_colors = [
    "#D8BFD8",  # 浅紫色
    "#E6E6FA",  # 薰衣草紫
    "#C8A2C8",  # 紫粉色
    "#DDA0DD",  # 浅紫色
    "#B090D0",  # 紫灰色
    "#9370DB",  # 紫罗兰色
    "#BA55D3",  # 中紫色
    "#A080C8",  # 深紫色
    "#C9A2D8",  # 柔紫色
    "#E0B0FF",  # 浅紫罗兰
    "#DAB0E8",  # 淡紫粉
    "#E6CFEF",  # 浅紫粉
    "#F3E6FA",  # 淡薰衣草紫
    "#E8D8F8",  # 柔和紫色
] * (
    len(labels) // 15 + 1
)  # 循环颜色，确保足够覆盖所有节点

link_colors = [
    "#DCDDDD",  # 浅灰色
] * (
    len(values) // 1 + 1
)  # 循环颜色，确保足够覆盖所有链

# 绘制 Sankey 图
fig = go.Figure(
    data=[
        go.Sankey(
            node=dict(
                pad=15,
                thickness=20,
                line=dict(color="black", width=0.5),
                label=labels,
                color=node_colors[: len(labels)],  # 设置节点颜色
            ),
            link=dict(
                source=sources,
                target=targets,
                value=values,
                color=link_colors[: len(values)],  # 设置链接颜色
                hovertemplate="Source: %{source.label}<br>Target: %{target.label}<br>Value: %{value}<extra></extra>",
            ),
        )
    ]
)

# 设置图表标题和样式
fig.update_layout(
    title_text="Sankey Diagram: Headgroup → Amino Acid → Tail", font_size=12
)

# 显示图表
fig.show()

# 导出图表为 SVG 格式
fig.write_image("sankey_diagram.svg", format="svg")
