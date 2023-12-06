import unittest
from authHelpers import login
import chatbot

class testAuthentication(unittest.TestCase):
    def testAuth(self):
        self.assertTrue(login("foobar@grr.la", "password"))

        self.assertFalse(login("false@grr.la", "password"))
        self.assertFalse(login("foobargrr.la", "password"))
        self.assertFalse(login("foobar", "password"))
        self.assertFalse(login("false@grr.la", "word"))
        self.assertFalse(login("false@grr.la", ""))
        self.assertFalse(login("", "password"))
        self.assertFalse(login("",""))

class testChatbot(unittest.TestCase):
    def testChatbotInit(self):
        Foobar = chatbot.Persona("FooBar", "You are a chatbot that will only say FooBar. Nothing else.", [])

        self.assertIsInstance(Foobar, chatbot)
        self.assertEquals(type(Foobar.getMessageHistory()), list)
        self.assertEquals(type(Foobar.filteredMessageHistory, list))
        self.assertNotEqual(Foobar.getMessagehistory(), Foobar.filteredMessageHistory())

    def testChatResponse(self):
        BarFoo = chatbot.Persona("FooBar", "You are a chatbot that will only say BarFoo. Nothing else.", [])

        self.assertEquals(type(BarFoo.prompt("Testing")), str)
        self.assertEquals(type(BarFoo.prompt("")), str)

if __name__ == "__unitTest__":
    unittest.main()