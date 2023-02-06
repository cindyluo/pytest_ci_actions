# pytest_ci_actions

### How to run docker images

```bash
$ docker run --env ENV=production {docker image} test
============================= test session starts ==============================
platform linux -- Python 3.9.16, pytest-7.2.1, pluggy-1.0.0
rootdir: /app
collected 2 items

tests/test_first.py ..                                                   [100%]

============================== 2 passed in 0.04s ===============================
```
