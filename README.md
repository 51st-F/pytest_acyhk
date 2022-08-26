# pytest_acyhk

Using selenium to run register form under pytest framework.
There are mainly two function under this repo:
1. Test url's connection
2. Test after auto-filled step1 whether can click the next button

Future optimize part
1. Use pytest-xdist to run parallel test.
2. Use different brower and different version to run the test.
3. Creat a conftest.py and put all fixture in it.
4. Creat class level due to different test condition.
5. Check whether input warning match the error condition.
6. Check whether after country select match the auto-filled in phone district.

Follow steps bellow to run the test:
1. git clone https://github.com/51st-F/pytest_acyhk.git
2. cd pytest_acyhk
3. pipenv shell
4. pipenv install
5. pytest -v