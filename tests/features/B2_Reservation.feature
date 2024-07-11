@web
Feature: B2) Hotel Reservation


  @SearchHotel2
  Scenario Outline: A) Search Hotel
    When the user select "<location>" on "LocationDropDown"
    When the user select "<hotel>" on "HotelDropDown"
    When the user select "<type>" on "RoomsDropDown"
    When the user select "<no_of_rooms>" on "RoomsNoDropDown"
    When the user click on "SearchButton"
    Examples:
      | location   | hotel        | type        | no_of_rooms   |
      | Sydney     | Hotel Creek  | Standard    | 2             |

  @SearchHotel2
  Scenario Outline: C) Add Reservation
    Given the user click on "RadioButtonFirstRecord"
    When the user click on "ContinueButton"
    When the user enter "<firstname>" with "FirstName"
    When the user enter "<lastname>" with "LastName"
    When the user enter "<address>" with "Address"
    When the user enter "<ccNO>" with "CC_Num"
    When the user select "<CC_type>" on "CC_Type"
    When the user select "<Exp_Month>" on "cc_exp_month"
    When the user select "<Exp_Year>" on "cc_exp_year"
    When the user enter "<cc_cvv>" with "cc_cvv"
    When the user click on "book_now"
    Examples:
      |firstname|lastname|address              |ccNO            |CC_type|Exp_Month|Exp_Year|cc_cvv|
      |Babar    |Bilal   |House#112 ABC Streat |1234567890987654|AMEX   |12       |2022    |222   |
