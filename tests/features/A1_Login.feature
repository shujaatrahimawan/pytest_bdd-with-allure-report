Feature: A1) Login Feature

  @SearchHotel
  Scenario Outline: A) Login in Website
    Given Open Website with "https://adactinhotelapp.com/"
    When the user enter "<username>" with "LoginEmailField"
    When the user enter "<password>" with "LoginPasswordField"
    When the user click on "LoginSubmitButton"
    Examples:
      | username            | password  | toast                               |
      |shujaatrahim         | 85333W    | Welcome to Adactin Group of Hotels  |
      