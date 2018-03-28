import win32api, win32con, time
def click(x,y):
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
ct = 1
while(True):
	click(600,600)
	time.sleep(10)
	# print('printed' + str(ct))
	# ct = ct + 1
