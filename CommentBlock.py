import sublime, sublime_plugin

class CommentBlockCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		block = """# ------------------- comment -------------------
# -- 
# -- 
# -- 
# -----------------------------------------------"""

		self.view.replace(edit, self.view.sel()[0], block)
