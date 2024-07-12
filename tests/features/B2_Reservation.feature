Feature: B2) Hotel Reservation


  @sanity
  Scenario Outline: A) Search Hotel
    Given the default url "https://adactinhotelapp.com/SearchHotel.php"
    When the user select "<location>" on "LocationDropDown"
    When the user select "<hotel>" on "HotelDropDown"
    When the user select "<type>" on "RoomsDropDown"
    When the user select "<no_of_rooms>" on "RoomsNoDropDown"
    When the user click on "SearchButton"
    Examples:
      | location   | hotel        | type        | no_of_rooms   |
      | Sydney     | Hotel Creek  | Standard    | 2             |

  @sanity 
  Scenario Outline: C) Add Reservation
    Given the default url "https://adactinhotelapp.com/BookHotel.php"
    Given the user click on "RadioButtonFirstRecord"
    When the user click on "ContinueButton"
    When the user enter "<firstname>" with "FirstName"
    When the user enter "<lastname>" with "LastName"
    When the user enter "<address>" with "Address"
    When the user enter "<ccNO>" with "CC_Num"
    When the user select "<CC_type>" on "CC_Type"
    Given the user select "<Exp_Month>" on "cc_exp_month"
    When the user select "<Exp_Year>" on "cc_exp_year"
    When the user enter "<cc_cvv>" with "cc_cvv"
    When the user click on "book_now"
    Examples:
      |firstname|lastname|address              |ccNO            |CC_type|Exp_Month|Exp_Year|cc_cvv|
      |Babar    |Bilal   |House#112 ABC Streat |1234567890987654|AMEX   |12       |2022    |222   |
    
    
  @regression
  Scenario Outline: D) Search Multiple Hotels and Add Multiple Reservations
    Given the default url "https://adactinhotelapp.com/SearchHotel.php"
    Given the user select "<location>" on "LocationDropDown"
    When the user select "<hotel>" on "HotelDropDown"
    When the user select "<type>" on "RoomsDropDown"
    When the user select "<no_of_rooms>" on "RoomsNoDropDown"
    When the user click on "SearchButton"
    When the user click on "RadioButtonFirstRecord"
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
    Then the user click on "search_hotel"
    Examples:
      | location     | hotel          | type          | no_of_rooms   |firstname|lastname|address               |ccNO            |CC_type|Exp_Month|Exp_Year|cc_cvv|
      | Sydney       | Hotel Creek    | Standard      | 1             |Babar    |Bilal   |House#112 ABC Street1 |1234567890987654|AMEX   |1        |2025    |122   |
      | Melbourne    | Hotel Sunshine | Double        | 2             |Babar    |Bilal   |House#212 ABC Street2 |1234567890987654|AMEX   |2        |2026    |222   |
      | Brisbane     | Hotel Hervey   | Deluxe        | 3             |Babar    |Bilal   |House#312 ABC Street3 |1234567890987654|AMEX   |3        |2027    |322   |
      | Adelaide     | Hotel Cornice  | Super Deluxe  | 4             |Babar    |Bilal   |House#412 ABC Street4 |1234567890987654|AMEX   |4        |2028    |422   |
      | London       | Hotel Creek    | Standard      | 5             |Babar    |Bilal   |House#512 ABC Street5 |1234567890987654|AMEX   |5        |2029    |522   |
      | New York     | Hotel Sunshine | Double        | 6             |Babar    |Bilal   |House#612 ABC Street6 |1234567890987654|AMEX   |6        |2030    |622   |
      | Los Angeles  | Hotel Cornice  | Deluxe        | 7             |Babar    |Bilal   |House#712 ABC Street7 |1234567890987654|AMEX   |7        |2030    |722   |
      | Paris        | Hotel Hervey   | Super Deluxe  | 8             |Babar    |Bilal   |House#812 ABC Street8 |1234567890987654|AMEX   |8        |2030    |822   |