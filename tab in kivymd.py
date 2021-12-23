from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.tab import MDTabsBase
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.lang import Builder
KV = '''	
MDTabs:
	id:hello_tabs
	tab_hint_x:True
	Tab:
		title:"MESSAGE"
		MDLabel:
			text:"MESSAGE"
			halign:"center"
	Tab:
		title:"STATUS"
		MDLabel:
			text:"STATUS"
			halign:"center"
	Tab:
		title:"CALLS"
		MDLabel:
			text:"CALLS"
			halign:"center"
	
'''
class Tab(MDFloatLayout,MDTabsBase):
	pass
class Test(MDApp):
	def build(self):
		return Builder.load_string(KV)
Test().run()