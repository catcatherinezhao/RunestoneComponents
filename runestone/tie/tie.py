from docutils import nodes
from docutils.parsers.rst import directives
from runestone.server.componentdb import addQuestionToDB, addHTMLToDB
from runestone.common import RunestoneIdDirective, RunestoneNode
import sys, os

def setup(app):
    app.add_directive('tie', TieDirective)
    app.add_node(TieNode, html=(visit_tie_node, depart_tie_node))

    app.add_autoversioned_javascript('tie.js')
    app.add_config_value('tie_div_class', 'runestone', 'html')

    app.connect('doctree-resolved', process_tie_nodes)
    app.connect('env-purge-doc', purge_tie)

VIS = '''
<div class="runestone">
<p data-component="tie" class="%(divclass)s" id=%(divid)s></p>
</div>
'''


# # no node
# class Tie(RunestoneIdDirective):
#     """
# .. tie:: uniqueid
#    :showfeedback: feedback for incorrect answers
#    :showoutput: show stdout from program
#    :showsyntaxerrors: show syntax errors from the program

# config values (conf.py): 

# - tie_div_class - custom CSS class of the component's outermost div
#     """
#     required_arguments = 1
#     optional_arguments = 1
#     option_spec = RunestoneIdDirective.option_spec.copy()
#     # option_spec.update({
#     #     'showfeedback': directives.flag,
#     #     'showoutput': directives.flag,
#     #     'showsyntaxerrors': directives.flag,
#     # })

#     has_content = True

#     def run(self):
#         super(TIE, self).run()

#         # addQuestionToDB(self)

#         env = self.state.document.settings.env
#         self.options['divclass'] = env.config.tie_div_class

#         return [nodes.raw('', '<learner-view-directive></learner-view-directive>', format='html')]


# with node
class TieNode(nodes.General, nodes.Element, RunestoneNode):
    def __init__(self, options, **kwargs):
        super(TieNode, self).__init__(**kwargs)
        self.tienode_components = options


def visit_tie_node(self, node):
    div_id = node.tienode_components['divid']
    components = dict(node.tienode_components)
    components.update({'divid': div_id})
    res = VIS % components
    # addHTMLToDB(div_id, components['basecourse'], res)

    self.body.append(res)

def depart_tie_node(self,node):
    pass

def process_tie_nodes(app, env, docname):
    pass

def purge_tie(app, env, docname):
    pass

class TieDirective(RunestoneIdDirective):
    """
.. tie:: uniqueid


config values (conf.py): 

- tie_div_class - custom CSS class of the component's outermost div
    """
    required_arguments = 1  # the div id
    optional_arguments = 0
    final_argument_whitespace = True
    has_content = True
    option_spec = RunestoneIdDirective.option_spec.copy()
    # option_spec.update({'optional': directives.flag})

    node_class = TieNode

    def run(self):
        super(TieDirective, self).run()
        # addQuestionToDB(self)
        # Raise an error if the directive does not have contents.
        self.assert_has_content()

        self.options['divid'] = self.arguments[0]

        env = self.state.document.settings.env
        self.options['divclass'] = env.config.tabbed_div_class

        tie_node = TieNode(self.options, rawsource=self.block_text)
        tie_node.source, tie_node.line = self.state_machine.get_source_and_line(self.lineno)

        return [tie_node]
