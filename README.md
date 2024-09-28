# Assignment_2_hidden_tests
This repository houses the hidden test cases for assignment 2 - CSYE6225

## Overview

This repository contains unit and end-to-end (E2E) tests for verifying the functionality of an inventory management system. The test cases are divided across four directories, each with its own set of tests and corresponding documentation.

## Repository Structure

The repository is organized into four main directories:

1. **hidden_unit_test_1**
2. **hidden_unit_test_2**
3. **hidden_e2e_test_1**
4. **hidden_e2e_test_2**

Each directory focuses on specific aspects of the system's functionality, covering different types of tests and scenarios.

### Directory Details

1. **hidden_unit_test_1**
    - Contains `unit_test.py`, which has a negative test case for delete_data API, to delete a non existent snapshot.
    - A `README.md` file in this directory explains the test case.

2. **hidden_unit_test_2**
    - Contains `unit_test.py`, which has a negative test case for load_data API, to load a non existent snapshot.
    - A `README.md` file in this directory explains the test case.

3. **hidden_e2e_test_1**
    - Contains `e2e_test.py`, which includes end-to-end test to test all the APIs together including save_data, load_data and delete_data. This will add a new type, give a count, then removes count and undefines it and performs validations.
    - A `README.md` is provided to explain the test in detail and the expected outcomes.

4. **hidden_e2e_test_2**
    - Contains `e2e_test.py`, which includes end-to-end test to test all the APIs together including save_data, load_data and delete_data including multiple snapshots. This test will create snapshots at multiple points of time and verifies the count and existence of types.
    - A `README.md` is provided to explain the test in detail and the expected outcomes.


## Note
The assert repsonses have been modified during the testing to ensure that the message matches the server response according to each repository.

