from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
Builder.load_string(
    """
<List>:
	MDBoxLayout:
		orientation:"vertical"
		GridLayout:
			cols:1
			MDList:
			    OneLineListItem:
			    	text:"Hello akivymd"
			    	divider:None
			    OneLineListItem:
			    	text:"Hello kivymd"
			    	divider:None
			    OneLineListItem:
			    	text:"Hello kivy"
			    	divider:None
		    
		    
"""
)


class List(MDScreen):
    pass

class Test(MDApp):
    def build(self):
        return List()
Test().run()