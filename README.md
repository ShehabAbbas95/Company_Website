# MY FINAL PROJECT
- What does it do?  
  * It's a company website shows a landing page that introduces the company 
  * The company has it's own shop for thier employees (This should only for the registered employees that added by the admins but for testing, any one can register and login)

- What is the "new feature" which you have implemented that we haven't seen before?  
    * The user is allowed to select products from the shop and his products appear in his cart
## Prerequisites
    * flask_login
    * flask_sqlalchemy
    * flask_bcrypt
## Project Checklist
- [x] It is available on GitHub.
- [x] It uses the Flask web framework.
- [x] It uses at least one module from the Python Standard Library other than the random module.
  - Module name: datetime
- [x] It contains at least one class written by you that has both properties and methods. This includes instantiating the class and using the methods in your app. Please provide below the file name and the line number(s) of at least one example of a class definition in your code as well as the names of two properties and two methods.
  - File name: remote_coders.py (the class is imported from User.py file)
  - Line number(s): 67
  - Name of two properties: id, username, email, password, mobile
  - Name of two methods: update_email, update_username
- [x] It makes use of JavaScript in the front end and uses the localStorage of the web browser.
- [x] It uses modern JavaScript (for example, let and const rather than var).
- [x] It makes use of the reading and writing to a file feature.
- [x] It contains conditional statements. Please provide below the file name and the line number(s) of at least
  one example of a conditional statement in your code.
  - File name: remote_coders.py
  - Line number(s): 94 
- [x] It contains loops. Please provide below the file name and the line number(s) of at least
  one example of a loop in your code.
  - File name: remote_coders.py
  - Line number(s): 256
- [x] It lets the user enter a value in a text box at some point.
  This value is received and processed by your back end Python code.
- [x] It doesn't generate any error message even if the user enters a wrong input.
- [x] The code follows the code and style conventions as introduced in the course, is fully documented using comments and doesn't contain unused or experimental code. 
  In particular, the code should not use `print()` or `console.log()` for any information the app user should see. Instead, all user feedback needs to be visible in the browser.  
- [x] All exercises have been completed as per the requirements and pushed to the respective GitHub repository.

## Testing Intruction:
- For testing the Product class functions user should be admin, so please login with the following credentials
- Email: admin@gmail.com  Pass: admin123
- If you intialized a new database please sign up with the above credentials for the admin