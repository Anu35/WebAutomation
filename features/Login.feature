Feature: Login

Scenario Outline:  login in Application
        Given Go to https://clarity.dexcom.com/
        When Click on the Home Page
        And Enter the <Username> and <Password>
        Then Click on Login Page
        Examples:
            | Username             | Password |
            | nilepatest001        |   Password@1 |
            