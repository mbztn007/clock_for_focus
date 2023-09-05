# 导入tkinter模块，用于创建窗口和显示时间
import tkinter as tk

# 创建一个窗口对象，命名为window
window = tk.Tk()

# 设置窗口的标题为"专注时钟"
window.title("专注时钟")

# 设置窗口的大小为300x100像素，并居中显示
window.geometry("300x100+{}+{}".format(int((window.winfo_screenwidth() - 300) / 2), int((window.winfo_screenheight() - 100) / 2)))

# 创建一个标签对象，命名为label，用于显示倒计时
label = tk.Label(window, text="120:00", font=("Arial", 32))

# 将标签放置在窗口的中央
label.pack(expand=True)

# 定义一个变量，命名为seconds，用于存储剩余的秒数，初始值为120分钟乘以60秒，即7200秒
seconds = 120 * 60

# 定义一个函数，命名为update_time，用于更新倒计时
def update_time():
    # 声明全局变量seconds，以便在函数内修改它的值
    global seconds

    # 如果seconds大于0，说明倒计时还没有结束
    if seconds > 0:
        # 将seconds减去1，表示过去了一秒
        seconds -= 1

        # 计算剩余的分钟数和秒数，分别赋值给minutes和secs
        minutes = seconds // 60
        secs = seconds % 60

        # 格式化时间，用冒号分隔分钟数和秒数，并补齐两位数，例如"05:07"
        time = "{:02d}:{:02d}".format(minutes, secs)

        # 更新标签的文本为当前的时间
        label.config(text=time)

        # 在一秒后再次调用update_time函数，实现循环更新
        window.after(1000, update_time)

    # 否则，说明倒计时已经结束
    else:
        # 销毁窗口对象，关闭窗口
        window.destroy()

# 调用update_time函数，开始倒计时
update_time()

# 进入窗口的主循环，等待用户的操作
window.mainloop()
