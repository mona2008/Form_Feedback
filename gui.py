import wx
import wx.animate

class MainFrame ( wx.Frame ):
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent,id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,400 ), style = wx.TAB_TRAVERSAL )
        self.Centre( wx.BOTH )
    def __del__( self ):
        pass
######################################################################################################################
class panel_zero(wx.Panel):
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,400 ), style = wx.ALIGN_CENTRE)
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        bSizer5 = wx.BoxSizer( wx.VERTICAL )
        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"CODROIDHUB SOCIETY", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        self.m_staticText1.SetFont( wx.Font( 14, 73, 90, 92, False, "Lucida Handwriting" ) )
        bSizer5.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 40 )
        #self.m_animCtrl3 = wx.animate.AnimationCtrl( self, wx.ID_ANY, wx.animate.NullAnimation, wx.DefaultPosition, wx.DefaultSize, wx.animate.AC_DEFAULT_STYLE )
        #self.m_animCtrl3.SetInactiveBitmap( wx.Bitmap( u"code/Feedback.jpg", wx.BITMAP_TYPE_ANY ) )
        #bSizer5.Add( self.m_animCtrl3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"FEEDBACK FORM", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        self.m_staticText3.SetFont( wx.Font( 16, 74, 90, 92, False, "Segoe Script" ) )
        bSizer5.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 20 )
        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"We would appreciate your views and improve ourselves.", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        self.m_staticText4.SetFont( wx.Font( 12, 74, 90, 92, False, "Calibri" ) )
        bSizer5.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 10 )
        self.m_button0 = wx.Button( self, wx.ID_ANY, u"GO", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button0.SetDefault()
        bSizer5.Add( self.m_button0, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        self.SetSizer( bSizer5 )
        self.Layout()
        self.Centre( wx.BOTH )
        self.m_button0.Bind( wx.EVT_BUTTON,self.changeIntroPanel  )
	# Connect Events )
    def __del__( self ):
        pass
    # Virtual event handlers, overide them in your derived class
    def changeIntroPanel( self, event ):
        event.Skip()
######################################################################################################################
class panel_one ( wx.Panel ):
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,400 ), style = wx.ALIGN_CENTRE)
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        bSizer5 = wx.BoxSizer( wx.VERTICAL )
        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"How much you like it?",wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1)
        self.m_staticText4.SetFont( wx.Font( 18, 73, 90, 90, False, "Lucida Handwriting"))
        bSizer5.Add( self.m_staticText4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.LEFT, 50)
        m_radioBox5Choices = [ u"don't like", u"slightly like", u"very much liked"]
        self.m_radioBox5 = wx.RadioBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_radioBox5Choices, 1, wx.RA_SPECIFY_ROWS)
        self.m_radioBox5.SetSelection( 0)
        bSizer5.Add( self.m_radioBox5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.m_button1 = wx.Button( self, wx.ID_ANY, u"NEXT", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button1.SetDefault()
        bSizer5.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.SetSizer( bSizer5)
        self.Layout()
        self.Centre( wx.BOTH )
        self.m_button1.Bind( wx.EVT_BUTTON,self.changeIntroPanel  )
	# Connect Events )
    def __del__( self ):
        pass
    # Virtual event handlers, overide them in your derived class
    def changeIntroPanel( self, event ):
        event.Skip()
###################################################################################################################
class panel_two ( wx.Panel ):
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,400 ), style = wx.ALIGN_CENTRE)
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize)
        bSizer5 = wx.BoxSizer( wx.VERTICAL )
        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Which Andriod project did you like most", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap( -1)
        self.m_staticText3.SetFont( wx.Font( 14, 71, 90, 92, False,"Lucida Handwriting"))
        self.m_staticText3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ))
        bSizer5.Add( self.m_staticText3, 0,wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.LEFT, 50)
        m_radioBox4Choices = [ u"Bus Locator", u"Helping Hand",u"QuizApp",u"Attendance",u"ACE App",u"Medicine Reminder",u"Park Me",u"Online Test"]
        self.m_radioBox4 = wx.RadioBox( self, wx.ID_ANY,wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_radioBox4Choices,2, wx.RA_SPECIFY_ROWS  )
        self.m_radioBox4.SetSelection( 1)
        bSizer5.Add( self.m_radioBox4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.m_button2 = wx.Button( self, wx.ID_ANY, u"NEXT", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.SetSizer( bSizer5)
        self.Layout()
        self.Centre( wx.BOTH )
        self.m_button2.Bind( wx.EVT_BUTTON,self.changeIntroPanel) # Connect Events
    def __del__( self ):
        pass
        # Virtual event handlers, overide them in your derived class
    def changeIntroPanel( self, event ):
        event.Skip()

########################################################################################################################
class panel_three ( wx.Panel ):   
    def __init__(self, parent):
        wx.Panel.__init__(self, parent,id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,400 ), style = wx.ALIGN_CENTRE  )
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
      
        bSizer5 = wx.BoxSizer( wx.VERTICAL )
      
        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"How do u rate our projects?", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
        self.m_staticText1.Wrap( -1 )
        self.m_staticText1.SetFont( wx.Font( 14, 71, 93, 92, False, "Lucida Handwriting" ) )
        self.m_staticText1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT  ) )
        #self.m_staticText1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
      
        bSizer5.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.LEFT, 50 )
      
        m_radioBox2Choices = [ u"agree", u"disagree", u"helpful", u"very helpul", u"okay" ]
        self.m_radioBox2 = wx.RadioBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_radioBox2Choices, 5, wx.RA_SPECIFY_COLS )
        self.m_radioBox2.SetSelection( 1 )
        bSizer5.Add( self.m_radioBox2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_button3 = wx.Button( self, wx.ID_ANY, u"NEXT", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
          
      
      
        self.SetSizer( bSizer5 )
        self.Layout()
      
        self.Centre( wx.BOTH )
        self.m_button3.Bind( wx.EVT_BUTTON, self.changeIntroPanel )
    def __del__( self ):
        pass
    def changeIntroPanel( self, event ):
        event.Skip()

###################################################################################################################
class panel_four(wx.Panel):
       
    def __init__(self, parent):

        """Constructor"""
        wx.Panel.__init__(self, parent,id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,400 ), style = wx.ALIGN_CENTRE  )
        
        bSizer5 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Which Python project did you like most", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        self.m_staticText2.SetFont( wx.Font( 18, 73, 90, 92, False, "Lucida Handwriting" ) )
        self.m_staticText2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT  ) )
        #self.m_staticText2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )
        
        bSizer5.Add( self.m_staticText2, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.LEFT, 50 )
        
        m_radioBox3Choices = [ u"Bulk Mail", u"Digital Board", u"Security System", u"Feedback Form", u"Blog"]
        self.m_radioBox3 = wx.RadioBox( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.DefaultSize, m_radioBox3Choices, 1, wx.RA_SPECIFY_ROWS )
        self.m_radioBox3.SetSelection( 2 )
        self.m_radioBox3.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 71, 90, 90, False, wx.EmptyString ) )
        self.m_radioBox3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )
      
        bSizer5.Add( self.m_radioBox3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_button4 = wx.Button( self, wx.ID_ANY, u"NEXT", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.m_button4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.SetSizer( bSizer5 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        self.m_button4.Bind( wx.EVT_BUTTON, self.changeIntroPanel )

    def __del__( self ):
        pass
    def changeIntroPanel( self, event ):
        event.Skip()
###################################################################################################################
class panel_five(wx.Panel):
       
    def __init__(self, parent):

        """Constructor"""
        wx.Panel.__init__(self, parent,id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,400 ), style = wx.ALIGN_CENTRE  )
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize)
        bSizer5 = wx.BoxSizer( wx.VERTICAL)
        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"How do you rate our Section?", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap( -1)
        self.m_staticText5.SetFont( wx.Font( 14, 73, 90, 90, False, "Lucida Handwriting"))
        bSizer5.Add( self.m_staticText5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.LEFT, 50)
        m_radioBox6Choices = [ u"Very Poor", u"Poor", u"Average", u"Good", u"Excellent"]
        self.m_radioBox6 = wx.RadioBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_radioBox6Choices, 1, wx.RA_SPECIFY_ROWS)
        self.m_radioBox6.SetSelection( 0)
        bSizer5.Add( self.m_radioBox6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.m_button5 = wx.Button( self, wx.ID_ANY, u"SUBMIT", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add( self.m_button5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.SetSizer( bSizer5)
        self.Layout()
        self.Centre( wx.BOTH )
        self.m_button5.Bind( wx.EVT_BUTTON,self.changeIntroPanel )
	
    def __del__( self ):
        pass
    def changeIntroPanel( self, event ):
        event.Skip()
#########################################################################################################################
class panel_six ( wx.Panel ):
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,400 ),style = wx.ALIGN_CENTRE )
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        bSizer5 = wx.BoxSizer( wx.VERTICAL )
        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"THANK YOU FOR VALUABLE FEEDBACK", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap( -1 )
        self.m_staticText2.SetFont( wx.Font( 14, 74, 90, 90, False, "Lucida Handwriting" ) )
        self.m_staticText2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ))
        bSizer5.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 50)
        #m_sdbSizer2 = wx.StdDialogButtonSizer()
        #self.m_sdbSizer2OK = wx.Button( self, wx.ID_OK )
        #m_sdbSizer2.AddButton( self.m_sdbSizer2OK)
        #self.m_sdbSizer2Cancel = wx.Button( self, wx.ID_CANCEL)
        #m_sdbSizer2.AddButton( self.m_sdbSizer2Cancel)
        #m_sdbSizer2.Realize()
        #bSizer5.Add( m_sdbSizer2, 1, wx.EXPAND, 5)
        #self.SetSizer( bSizer5)
        #self.Layout()
        #self.Centre( wx.BOTH)
        #self.m_sdbSizer2OK.Bind( wx.EVT_BUTTON, self.changeIntroPanel )
        self.m_button6 = wx.Button( self, wx.ID_ANY, u"CLOSE", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button6.SetDefault()
        bSizer5.Add( self.m_button6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        self.SetSizer( bSizer5 )
        self.Layout()
        self.Centre( wx.BOTH )
        self.m_button6.Bind( wx.EVT_BUTTON,self.changeIntroPanel  )
    def __del__( self ):
        pass
	# Virtual event handlers, overide them in your derived class
    def changeIntroPanel( self, event ):
        event.Skip()
#########################################################################################################################	
	
	
