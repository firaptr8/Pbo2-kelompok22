# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyDialog1
###########################################################################

class MyDialog1 ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Registrasi Akun", pos = wx.DefaultPosition, size = wx.Size( 339,343 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Email", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		fgSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.txtEmail = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer1.Add( self.txtEmail, 0, wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		fgSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.txtUsername = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer1.Add( self.txtUsername, 0, wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Nama Depan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		fgSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.txtDepan = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer1.Add( self.txtDepan, 0, wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Nama Belakang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		fgSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.txtBelakang = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer1.Add( self.txtBelakang, 0, wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Jenis Kelamin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		fgSizer1.Add( self.m_staticText5, 0, wx.ALL, 5 )

		comboKelaminChoices = [ u"laki-laki", u"perempuan" ]
		self.comboKelamin = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,-1 ), comboKelaminChoices, 0 )
		self.comboKelamin.SetSelection( 0 )
		fgSizer1.Add( self.comboKelamin, 0, wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		fgSizer1.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.txtPassword = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer1.Add( self.txtPassword, 0, wx.ALL, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"No Telepon", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		fgSizer1.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.txtNo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer1.Add( self.txtNo, 0, wx.ALL, 5 )


		fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Daftar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_button1, 0, wx.ALL, 5 )


		self.SetSizer( fgSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.onDaftar )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def onDaftar( self, event ):
		event.Skip()


###########################################################################
## Class MyDialog2
###########################################################################

class MyDialog2 ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Login", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		fgSizer2.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.txtUsername = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.txtUsername, 0, wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		fgSizer2.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.txtPassword = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.txtPassword, 0, wx.ALL, 5 )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"Register", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_button4, 0, wx.ALL, 5 )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_button7, 0, wx.ALL, 5 )


		self.SetSizer( fgSizer2 )
		self.Layout()
		fgSizer2.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button4.Bind( wx.EVT_BUTTON, self.onRegister )
		self.m_button7.Bind( wx.EVT_BUTTON, self.onLogin )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def onRegister( self, event ):
		event.Skip()

	def onLogin( self, event ):
		event.Skip()


