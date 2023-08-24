from screeninfo import get_monitors

# 获取所有连接的显示器信息
monitors = get_monitors()

# 遍历每个显示器并打印其参数
for monitor in monitors:
    print(f"Monitor Name: {monitor.name}")
    print(f"Width: {monitor.width} pixels")
    print(f"Height: {monitor.height} pixels")
    print(f"Position X: {monitor.x} pixels from the left")
    print(f"Position Y: {monitor.y} pixels from the top")
    print(f"Aspect Ratio: {monitor.width/monitor.height:.2f}")
    print(f"Screen DPI (dots per inch): {monitor.dpi}\n")