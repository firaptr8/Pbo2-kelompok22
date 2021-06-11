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
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"JalanKuy!", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 51, 73, 74 ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel1 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel1.SetBackgroundColour( wx.Colour( 77, 126, 134 ) )

		self.m_notebook1.AddPage( self.m_panel1, u"Home", False )

		bSizer1.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Lihat Daftar Tiket", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button1.SetBackgroundColour( wx.Colour( 140, 184, 189 ) )

		bSizer1.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_panel1.Bind( wx.EVT_PAINT, self.m_panel1OnPaint )
		self.m_button1.Bind( wx.EVT_BUTTON, self.lihatDaftar )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_panel1OnPaint( self, event ):
		event.Skip()

	def lihatDaftar( self, event ):
		event.Skip()


