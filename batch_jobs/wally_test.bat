REM Get baseline code coverage for host1_max.pdf. Test suite of 1000 pdf
REM Mode = Single Object Update (SOU)
REM test mupdf pdf viewer on windows (c++ win32)
REM @ECHO off
SET PATH=%PATH%;"C:\Program Files (x86)\Microsoft Visual Studio 17.0\Team Tools\Performance Tools\x64"
CLS
C:
CD C:\Users\"De Kai"\Desktop\Security\Research\mupdf\platform\win32\x64\Debug
CLS

START VSPerfMon /coverage /output:./host1_max_baseline2_mou.coverage
REM ping google.com
timeout /t 5
 
FOR %%i IN (.\pdfs_small\*.pdf) DO ( 
	REM mutool clean -difa %%i	
	REM mutool clean -d %%i
	REM mutool clean -a
	REM mutool clean %%i
	REM mutool show -b %%i
	REM timeout /t 1
	START mupdf %%i
	timeout /t 3
	taskkill /IM mupdf.exe
	timeout /t 2
	)

timeout /t 5
VSPerfCmd /shutdown

REM With above config 1000 pdf file take about 83.33 minutes to be processed
REM just to get code coverage data 



