# Hudl Login Project

This project is an automation test framework designed to test Hudl's front end web application using Selenium, Pytest and Pytest-BDD. The tests are written using the Behavioural Driven Development (BDD) framework.

## Getting Started

### Prerequisites

- Python 3.x.x
- Chrome or Firefox browser
- Valid Hudl accounts setup

### Installation

1. Open terminal and go to the folder you want to install this project.

`cd /<MY_PATH>/`

2. Clone the repository:
   You can this through GitHub -> Click Code or on the terminal below.

   ```
   git clone https://github.com/AO-15/hudl-project.git
   ```

3. Install the required packages:
   ```
    pip install -r requirements.txt
   ```

### File stucture

_Folders:_

- features: Gherkin feature files that define test case scenarios
- locators: Files that identify web elements locators.
- pages: Each file is a representation of the UI interactions of the page. Follows the Page Object Model design pattern.
- reports: Any reports or screenshots generated from the execution of test.
- utils: Helper methods and files like credentials (Temporarily) and selelenium_base.py
- tests: Pytest test scripts.

_Files:_

- conftest.py: Contains pytest fixtures and hooks.
- pytest.ini: Pytest configuration file, for example pytest marker definitions.
- settings.py: Global config settings like environment urls and browser.
- requirements.txt: Required project dependencies.

### How to execute the tests

1.  Go to the project directory.

2.  To run the tests in Chrome:

```
pytest
```

3. To run the tests in Firefox:

```
pytest --browser=firefox
```

4. _Recommended_: To run tests and generate test reports :

```
pytest --html=reports/report.html --self-contained-html
```

OR

```
pytest --browser=chrome --html=reports/report.html --self-contained-html
```

### Test Results

- The test results will be displayed in the terminal.
- If you generated the test report, the HTML report will be inside the "reports" folder.

### Test Structure

The tests are written using Pytest and are located in the tests directory. The conftest.py file contains the fixtures used throughout the tests.

1. The tests are written in the Gherkin Language using BDD inside the `features` folder.
   - They files end with the \*.feature file extension.
   - `features/login_page.feature`
2. Next the step definitions live inside the `tests` folder.

- They are marked with fixture for example:
  In Gherkin:
- `Given I am on the Login Page`
  In test_login.py, the method is given a function decoration like:
- `@given("I am on the Login Page")`

### How to add a test

1. Firstly, create the test inside the feature folder using the Gherkin Language.
2. Inside locators.py, create the class for the page and add the locators
3. Create the page file for it inside the pages folder and add the functionality.
4. Add a news test case inside the tests folder - ensure the file names start with like `test_*.py`
5. Use the login_page fixture to interact with the UI.
6. Ensure the text inside the function decorators match the text inside the `.features` class

### License
This project is licensed under the MIT License.
