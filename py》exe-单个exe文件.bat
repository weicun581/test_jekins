::ʹ��˵����
::    ����������ļ���������.py�ļ�ת����.exe�ļ���
::    ʹ��Ҫ����Ҫ��.py�ļ��Ͻ�DOS���棬���س�����������dist�ļ��У�
::���ߣ�Jimmy.wei  2016/6/6    ��Ȩ���У�άȨ·�Ͼ�����Ĭ������


@echo off & color 0 
 setlocal enabledelayedexpansion
  
 set/p a=�������ļ�: 
 for %%a in (!a!) do (
  set name=%%~nxa
 )
pyinstaller -F -w %name%
echo ��ϲ����ִ���ļ�%name%.exe�����ɣ�����֤�Ƿ���Ч������
echo ��ϲ����ִ���ļ�%name%.exe�����ɣ�����֤�Ƿ���Ч������
echo ��ϲ����ִ���ļ�%name%.exe�����ɣ�����֤�Ƿ���Ч������
echo ��ϲ����ִ���ļ�%name%.exe�����ɣ�����֤�Ƿ���Ч������
echo ��ϲ����ִ���ļ�%name%.exe�����ɣ�����֤�Ƿ���Ч������
@msg * ��ϲ����ִ���ļ�%name%.exe�����ɣ�����֤�Ƿ���Ч������
pause