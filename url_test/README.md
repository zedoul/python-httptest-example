RESTful API Testing
===================

How to use
----------

```
    $ run.sh
```

Installation on Mac
-------------------

1. pytest

    ```
    $ pip install -U pytest
    ```

    To check your installation has installed the correct version

    ```
    $ py.test --version
    This is pytest version 2.8.2, imported from $PYTHON_PREFIX/lib/python3.4/site-packages/pytest.py
    ```

2. requests

    ```
    pip install requests
    ```

Test cases 
----------

- conftest.py : Basic HTTP Requests test - connection errors test.
- test_request.py : Basic HTTP Requests test - header validation.
- test_api.py : Contents validation

Removed test cases
----------

* 95-96 lines of app.yaml are commented out
* 114-115 lines of app.yaml are commented out
* 31-33 lines of test_api.py are commented out.

Limitation
----------

1. Although I asked several questions to know API specification, but 
there are still many holes in the test cases. For example, we may be 
able to find a better way to check ``content_length_threshold``.

2. It may not work well for the bunch of requests, this scenario is 
covered by load testing.
