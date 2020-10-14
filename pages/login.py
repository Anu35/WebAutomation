class Login():
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Login()
        return cls.instance

    def __init__(self):
        self.driver = Login.get_driver()

    def verify_Dexcom(self):
        
         DexcomHome = self.driver.find_element_by_xpath('//a[contains(text(),'Dexcom CLARITY for Home Users')]')
         DexcomHome.click()
         print('Verify click on HomePage')

    def verify_Login(self, Username , Password):
        
         Username = self.driver.find_element_by_xpath('//input[@id='username']').text
         assert row in status, "{} not present in status component".format(Username)
         Password = self.driver.find_element_by_xpath('//input[@id='password']').text
         assert row in status, "{} not present in status component".format(Password)
         
         
   def verify_Click(self):
         
         Login = self.driver.find_element_by_xpath('//*[@id="edit-actions"]/input')
         Login.click()
         print('Click on Login button ..')

  


login = Login.get_instance()
