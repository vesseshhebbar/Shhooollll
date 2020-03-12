x = InputBox("Please enter the last name of the person:")

select case x
	case "Raj"
		x = MsgBox ("Raj is the President", 0)
	case "Ram"
		x = MsgBox ("Ram is the Senior Vice President", 0)
	case "Kumar"
		x = MsgBox ("Kumar is the Vice President", 0)
	case "Sri"
		x = MsgBox ("Sri is the Manager", 0)
	case else:
		x = MsgBox("Hello " & x & ", You are not part of the management team.", 0)
End Select