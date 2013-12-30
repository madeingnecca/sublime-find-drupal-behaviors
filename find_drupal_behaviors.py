import sublime
import sublime_plugin

# @TODO: make regex configurable.
BEHAVIOR_RE = 'Drupal\.behaviors\.([^\s]+)\s*?=\s*?\{'

class FindDrupalBehaviorsCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        behaviors = []
        quicklist = []

        replacements = []
        matching_regions = self.view.find_all(BEHAVIOR_RE, sublime.IGNORECASE, '\\1', replacements)

        i = 0
        for r in matching_regions:
            behavior_name = replacements[i]
            behaviors.append({'name': behavior_name, 'region': r})
            quicklist.append(behavior_name)
            i += 1

        def goto_behavior(index):
            if index is not -1:
                item = behaviors[index]
                self.view.sel().clear()
                self.view.sel().add(item['region'])
                self.view.show(item['region'])

        self.view.window().show_quick_panel(quicklist, goto_behavior)
