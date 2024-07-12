## Installation
Install Python in Operating System
Install Allure in Operating System from the Allure Website
When Open project in VS code or any IDE ( MUST HAVE TO CREATE VIRTUAL ENVIRONMENT )
Once You created the VIRTUAL ENVIRONMENT Install requirement.txt by using command 
command: pip install requirement.txt


## Running Tests
Run tests simply using the `pytest` command.
Depending upon your environment, it may be better to use `python -m pytest`.
If you are using `pipenv`, then run `pipenv run python -m pytest`.
Use the "-k" option to filter tests by tags.



## Before Running all Pytest 
command: `allure generate`

## Run Pytest with Tag and Get Allure Report
command: `pytest -m "sanity" --alluredir=allure-report/`
detail:  `pytest -m "[tag name]"        --alluredir=[directory where you want allure reports]`

## View Allure Report in Browser
command: `allure serve allure-report/`
detail:  `allure serve [directory where you have allure reports]`

## Run Pytest with Tags Only
command: `pytest -m "sanity"`
detail:  `pytest -m "[tag name]" 



## Run Pytest Combine Command
command: rmdir .\allure-report\;allure generate; pytest -m "sanity" --alluredir=allure-report/ ;  allure serve allure-report/

## Help Text Keys (This codes can be used in selenium send text method)

    NULL = '\ue000'
    CANCEL = '\ue001'  # ^break
    HELP = '\ue002'
    BACKSPACE = '\ue003'
    BACK_SPACE = BACKSPACE
    TAB = '\ue004'
    CLEAR = '\ue005'
    RETURN = '\ue006'
    ENTER = '\ue007'
    SHIFT = '\ue008'
    LEFT_SHIFT = SHIFT
    CONTROL = '\ue009'
    LEFT_CONTROL = CONTROL
    ALT = '\ue00a'
    LEFT_ALT = ALT
    PAUSE = '\ue00b'
    ESCAPE = '\ue00c'
    SPACE = '\ue00d'
    PAGE_UP = '\ue00e'
    PAGE_DOWN = '\ue00f'
    END = '\ue010'
    HOME = '\ue011'
    LEFT = '\ue012'
    ARROW_LEFT = LEFT
    UP = '\ue013'
    ARROW_UP = UP
    RIGHT = '\ue014'
    ARROW_RIGHT = RIGHT
    DOWN = '\ue015'
    ARROW_DOWN = DOWN
    INSERT = '\ue016'
    DELETE = '\ue017'
    SEMICOLON = '\ue018'
    EQUALS = '\ue019'

    NUMPAD0 = '\ue01a'  # number pad keys
    NUMPAD1 = '\ue01b'
    NUMPAD2 = '\ue01c'
    NUMPAD3 = '\ue01d'
    NUMPAD4 = '\ue01e'
    NUMPAD5 = '\ue01f'
    NUMPAD6 = '\ue020'
    NUMPAD7 = '\ue021'
    NUMPAD8 = '\ue022'
    NUMPAD9 = '\ue023'
    MULTIPLY = '\ue024'
    ADD = '\ue025'
    SEPARATOR = '\ue026'
    SUBTRACT = '\ue027'
    DECIMAL = '\ue028'
    DIVIDE = '\ue029'

    F1 = '\ue031'  # function  keys
    F2 = '\ue032'
    F3 = '\ue033'
    F4 = '\ue034'
    F5 = '\ue035'
    F6 = '\ue036'
    F7 = '\ue037'
    F8 = '\ue038'
    F9 = '\ue039'
    F10 = '\ue03a'
    F11 = '\ue03b'
    F12 = '\ue03c'

    META = '\ue03d'
    COMMAND = '\ue03d'
    ZENKAKU_HANKAKU = '\ue040'
