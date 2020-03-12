
ram = InputBox("Enter Ram's Age")
raj =  InputBox("Enter Raj's Age")

if(ram > raj) Then
	MsgBox "Ram is older than Raj", 0, "Information about Ram and Raj"

elseif(raj > ram) Then
	MsgBox "Raj is older than Ram", 0, "Information about Ram and Raj"

else
	MsgBox "Ram and Raj are peers", 0, "Information about Ram and Raj"
End If



MsgBox "Ram and Raj are " & ram & " and " & raj & " years old respectively", 0, "Information about " & name