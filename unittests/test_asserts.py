import imp_unittest, unittest
import wtc
import wx

#---------------------------------------------------------------------------

class asserts_Tests(wtc.WidgetTestCase):

    def test_asserts1(self):
        wx.PyAssertionError
        wx.APP_ASSERT_SUPPRESS
        wx.APP_ASSERT_EXCEPTION
        wx.APP_ASSERT_DIALOG
        wx.APP_ASSERT_LOG


    def test_asserts2(self):
        # check default mode
        self.assertTrue(wx.GetApp().GetAssertMode() == wx.APP_ASSERT_EXCEPTION)

        # attempting to convert an invalid bitmap to an image is an easy way
        # to trigger an assert
        with self.assertRaises(wx.PyAssertionError):
            wx.NullBitmap.ConvertToImage()


    def test_asserts3(self):
        # test that assertions can be ignored...
        wx.GetApp().SetAssertMode(wx.APP_ASSERT_SUPPRESS)
        wx.NullBitmap.ConvertToImage()

        # ...and then turned back on
        wx.GetApp().SetAssertMode(wx.APP_ASSERT_EXCEPTION)
        with self.assertRaises(wx.PyAssertionError):
            wx.NullBitmap.ConvertToImage()
        
        
#---------------------------------------------------------------------------


if __name__ == '__main__':
    unittest.main()
