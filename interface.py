# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 754,454 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button2 = wx.Button( self.m_panel1, wx.ID_ANY, u"Pesan", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button2, 0, wx.ALL, 5 )

		self.m_button3 = wx.Button( self.m_panel1, wx.ID_ANY, u"Upload Bukti Bayar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button3, 0, wx.ALL, 5 )


		bSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer2.Add( bSizer3, 1, wx.EXPAND, 5 )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.tabeltiket = wx.grid.Grid( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 720,380 ), 0 )

		# Grid
		self.tabeltiket.CreateGrid( 10, 4 )
		self.tabeltiket.EnableEditing( True )
		self.tabeltiket.EnableGridLines( True )
		self.tabeltiket.EnableDragGridSize( False )
		self.tabeltiket.SetMargins( 0, 0 )

		# Columns
		self.tabeltiket.SetColSize( 0, 250 )
		self.tabeltiket.SetColSize( 1, 70 )
		self.tabeltiket.SetColSize( 2, 250 )
		self.tabeltiket.SetColSize( 3, 80 )
		self.tabeltiket.EnableDragColMove( False )
		self.tabeltiket.EnableDragColSize( True )
		self.tabeltiket.SetColLabelSize( 30 )
		self.tabeltiket.SetColLabelValue( 0, u"Nama Wisata" )
		self.tabeltiket.SetColLabelValue( 1, u"Harga" )
		self.tabeltiket.SetColLabelValue( 2, u"Lokasi" )
		self.tabeltiket.SetColLabelValue( 3, u"Stok" )
		self.tabeltiket.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabeltiket.AutoSizeRows()
		self.tabeltiket.EnableDragRowSize( True )
		self.tabeltiket.SetRowLabelSize( 80 )
		self.tabeltiket.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tabeltiket.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer2.Add( self.tabeltiket, 0, wx.ALL, 5 )


		bSizer2.Add( fgSizer2, 1, wx.EXPAND, 5 )


		self.m_panel1.SetSizer( bSizer2 )
		self.m_panel1.Layout()
		bSizer2.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button2.Bind( wx.EVT_BUTTON, self.OnPesan )
		self.m_button3.Bind( wx.EVT_BUTTON, self.OnUpload )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnPesan( self, event ):
		event.Skip()

	def OnUpload( self, event ):
		event.Skip()


###########################################################################
## Class MyDialog2
###########################################################################

class MyDialog2 ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Pesan Tiket", pos = wx.DefaultPosition, size = wx.Size( 408,340 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Email", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		fgSizer3.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.txtEmail = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer3.Add( self.txtEmail, 0, wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Nama Lengkap", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		fgSizer3.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.txtNama = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer3.Add( self.txtNama, 0, wx.ALL, 5 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Alamat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		fgSizer3.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.txtAlamat = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer3.Add( self.txtAlamat, 0, wx.ALL, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Tempat Wisata", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		fgSizer3.Add( self.m_staticText12, 0, wx.ALL, 5 )

		comboWisataChoices = [ u"Kebun Botani", u"Mumbul Garden", u"Perkebunan Teh Gunung Gambir", u"Wisata Agro Glantangan", u"Taman Galaxy", u"Dira Park", u"Taman Nasional Meru Betiri", u"Tiara Jember Park Waterboom", u"Kawasan Puncak Dan Pemandian Rembangan", u"Pemandian Kebon Agung" ]
		self.comboWisata = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboWisataChoices, 0 )
		self.comboWisata.SetSelection( 0 )
		fgSizer3.Add( self.comboWisata, 0, wx.ALL, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Jumlah Tiket", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		fgSizer3.Add( self.m_staticText13, 0, wx.ALL, 5 )

		self.txtJmlTiket = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer3.Add( self.txtJmlTiket, 0, wx.ALL, 5 )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Tanggal Kunjungan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		fgSizer3.Add( self.m_staticText14, 0, wx.ALL, 5 )

		self.txtTgl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer3.Add( self.txtTgl, 0, wx.ALL, 5 )


		fgSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.Pesan = wx.Button( self, wx.ID_ANY, u"Pesan", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.Pesan, 0, wx.ALL, 5 )


		self.SetSizer( fgSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Pesan.Bind( wx.EVT_BUTTON, self.OnKlikPesan )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnKlikPesan( self, event ):
		event.Skip()


