from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

quiz_data = [
  {"question": "1. Which keyword is used to define a function in Python?", "options": ["function", "fun", "def", "define"], "answer": "def"},
  {"question": "2. Which of the following correctly calls a function named greet?", "options": ["call greet", "greet", "greet()", "def greet()"], "answer": "greet()"},
  {"question": "3. What will print() return?", "options": ["None", "0", "''", "print"], "answer": "None"},
  {"question": "4. Which statement exits a function and returns a value?", "options": ["exit", "return", "stop", "break"], "answer": "return"},
  {"question": "5. If a function has no return statement, it returns:", "options": ["0", "False", "None", "Null"], "answer": "None"},
  {"question": "6. What is passed inside the parentheses of a function?", "options": ["Arguments", "Return values", "Variables", "Conditions"], "answer": "Arguments"},
  {"question": "7. How many arguments can a Python function have?", "options": ["Only 2", "10", "As many as needed", "1"], "answer": "As many as needed"},
  {"question": "8. Default argument value is used when:", "options": ["Argument is missing", "Value is zero", "Function ends", "Loop breaks"], "answer": "Argument is missing"},
  {"question": "9. Which is correct syntax for default value?", "options": ["def add(a=5,b):", "def add(a,b=5):", "def add(a=5,b=2):", "def add(a b=5):"], "answer": "def add(a,b=5):"},
  {"question": "10. What is output of show(3) if show(x, y=2): return x*y?", "options": ["3", "2", "6", "5"], "answer": "6"},
  {"question": "11. What does return do in Python?", "options": ["Stops loop", "Returns value", "Prints output", "Pauses code"], "answer": "Returns value"},
  {"question": "12. What happens after return statement?", "options": ["Continues execution", "Stops function", "Starts loop", "Skips return"], "answer": "Stops function"},
  {"question": "13. Can a function return multiple values?", "options": ["Yes", "No", "Only integers", "Only strings"], "answer": "Yes"},
  {"question": "14. What type is returned by return 10,20?", "options": ["List", "Tuple", "Dict", "Set"], "answer": "Tuple"},
  {"question": "15. If a function returns nothing, its return type is:", "options": ["String", "NoneType", "Integer", "Void"], "answer": "NoneType"},
  {"question": "16. Variables defined inside a function are:", "options": ["Global", "Static", "Local", "External"], "answer": "Local"},
  {"question": "17. Keyword for accessing global variable?", "options": ["world", "main", "global", "extern"], "answer": "global"},
  {"question": "18. Output of local and global x print?", "options": ["10 10", "5 10", "10 5", "5 5"], "answer": "5 10"},
  {"question": "19. Output of func(5) if func(a): return a+1?", "options": ["4", "5", "6", "Error"], "answer": "6"},
  {"question": "20. Can a function modify global variable without keyword?", "options": ["Yes", "No", "Sometimes", "Only constants"], "answer": "No"},
  {"question": "21. Function without return is:", "options": ["Void", "Lambda", "Recursive", "Local"], "answer": "Void"},
  {"question": "22. Function inside another function is:", "options": ["Nested", "Inner", "Recursive", "Hidden"], "answer": "Nested"},
  {"question": "23. Anonymous function keyword:", "options": ["def", "lambda", "anon", "func"], "answer": "lambda"},
  {"question": "24. Output of square(3) if square=lambda x:x*x?", "options": ["3", "6", "9", "Error"], "answer": "9"},
  {"question": "25. A function that calls itself is:", "options": ["Loop", "Recursive", "Inner", "Lambda"], "answer": "Recursive"},
  {"question": "26. Function with only print returns:", "options": ["0", "None", "Print", "Error"], "answer": "None"},
  {"question": "27. Correct function definition:", "options": ["function f()", "def f():", "func f():", "define f():"], "answer": "def f():"},
  {"question": "28. Output of print(f)?", "options": ["Hi", "<function f>", "None", "Error"], "answer": "<function f>"},
  {"question": "29. Output of print(f()) if f(): print('Hi')?", "options": ["Hi", "Hi None", "None", "Error"], "answer": "Hi None"},
  {"question": "30. type(f) returns:", "options": ["Object", "Function", "String", "Int"], "answer": "Function"},
  {"question": "31. *args is used to:", "options": ["Pass fixed args", "Pass variable args", "Pass keywords", "Return list"], "answer": "Pass variable args"},
  {"question": "32. **kwargs stands for:", "options": ["Keyword Arguments", "Key Arguments", "Kwarg loop", "KeyWords"], "answer": "Keyword Arguments"},
  {"question": "33. len(args) for show(1,2,3)?", "options": ["1", "2", "3", "Error"], "answer": "3"},
  {"question": "34. show(name='Subhani') returns:", "options": ["Subhani", "Error", "None", "Data"], "answer": "Subhani"},
  {"question": "35. Invalid syntax:", "options": ["def f(a,b=2):", "def f(a=1,b=2):", "def f(a=2,b):", "def f(a,b):"], "answer": "def f(a=2,b):"},
  {"question": "36. Base case in recursion is used to:", "options": ["Stop recursion", "Start recursion", "Print result", "None"], "answer": "Stop recursion"},
  {"question": "37. No base case causes:", "options": ["Infinite recursion", "Stop", "Skip", "Error only once"], "answer": "Infinite recursion"},
  {"question": "38. fact(3) returns:", "options": ["3", "5", "6", "9"], "answer": "6"},
  {"question": "39. Default recursion limit:", "options": ["100", "500", "1000", "Unlimited"], "answer": "1000"},
  {"question": "40. Function that returns itself:", "options": ["Recursive", "Lambda", "Static", "Return"], "answer": "Recursive"},
  {"question": "41. add('2','3') returns:", "options": ["5", "23", "Error", "None"], "answer": "23"},
  {"question": "42. test(b=2,a=1) prints:", "options": ["2 1", "1 2", "Error", "None"], "answer": "1 2"},
  {"question": "43. Nested functions allowed?", "options": ["Yes", "No", "Only global", "Only once"], "answer": "Yes"},
  {"question": "44. Function name stored in variable?", "options": ["Yes", "No", "Only strings", "Only numbers"], "answer": "Yes"},
  {"question": "45. id(func) returns:", "options": ["Memory address", "Function name", "Value", "Location"], "answer": "Memory address"},
  {"question": "46. test() with pass returns:", "options": ["0", "None", "Empty", "Skip"], "answer": "None"},
  {"question": "47. Can function be argument to another?", "options": ["Yes", "No", "Sometimes", "Only in class"], "answer": "Yes"},
  {"question": "48. Function names case-sensitive?", "options": ["Yes", "No", "Optional", "Sometimes"], "answer": "Yes"},
  {"question": "49. A function can return:", "options": ["One value", "Many values", "Only string", "Nothing"], "answer": "Many values"},
  {"question": "50. Invalid function name:", "options": ["my_func", "_func", "123func", "func_1"], "answer": "123func"}
   ]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-quiz')
def get_quiz():
    return jsonify(quiz_data)

if __name__ == '__main__':
    app.run(debug=True)
