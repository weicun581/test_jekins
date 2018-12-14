::使用说明：
::    这个批处理文件是用来将.py文件转换成.exe文件。
::    使用要求：需要将.py文件拖进DOS界面，按回车键即可生成dist文件夹！
::作者：Jimmy.wei  2016/6/6    版权所有，维权路上绝不沉默！！！


@echo off & color 0 
 setlocal enabledelayedexpansion
  
 set/p a=请拉入文件: 
 for %%a in (!a!) do (
  set name=%%~nxa
 )
pyinstaller -F -w %name%
echo 恭喜，可执行文件%name%.exe已生成，请验证是否有效！！！
echo 恭喜，可执行文件%name%.exe已生成，请验证是否有效！！！
echo 恭喜，可执行文件%name%.exe已生成，请验证是否有效！！！
echo 恭喜，可执行文件%name%.exe已生成，请验证是否有效！！！
echo 恭喜，可执行文件%name%.exe已生成，请验证是否有效！！！
@msg * 恭喜，可执行文件%name%.exe已生成，请验证是否有效！！！
pause