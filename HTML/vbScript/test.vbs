x = weekday(date)

select case x
	case 1
		x = MsgBox ("Sun", 0)
	case 2
		x = MsgBox ("Mon", 0)
	case 3
		x = MsgBox ("Tue", 0)
	case 4
		x = MsgBox ("Wed", 0)
	case 5
		x = MsgBox ("Thu", 0)
	case 6
		x = MsgBox ("Fri", 0)
	case 7
		x = MsgBox ("Sat", 0)
End Select