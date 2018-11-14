Dim x
' These three produce the same result. However, the use of constants as in the third line 
' is considered best practice.
x = MsgBox("Hello World:Text",1+64+4096,"Hello World:Title")
x = MsgBox("Hello World:Text",4161,"Hello World:Title")
x = MsgBox("Hello World:Text", vbOKCancel+vbInformation+vbSystemModal, _
           "Hello World:Title")
 
' Presents the number corresponding to the button pressed. Different constants will produce 
' different behaviours. For example, vbOKCancel specifies two buttons in the dialogue box, 
' whereas vbYesNoCancel specifies three.
x = MsgBox("Hello World:Text", vbYesNoCancel+vbInformation,"Hello World:Title")
MsgBox "The result is " & x