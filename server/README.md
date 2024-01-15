# Damion server v0.1.0
Damion is a Checker game for two players. This server project will allow you to serve the client project <br>
<a href="https://github.com/Lazare-Nogrette/damion/tree/main/client">Damion client </a>.

<a href="https://sodular.agglomy.com/lite.html#py_doc" target="_blank"><img src="doc/assets/img/sodulite-logo.png"></a>

## Get Started 
### 0. Clone the project 
If you didn't clone already:
Windows : ``git clone https://github.com/Lazare-Nogrette/damion.git`` <br>
  ### 0.1 Software 
  Requirements: <a href="https://www.python.org/downloads/">Python</a> should be installed
  ### 0.2 Project structure for server side
  ```
  server/
  |-- src/
  |   |-- config/
  |   |   |-- conf.py
  |   |-- model/
  |   |   |-- board.py
  |   |   |-- game.py
  |   |   |-- pieace.py
  |   |-- controller/
  |   |   |-- api.py
  |   |-- main.py
  |-- requirements.txt

  ```

### 1. Setup a virtual env
```
cd damion/server
python -m venv environment_name.
```
Powsershell:`.\environment_name\Scripts\activate`
### 2. Install requirements for the project
```
pip install -r requirements.txt 
```
### 3. Launch the server
```
python src/main.py.
```
### 4. Preview
<img src="doc/assets/img/server-running.png" alt="image of the running server">

## Todo
- Removing/Reduce some unusual dependencies,functions, refactoring paths/files...
- Code Cleaning/ Making a suitable project structure with modular pattern (DRY and KISS dev).

## Join US
If you have any suggestion, contribution, feature to add ...etc
- Discord(Support Team, FAQ, Chat): 

## Contributors
- Hetic Team :
    - Ivan Joel Sobgui
    - Lazare
    - Valentin
## Licence

MIT: You can use it for educational/personal/business purpose!