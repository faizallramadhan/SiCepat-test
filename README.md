# SiCepat-test

#SQL Query task
a) Buat query jika mencari employee name dan status employee?
answer:

SELECT emp_name, emp_status
FROM tbl_employee 

b) Buat query untuk menampilkan nama employee yang statusnya resign berserta gaji yang diperoleh?
answer:

SELECT e.emp_name, i.emp_income
FROM tbl_employee e
INNER JOIN tbl_income i ON e.emp_code = i.emp_code
WHERE e.emp_status = 'R';

c) Buat query untuk menampilkan emp_code, nama, status, income dan sorting berdasarkan income 
paling besar?
answer:

SELECT e.emp_code, e.emp_name, e.emp_status, i.emp_income
FROM tbl_employee e
INNER JOIN tbl_income i ON e.emp_code = i.emp_code
ORDER BY i.emp_income DESC;

#Automation script task
Environtment: Selenium webdriver with python

how to run: 
1. Pull/clone repository
2. Open terminal in SiCepat-Test/selenium-ui folder
3. type "py testing.py" (without the "")

#Karate API Test task
Environtment: Karate

how to run:
1. Pull/clone repository
2. Open SiCepat-Test/karate-api on your java environtments debugger, I'm using VSCode
3. Click/choose api.feature
4. Click "Run" codelens


Credit: Faizal Ramadhan Suyitno Putra

