@echo off
cd /d "D:/Scripts"
type NUL > %1.bat
echo . >> "C:\Users\Piyush\alias.cmd"
echo DOSKEY %1="D:\Scripts\%1.bat" >> "C:\Users\Piyush\alias.cmd"