' 静默启动Python程序，无cmd窗口
Set objShell = CreateObject("WScript.Shell")
' 获取当前脚本所在目录（项目根目录）
strPath = CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName)
' 拼接本地Python和代码文件的路径，执行时隐藏窗口
objShell.Run Chr(34) & strPath & "\Python\python.exe" & Chr(34) & " " & Chr(34) & strPath & "\vip_video_player.py" & Chr(34), 0, False
Set objShell = Nothing