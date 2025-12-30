import re
import tkinter as tk
import webbrowser
from tkinter import messagebox

"""
VIP视频播放器
作者：我爱云解析
版本：1.1
创建日期：2025-12-29
描述：支持主流视频网站的VIP视频播放工具
版权：仅供学习交流使用
"""


class VIPVideoPlayer:
    def __init__(self):
        # 初始化窗口
        self.root = tk.Tk()
        self.root.title("VIP视频播放器")
        self.root.geometry("500x400")

        # 设置透明度（0完全透明）
        self.root.configure(bg='')  # 清空背景色
        self.root.wm_attributes("-alpha", 1.0)

        # 创建界面组件
        self.create_widgets()

    def create_widgets(self):
        """创建界面组件"""
        # 主容器
        main_frame = tk.Frame(self.root, bg='#f0f0f0', padx=20, pady=20)
        main_frame.pack(expand=True, fill='both')

        # 标题
        title_label = tk.Label(
            main_frame,
            text="VIP视频播放器",
            font=('微软雅黑', 16, 'bold'),
            bg='#f0f0f0',
            fg='#333333'
        )
        title_label.pack(pady=(0, 10))

        # 说明文字
        subtitle_label = tk.Label(
            main_frame,
            text="支持大部分主流视频网站",
            font=('微软雅黑', 10),
            bg='#f0f0f0',
            fg='#666666'
        )
        subtitle_label.pack(pady=(0, 20))

        # URL输入框
        url_label = tk.Label(
            main_frame,
            text="请输入视频链接:",
            font=('微软雅黑', 11),
            bg='#f0f0f0',
            fg='#333333'
        )
        url_label.pack(anchor='w', pady=(0, 5))

        self.url_var = tk.StringVar()
        self.url_entry = tk.Entry(
            main_frame,
            textvariable=self.url_var,
            font=('微软雅黑', 10),
            width=50,
            relief='flat',
            bd=2,
            highlightbackground='#cccccc',
            highlightcolor='#66a3ff',
            highlightthickness=1
        )
        self.url_entry.pack(fill='x', pady=(0, 20))

        # 按钮区域
        button_frame = tk.Frame(main_frame, bg='#f0f0f0')
        button_frame.pack(pady=(0, 20))

        # 播放按钮
        play_button = tk.Button(
            button_frame,
            text="播放视频",
            command=self.play_video,
            font=('微软雅黑', 11),
            bg='#4CAF50',
            fg='white',
            relief='flat',
            padx=20,
            pady=8,
            cursor='hand2'
        )
        play_button.pack(side='left', padx=(0, 10))

        # 清空按钮
        clear_button = tk.Button(
            button_frame,
            text="清空链接",
            command=self.clear_url,
            font=('微软雅黑', 11),
            bg='#f44336',
            fg='white',
            relief='flat',
            padx=20,
            pady=8,
            cursor='hand2'
        )
        clear_button.pack(side='left')

        # 提示信息
        info_label = tk.Label(
            main_frame,
            text="注意：本工具仅供学习交流使用，请勿用于商业用途",
            font=('微软雅黑', 9),
            bg='#f0f0f0',
            fg='#e74c3c'
        )
        info_label.pack(pady=(10, 0))

        # 友情链接
        links_frame = tk.LabelFrame(
            main_frame,
            text="视频网站",
            font=('微软雅黑', 10),
            bg='#f0f0f0',
            fg='#333333',
            padx=10,
            pady=10
        )
        links_frame.pack(fill='x', pady=(20, 0))

        websites = [
            ("腾讯视频", "https://v.qq.com/"),
            ("爱奇艺", "https://www.iqiyi.com/"),
            ("优酷", "https://www.youku.com/"),
            ("B站", "https://www.bilibili.com/"),
            ("搜狐视频", "https://tv.sohu.com/"),
            ("乐视视频", "https://www.le.com/"),
            ("PPTV", "https://www.pptv.com/"),
            ("土豆视频", "https://www.tudou.com/"),
            ("暴风影音", "https://www.baofeng.com/"),
            ("咪咕视频", "https://www.miguvideo.com/"),
            ("西瓜视频", "https://www.ixigua.com/")
        ]

        for name, url in websites:
            link_btn = tk.Button(
                links_frame,
                text=name,
                command=lambda u=url: webbrowser.open(u),
                font=('微软雅黑', 9),
                bg='#e0e0e0',
                fg='#333333',
                relief='flat',
                padx=10,
                pady=5,
                cursor='hand2'
            )
            link_btn.pack(side='left', padx=5)

    def play_video(self):
        """播放视频"""
        video_url = self.url_var.get().strip()

        # 验证链接格式
        if not self.is_valid_url(video_url):
            messagebox.showerror("错误", "请输入有效的视频链接！\n链接应以 http:// 或 https:// 开头")
            return

        # 使用解析源
        parser_url = f"https://jx.xmflv.cc/?url={video_url}"

        # 在浏览器中打开解析后的链接（移除了成功提示弹窗）
        try:
            webbrowser.open(parser_url)
        except Exception as e:
            messagebox.showerror("错误", f"无法打开浏览器：{str(e)}")

    def is_valid_url(self, url):
        """验证URL格式是否正确"""
        pattern = re.compile(
            r'^https?://'  # http:// 或 https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # 域名
            r'localhost|'  # localhost
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # IP
            r'(?::\d+)?'  # 可选端口
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return url is not None and pattern.search(url) is not None

    def clear_url(self):
        """清空输入框"""
        self.url_var.set("")

    def run(self):
        """运行应用"""
        self.root.resizable(False, False)
        self.root.mainloop()


if __name__ == '__main__':
    # 隐藏控制台窗口（如果是通过pyinstaller打包成exe时生效）
    try:
        import ctypes
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    except:
        pass
    app = VIPVideoPlayer()
    app.run()