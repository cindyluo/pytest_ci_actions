# pytest_ci_actions

### How to run docker images

```bash
$ docker run {docker_image} test "--env staging"
============================= test session starts ==============================
platform linux -- Python 3.9.16, pytest-7.2.1, pluggy-1.0.0
rootdir: /app
collected 1 item

tests/test_first.py .                                                    [100%]

============================== 1 passed in 0.02s ===============================
```
