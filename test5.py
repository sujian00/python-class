# ====================== 超精细版 · 纯Python原生无插件 ======================
# 牛顿冷却定律 | 欧拉法 | Δt=0.1 | 100帧 | 高精度控制台绘图
# 无任何第三方库，无插件，纯原生，直接运行

# ========== 1. 基础参数 ==========
dt = 0.1           # 时间步长
total_frames = 100 # 计算100帧
T_env = 25.0       # 环境温度
T_now = 100.0      # 初始温度
cool_k = 0.05      # 冷却系数

# ========== 2. 存储所有数据 ==========
data = []
for frame in range(1, total_frames + 1):
    data.append((frame, T_now))
    # 欧拉法核心公式
    dTdt = -cool_k * (T_now - T_env)
    T_now = T_now + dt * dTdt

# ========== 3. 输出超精细表格 ==========
print("=" * 70)
print("                牛顿冷却定律 - 欧拉法计算结果（1~100帧）")
print(f"Δt = {dt}   |   初始温度 = 100°C   |   环境温度 = 25°C   |   冷却系数 = {cool_k}")
print("=" * 70)
print(f"{'帧数':<6}{'温度(°C)':<12}{'帧数':<6}{'温度(°C)':<12}{'帧数':<6}{'温度(°C)':<12}{'帧数':<6}{'温度(°C)':<12}")
print("-" * 70)

# 4列并排输出，更整洁
for i in range(0, total_frames, 4):
    line = ""
    for j in range(4):
        if i + j < total_frames:
            f, t = data[i + j]
            line += f"{f:<6}{t:<12.4f}"
    print(line)

# ========== 4. 高精度字符绘图（逐帧、等比例、精细） ==========
print("\n" + "=" * 70)
print("                        温度变化精细曲线图")
print("【左=帧数 | 右=温度 | ★长度=温度高低】")
print("=" * 70)

max_t = 100.0
min_t = 25.0
plot_length = 60  # 绘图精度

for idx, (frame, temp) in enumerate(data):
    # 等比例计算星号长度
    ratio = (temp - min_t) / (max_t - min_t)
    stars = "★" * int(ratio * plot_length)
    # 每10帧输出一次，避免刷屏（可改成1逐帧输出）
    if frame % 10 == 0 or frame == 1:
        print(f"第{frame:>3}帧 | {stars:<60} {temp:>6.2f} °C")

print("-" * 70)
print("✅ 计算完成：100帧高精度温度 + 精细字符绘图已全部输出")