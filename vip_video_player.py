import tkinter as tk
from tkinter import ttk, messagebox
import requests
import webbrowser

def create_ui():
    # 主窗口（700x550，适配操作）
    root = tk.Tk()
    root.title("VIP视频播放器")
    root.geometry("700x550")
    root.resizable(width=False, height=False)

    # 标题
    title_label = tk.Label(root, text="VIP视频播放器", font=("微软雅黑", 24, "bold"))
    title_label.pack(pady=(30, 10))

    # 副标题
    sub_label = tk.Label(root, text="支持大部分主流视频网站", font=("微软雅黑", 12))
    sub_label.pack(pady=(0, 30))

    # 输入框区域
    input_frame = tk.Frame(root)
    input_frame.pack(fill="x", padx=40)
    input_label = tk.Label(input_frame, text="请输入视频链接:", font=("微软雅黑", 12))
    input_label.pack(anchor="w")
    
    # 视频链接输入框
    url_entry = tk.Entry(input_frame, width=80, font=("微软雅黑", 12))
    url_entry.pack(pady=(5, 15), fill="x", ipady=5)

    # --------------------- 核心：给输入框添加右键菜单 ---------------------
    def show_right_menu(event):
        # 创建右键菜单
        right_menu = tk.Menu(root, tearoff=0, font=("微软雅黑", 10))
        # 添加菜单功能
        right_menu.add_command(label="粘贴", command=lambda: url_entry.event_generate('<<Paste>>'))
        right_menu.add_command(label="复制", command=lambda: url_entry.event_generate('<<Copy>>'))
        right_menu.add_command(label="剪切", command=lambda: url_entry.event_generate('<<Cut>>'))
        right_menu.add_separator()  # 分隔线
        right_menu.add_command(label="清空", command=lambda: url_entry.delete(0, tk.END))
        # 在鼠标右键点击位置显示菜单
        try:
            right_menu.tk_popup(event.x_root, event.y_root)
        finally:
            # 释放菜单资源
            right_menu.grab_release()

    # 给输入框绑定右键点击事件
    url_entry.bind("<Button-3>", show_right_menu)
    # ---------------------------------------------------------------------

    # 按钮区域
    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=20)
    play_btn = tk.Button(btn_frame, text="播放视频", bg="#28a745", fg="white", 
                         font=("微软雅黑", 14), width=15, height=1,
                         command=lambda: play_video(url_entry.get()))
    play_btn.grid(row=0, column=0, padx=20)
    clear_btn = tk.Button(btn_frame, text="清空链接", bg="#dc3545", fg="white", 
                          font=("微软雅黑", 14), width=15, height=1,
                          command=lambda: url_entry.delete(0, tk.END))
    clear_btn.grid(row=0, column=1, padx=20)

    # 注意提示
    note_label = tk.Label(root, text="注意: 本工具仅供学习交流使用,请勿用于商业用途", 
                          font=("微软雅黑", 11), fg="#dc3545")
    note_label.pack(pady=(30, 15))

    # 视频网站标签栏（带跳转）
    site_frame = tk.Frame(root)
    site_frame.pack(pady=15, fill="x", padx=40)
    site_label = tk.Label(site_frame, text="视频网站", font=("微软雅黑", 12))
    site_label.pack(anchor="w")
    site_urls = {
        "腾讯视频": "https://v.qq.com/",
        "爱奇艺": "https://www.iqiyi.com/",
        "优酷": "https://youku.com/",
        "B站": "https://www.bilibili.com/",
        "搜狐视频": "https://tv.sohu.com/",
        "乐视视频": "https://www.letv.com/"
    }
    for site_name, site_url in site_urls.items():
        site_btn = ttk.Button(site_frame, text=site_name, width=10)
        site_btn.configure(command=lambda url=site_url: webbrowser.open(url))
        site_btn.pack(side="left", padx=10, pady=10)

    root.mainloop()

def play_video(url):
    if not url.strip():
        messagebox.showwarning("提示", "请输入视频链接!")
        return
    parse_url = f"https://jx.xmflv.com/?url={url}"
    try:
        response = requests.get(parse_url, timeout=10)
        if response.status_code == 200:
            webbrowser.open(parse_url)
        else:
            messagebox.showerror("错误", "解析失败，请检查链接!")
    except Exception as e:
        messagebox.showerror("错误", f"网络异常: {str(e)}")

if __name__ == "__main__":
    create_ui()