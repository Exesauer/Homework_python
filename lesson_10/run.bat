@echo off
set results=.\allure-results
set report_history=.\allure-report\history
set report=.\allure-report

REM Удаляем директорию results
if exist %results% (
    rmdir /S /Q %results%
)

REM Запускаем pytest и сохраняем результаты
python -m pytest test_calc.py test_shop.py --alluredir=%results%

REM Перемещаем файлы из report_history в results
if exist %report_history% (
    move %report_history% %results%
)

REM Удаляем директорию report
if exist %report% (
    rmdir /S /Q %report%
)

REM Генерируем allure отчет
start /wait allure generate %results% -o %report%

REM Открываем allure отчет
start allure open %report%