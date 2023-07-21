# SiCepat-test<br><br>

#SQL Query task<br>
Environtment: Any SQL Tools - I am using phpmyadmin<br>
a) Buat query jika mencari employee name dan status employee?<br>
answer:<br>

SELECT emp_name, emp_status<br>
FROM tbl_employee 
<br><br>
b) Buat query untuk menampilkan nama employee yang statusnya resign berserta gaji yang diperoleh?<br>
answer:<br>

SELECT e.emp_name, i.emp_income<br>
FROM tbl_employee e<br>
INNER JOIN tbl_income i ON e.emp_code = i.emp_code<br>
WHERE e.emp_status = 'R';<br><br>

c) Buat query untuk menampilkan emp_code, nama, status, income dan sorting berdasarkan income
paling besar?<br>
answer:<br><br>

SELECT e.emp_code, e.emp_name, e.emp_status, i.emp_income<br>
FROM tbl_employee e<br>
INNER JOIN tbl_income i ON e.emp_code = i.emp_code<br>
ORDER BY i.emp_income +0 DESC;<br><br>

#Automation script task<br>
Environtment: Selenium webdriver with python<br><br>

how to run: <br>
1. Pull/clone repository<br>
2. Open terminal in SiCepat-Test/selenium-ui folder<br>
3. type "py testing.py" (without the "")<br><br>

#Karate API Test task<br>
Environtment: Karate<br><br>

how to run:<br>
1. Pull/clone repository<br>
2. Open SiCepat-Test/karate-api on your java environtments debugger, I am using VSCode<br>
3. Click/choose api.feature<br>
4. Click "Run" codelens<br>
5. Test will run and the report.html will created automatically<br><br>


Run video included<br>
Credit: Faizal Ramadhan Suyitno Putra

