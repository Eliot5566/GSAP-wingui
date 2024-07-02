import win32gui
# import win32con

def find_window(title):
    hwnd = win32gui.FindWindow(None, title)
    if hwnd:
        print(f'Found window with title: {title}, Handle: {hwnd}')
    else:
        print(f'No window found with title: {title}')
    return hwnd

def enum_child_windows(parent_hwnd):
    child_windows = []
    def callback(hwnd, lParam):
        child_windows.append(hwnd)
        return True

    win32gui.EnumChildWindows(parent_hwnd, callback, None)
    return child_windows

def get_window_info(hwnd):
    rect = win32gui.GetWindowRect(hwnd)
    title = win32gui.GetWindowText(hwnd)
    return {
        "handle": hwnd, #窗口句柄
        "title": title, #窗口標題
        "rect": rect  #rect = (left, top, right, bottom)
    }

parent_title = "設定"  # 使用要查找的父窗口標題
parent_hwnd = find_window(parent_title) # 查找父窗口

if parent_hwnd:
    child_hwnds = enum_child_windows(parent_hwnd) # 查找子窗口
    for child_hwnd in child_hwnds: # 遍歷子窗口
        info = get_window_info(child_hwnd) # 獲取窗口信息
        print(info) # 打印窗口信息
