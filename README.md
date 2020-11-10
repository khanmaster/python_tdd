# TDD Test Driven Development 
## Type of testing
- unit testing
- TDD

### Python has several modules that we can use 
to test our code
- pytest
- unittest

**Why TDD**
- TDD helps us minimise the risk of failure before sending the product to production 

**steps**
- we will create a file to write our tests
- we will run the test they will all fail
- we will create a file to write our code
- we will refactor and add the code to pass the tests

**Naming convention for test files and methods**
- file name simple_calc
- test_simple_calc
 
** install the testing frameworks**

```python
pip install pytest
```

- How does ```pytest``` work

- pytest looks for the files with ``` test_*.py``` and ```_test*.py```
- ```-v``` is vor verbose flag

- We can use different condition with assertEqual as per business need
