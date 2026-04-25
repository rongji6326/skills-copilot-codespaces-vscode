import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.font_manager as fm
import numpy as np

# Use a font that supports Chinese characters
plt.rcParams['font.family'] = 'WenQuanYi Zen Hei'
plt.rcParams['axes.unicode_minus'] = False

# ── 配送中心坐标 ──────────────────────────────────────────────────────────────
depot = (20, 20)

# ── 客户坐标（依据第二张图估读） ──────────────────────────────────────────────
customers = [
    # 绿色配送区内部 (|x|<=10, |y|<=10)
    (-2,  9), ( 1,  7), ( 4,  6), (-4,  4), ( 6,  4),
    (-7,  2), (-1,  2), ( 3,  1), ( 7,  1), (-5, -2),
    ( 2, -2), (-8, -4), ( 0, -4), ( 5, -5), (-3, -7),
    ( 4, -8), (-1, -9), ( 7, -6), (-6, -9),
    # 外部客户 — 第二、第三象限
    (-35,  2), (-35, 16), (-30,  8), (-30, -14), (-28,  2),
    (-25, 25), (-20, 18), (-20,  8), (-20, -9),  (-20, -20),
    (-15, 30), (-15, 18), (-12, 10), (-12, -9),  (-12, -15),
    (-10, 35), ( -8,  0), ( -8, -23),( -8, -33),
    ( -5, 30), ( -5, 15), ( -3,  3), ( -3, -20), ( -3, -29),
    (  0,-11), (  0,-30), (  0,-39),
    # 外部客户 — 第一、第四象限
    (  2, 31), (  2,-12), (  2,-27),
    (  8, 17), (  8,  6), (  8,-12), ( 10,-27),
    ( 12, 29), ( 12, 24), ( 12,  7), ( 12,-14), ( 12,-28),
    ( 15,-19), ( 15,-34),
    ( 18, 24), ( 18,-14),
    ( 20,-34),
    ( 22,  7), ( 22,-10),
    ( 25,-20),
    ( 28,-25),
    ( 30, 13), ( 30, -8), ( 30,-11),
    ( 33,  7), ( 35,-10),
]

# ── 5 条车辆路线（将客户按区域/方向分组） ────────────────────────────────────
vehicle_routes = {
    '燃油车1':   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
    '燃油车2':   [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33],
    '燃油车3':   [34, 35, 36, 37, 38, 39, 40, 41, 42],
    '新能源车1': [43, 44, 45, 46, 47, 48, 49, 50, 51],
    '新能源车2': [52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62],
}

colors = {
    '燃油车1':   '#1f77b4',   # 蓝
    '燃油车2':   '#ff7f0e',   # 橙
    '燃油车3':   '#d62728',   # 红
    '新能源车1': '#2ca02c',   # 绿
    '新能源车2': '#9467bd',   # 紫
}

# ── 绘图 ──────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 10))

# 坐标轴
ax.axhline(0, color='black', linewidth=0.8)
ax.axvline(0, color='black', linewidth=0.8)
ax.set_xlim(-40, 40)
ax.set_ylim(-42, 42)
ax.set_xlabel('X坐标 (km)', fontsize=12)
ax.set_ylabel('Y坐标 (km)', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.4)
ax.set_aspect('equal')

# 绿色配送区
circle = plt.Circle((0, 0), 10, edgecolor='green', linestyle='--',
                     fill=True, facecolor='#d0f0d0', alpha=0.5,
                     linewidth=1.8, zorder=2)
ax.add_patch(circle)

# 路线（depot → 每个客户）
for vname, indices in vehicle_routes.items():
    c = colors[vname]
    for idx in indices:
        if idx < len(customers):
            cx, cy = customers[idx]
            ax.plot([depot[0], cx], [depot[1], cy],
                    color=c, linewidth=0.9, alpha=0.75, zorder=3)

# 客户点
xs, ys = zip(*customers)
ax.scatter(xs, ys, color='gray', s=20, zorder=4, label='客户点')

# 市中心
ax.plot(0, 0, 'k+', markersize=10, markeredgewidth=2, zorder=5, label='市中心 (0,0)')

# 配送中心
ax.plot(depot[0], depot[1], 'r*', markersize=16, zorder=6, label='配送中心')

# 图例
legend_handles = [
    plt.Line2D([0], [0], color=colors[v], linewidth=2, label=v)
    for v in vehicle_routes
]
legend_handles += [
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='gray',
               markersize=7, label='客户点'),
    plt.Line2D([0], [0], marker='*', color='w', markerfacecolor='red',
               markersize=12, label='配送中心'),
    plt.Line2D([0], [0], linestyle='--', color='green',
               linewidth=1.5, label='绿色配送区 (r=10km)'),
]
ax.legend(handles=legend_handles, loc='upper right', fontsize=9,
          framealpha=0.9, edgecolor='gray')

plt.tight_layout()
plt.savefig('route_map.png', dpi=150, bbox_inches='tight')
print("Saved route_map.png")
