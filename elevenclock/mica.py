
import ctypes
from ctypes.wintypes import  DWORD, BOOL, HRGN, HWND


def mica(hwnd: int, darkMode: bool):
    user32 = ctypes.windll.user32
    dwm = ctypes.windll.dwmapi


    class ACCENTPOLICY(ctypes.Structure):
        _fields_ = [
            ("AccentState", ctypes.c_uint),
            ("AccentFlags", ctypes.c_uint),
            ("GradientColor", ctypes.c_uint),
            ("AnimationId", ctypes.c_uint)
        ]


    class WINDOWCOMPOSITIONATTRIBDATA(ctypes.Structure):
        _fields_ = [
            ("Attribute", ctypes.c_int),
            ("Data", ctypes.POINTER(ctypes.c_int)),
            ("SizeOfData", ctypes.c_size_t)
        ]


    class DWM_BLURBEHIND(ctypes.Structure):
        _fields_ = [
            ('dwFlags', DWORD), 
            ('fEnable', BOOL),  
            ('hRgnBlur', HRGN), 
            ('fTransitionOnMaximized', BOOL) 
        ]


    class MARGINS(ctypes.Structure):
        _fields_ = [("cxLeftWidth", ctypes.c_int),
                    ("cxRightWidth", ctypes.c_int),
                    ("cyTopHeight", ctypes.c_int),
                    ("cyBottomHeight", ctypes.c_int)
                    ]


    SetWindowCompositionAttribute = user32.SetWindowCompositionAttribute
    DwmSetWindowAttribute = dwm.DwmSetWindowAttribute 


    accent = ACCENTPOLICY()
    
    accent.GradientColor = int("00cccccc", base=16)
    accent.AccentState = 5

    data = WINDOWCOMPOSITIONATTRIBDATA()
    data.Attribute = 19 #WCA_ACCENT_POLICY
    data.SizeOfData = ctypes.sizeof(accent)
    data.Data = ctypes.cast(ctypes.pointer(accent), ctypes.POINTER(ctypes.c_int))
    
    SetWindowCompositionAttribute(int(hwnd), data)
    
    if darkMode:
        data.Attribute = 26 #WCA_USEDARKMODECOLORS
        SetWindowCompositionAttribute(int(hwnd), data)

    print("Res:", DwmSetWindowAttribute(int(hwnd), 1029, ctypes.byref(ctypes.c_int(0x01)), ctypes.sizeof(ctypes.c_int)))
