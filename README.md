# Test Automation Project

This repository was created for testing the [site](http://selenium1py.pythonanywhere.com).

## HOW TO INSTALL:

### Python version -- 3.8.5


#### 1) Activate your virtual environment:

##### For Mac:
```python
python3 -m venv venv
source venv/bin/activate
```

##### For Windows:
```python
pip install virtualenv
virtualenv venv
venv\Scripts\activate
```


#### 2) Clone the repository to your local machine:

```python
git clone https://github.com/oldevgeny/test-automation-project.git
```


#### 3) Install the requirements:

```python
pip install --upgrade pip
pip install -r requirements.txt
```

## HOW TO USE:


#### 1) Run all tests:

```python
pytest -v --tb=line --language=en
```

#### 2) Run all tests with need_review mark:

```python
pytest -v --tb=line --language=en -m need_review
```

#### 3) Run all tests with need_review mark and language=ru in firefox browser:

```python
pytest -v --tb=line --language=ru --firefox -m need_review
```
