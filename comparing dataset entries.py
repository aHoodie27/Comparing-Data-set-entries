Python 3.10.4 (v3.10.4:9d38120e33, Mar 23 2022, 17:29:05) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
id_1 = "#4"
average_grade_1 = "A"
test_score_1 = 90

id_2 = "#5"
average_grade_1 = "A"
test_score_2 = 70

No_duplicates = id_1 != id_2
print("no duplicate entries:")
no duplicate entries:
print(no_duplicates)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(no_duplicates)
NameError: name 'no_duplicates' is not defined. Did you mean: 'No_duplicates'?
print(No_duplicates)
True
higher_score = test_score_1 > test_score_2
print(“id_1 has higher score:”)
SyntaxError: invalid character '“' (U+201C)
print("id_1 has higher score:”)
      
SyntaxError: unterminated string literal (detected at line 1)
print("id_1 has higher score:")
      
id_1 has higher score:
print(higher_score)
      
True
