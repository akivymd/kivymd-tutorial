from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
<MDIconTooltip@MDIconButton+MDTooltip>
MDScreen:
	MDBoxLayout:
		orientation:"vertical"
		MDToolbar:
			title:"Check Tooltip"
			left_action_items:[['menu']]
		
			MDIconTooltip:
				icon:"magnify"
				tooltip_text:"Search"
				tooltip_bg_color:1,0,0,1
				tooltip_font_style:'Body2'
			MDIconTooltip:
				icon:"refresh"
				tooltip_text:"Reload"
				tooltip_bg_color:1,0,0,1
				tooltip_font_style:'Body2'
			MDIconTooltip:
				icon:"information"
				tooltip_text:"Info"
				tooltip_bg_color:1,0,0,1
				tooltip_font_style:'Body2'
		Widget:
		
		
		
	

'''

class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)
#Thanks for watching

Test().run()