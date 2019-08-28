from docutils import nodes
from docutils.parsers.rst import directives
from runestone.common import RunestoneIdDirective, RunestoneNode

def setup(app):
    app.add_directive('tie', TieDirective)
    app.add_node(TieNode, html=(visit_tie_node, depart_tie_node))
    app.add_config_value('tie_div_class', 'runestone explainer tie_section alert alert_warning', 'html')

VIS = '''
<head>
    <link rel="stylesheet" href="../_static/angular/third_party/codemirror-5.19.0/lib/codemirror.css">
    <link rel="stylesheet" href="../_static/angular/third_party/codemirror-5.19.0/lib/mbo.css">
    <link rel="stylesheet" href="../_static/angular/assets/base.css">
    <script src="../_static/angular/third_party/angular-1.6.1/angular.min.js"></script>
    <script src="../_static/angular/third_party/angular-1.6.1/angular-aria.min.js"></script>
    <script src="../_static/angular/third_party/angular-1.6.1/angular-sanitize.min.js"></script>
    <script src="../_static/angular/third_party/angular-cookies-1.6.1/angular-cookies.min.js"></script>
    <script src="../_static/angular/third_party/codemirror-5.19.0/lib/codemirror.js"></script>
    <script src="../_static/angular/third_party/codemirror-5.19.0/mode/python/python.js"></script>
    <script src="../_static/angular/third_party/codemirror-5.19.0/addon/edit/matchbrackets.js"></script>
    <script src="../_static/angular/third_party/ui-codemirror-0.3.0/ui-codemirror.min.js"></script>
    <script src="../_static/angular/client/config/config.js"></script>
    <script src="../_static/angular/client/config/deploymentSpecificConfig.js"></script>
    <script src="../_static/angular/client/data/data.js"></script>
    <script src="../_static/angular/client/data/domain/BuggyOutputTestObjectFactory.js"></script>
    <script src="../_static/angular/client/data/domain/PerformanceTestObjectFactory.js"></script>
    <script src="../_static/angular/client/data/domain/QuestionObjectFactory.js"></script>
    <script src="../_static/angular/client/data/domain/SuiteLevelTestObjectFactory.js"></script>
    <script src="../_static/angular/client/data/domain/TaskObjectFactory.js"></script>
    <script src="../_static/angular/client/data/domain/TestCaseObjectFactory.js"></script>
    <script src="../_static/angular/client/data/domain/TestSuiteObjectFactory.js"></script>
    <script src="../_static/angular/client/data/domain/TipObjectFactory.js"></script>
    <script src="../_static/angular/client/data/services/QuestionDataService.js"></script>
    <script src="../_static/angular/client/question/question.js"></script>
    <script src="../_static/angular/assets/questions/bomberman.js"></script>
    <script src="../_static/angular/assets/questions/checkBalancedParentheses.js"></script>
    <script src="../_static/angular/assets/questions/findAlphabet.js"></script>
    <script src="../_static/angular/assets/questions/findBestMeetupLocation.js"></script>
    <script src="../_static/angular/assets/questions/findClosestValueBst.js"></script>
    <script src="../_static/angular/assets/questions/findFirstNonRepeatingCharacter.js"></script>
    <script src="../_static/angular/assets/questions/findMostCommonCharacter.js"></script>
    <script src="../_static/angular/assets/questions/findMostCommonRepeatedCharacter.js"></script>
    <script src="../_static/angular/assets/questions/getStrobogrammaticNumbers.js"></script>
    <script src="../_static/angular/assets/questions/incrementDecimalCodedNumber.js"></script>
    <script src="../_static/angular/assets/questions/internationalization.js"></script>
    <script src="../_static/angular/assets/questions/isLeapYear.js"></script>
    <script src="../_static/angular/assets/questions/isPalindrome.js"></script>
    <script src="../_static/angular/assets/questions/longestSubstring.js"></script>
    <script src="../_static/angular/assets/questions/pirateTranslator.js"></script>
    <script src="../_static/angular/assets/questions/reverseWords.js"></script>
    <script src="../_static/angular/assets/questions/runLengthEncoding.js"></script>
    <script src="../_static/angular/assets/questions/sortItinerary.js"></script>
    <script src="../_static/angular/assets/questions/splitStringIntoWords.js"></script>
    <script src="../_static/angular/client/question/components/HtmlWithMarkdownLinksSnippetDirective.js"></script>
    <script src="../_static/angular/client/question/components/LearnerViewDirective.js"></script>
    <script src="../_static/angular/client/question/components/TranscriptParagraphsContainerDirective.js"></script>
    <script src="../_static/angular/client/question/domain/CodeEvalResultObjectFactory.js"></script>
    <script src="../_static/angular/client/question/domain/CodeSubmissionObjectFactory.js"></script>
    <script src="../_static/angular/client/question/domain/ErrorTracebackObjectFactory.js"></script>
    <script src="../_static/angular/client/question/domain/FeedbackDetailsObjectFactory.js"></script>
    <script src="../_static/angular/client/question/domain/FeedbackObjectFactory.js"></script>
    <script src="../_static/angular/client/question/domain/FeedbackParagraphObjectFactory.js"></script>
    <script src="../_static/angular/client/question/domain/LearnerViewSubmissionResultObjectFactory.js"></script>
    <script src="../_static/angular/client/question/domain/PreprocessedCodeObjectFactory.js"></script>
    <script src="../_static/angular/client/question/domain/PrereqCheckErrorObjectFactory.js"></script>
    <script src="../_static/angular/client/question/domain/PrereqCheckFailureObjectFactory.js"></script>
    <script src="../_static/angular/client/question/domain/SnapshotObjectFactory.js"></script>
    <script src="../_static/angular/client/question/domain/TranscriptParagraphObjectFactory.js"></script>
    <script src="../_static/angular/client/question/domain/TracebackCoordinatesObjectFactory.js"></script>
    <script src="../_static/angular/client/question/domain/TranscriptObjectFactory.js"></script>
    <script src="../_static/angular/client/question/services/AutosaveService.js"></script>
    <script src="../_static/angular/client/question/services/ConversationManagerService.js"></script>
    <script src="../_static/angular/client/question/services/CurrentQuestionService.js"></script>
    <script src="../_static/angular/client/question/services/EventHandlerService.js"></script>
    <script src="../_static/angular/client/question/services/FeedbackDisplayService.js"></script>
    <script src="../_static/angular/client/question/services/FeedbackGeneratorService.js"></script>
    <script src="../_static/angular/client/question/services/LearnerStateService.js"></script>
    <script src="../_static/angular/client/question/services/LocalStorageKeyManagerService.js"></script>
    <script src="../_static/angular/client/question/services/LocalStorageService.js"></script>
    <script src="../_static/angular/client/question/services/ParentPageService.js"></script>
    <script src="../_static/angular/client/question/services/PrintTerminalService.js"></script>
    <script src="../_static/angular/client/question/services/ServerHandlerService.js"></script>
    <script src="../_static/angular/client/question/services/SessionHistoryService.js"></script>
    <script src="../_static/angular/client/question/services/SessionIdService.js"></script>
    <script src="../_static/angular/client/question/services/ThemeNameService.js"></script>
    <script src="../_static/angular/client/question/services/UnpromptedFeedbackManagerService.js"></script>
    <script src="../_static/angular/client/question/services/code_evaluators/CodeRunnerDispatcherService.js"></script>
    <script src="../_static/angular/client/question/services/code_evaluators/PrereqCheckDispatcherService.js"></script>
    <script src="../_static/angular/client/question/services/code_evaluators/PythonCodeRunnerService.js"></script>
    <script src="../_static/angular/client/question/services/code_evaluators/PythonPrereqCheckService.js"></script>
    <script src="../_static/angular/client/question/services/code_preprocessors/CodePreprocessorDispatcherService.js"></script>
    <script src="../_static/angular/client/question/services/code_preprocessors/PythonCodePreprocessorService.js"></script>
</head>
<body>
<div id=%(divid)s class="%(divclass)s">
    <learner-view tie-id=%(divid)s question-id="%(question)s" show-output="%(output)s" show-error="%(error)s" show-feedback="%(feedback)s"></learner-view>
</div>
<script type="text/javascript">
    angular.element(document).ready(function() {
        angular.module('TieInstance', ['tie']);
        angular.bootstrap(%(divid)s, ['TieInstance']);
    });
</script>
</body>
'''

# Create a TIE node.
class TieNode(nodes.General, nodes.Element, RunestoneNode):
    def __init__(self, options, **kwargs):
        super(TieNode, self).__init__(**kwargs)
        self.tienode_components = options

def visit_tie_node(self, node):
    div_id = node.tienode_components['divid']
    components = dict(node.tienode_components)
    components.update({'divid': div_id})
    res = VIS % components
    self.body.append(res)

def depart_tie_node(self,node):
    pass

class TieDirective(RunestoneIdDirective):
    """
.. tie:: uniqueid
    :question: questionid
    :output: hide stdout from program
    :error: hide syntax errors from program
    :feedback: hide feedback from program


config values (conf.py): 

- tie_div_class - custom CSS class of the component's outermost div
    """
    required_arguments = 1  # the div id
    optional_arguments = 4
    option_spec = RunestoneIdDirective.option_spec.copy()
    option_spec.update({
        'question': directives.unchanged,
        'output': directives.flag,
        'error': directives.flag,
        'feedback': directives.flag
    })

    node_class = TieNode

    def run(self):
        super(TieDirective, self).run()

        self.options['divid'] = self.arguments[0]

        env = self.state.document.settings.env
        self.options['divclass'] = env.config.tie_div_class

        # Handle arguments included or not included by user.
        if 'question' not in self.options:
            # If the user doesn't choose a question, set the default question to 'Reverse Words'.
            self.options['question'] = 'reverseWords'

        if 'output' not in self.options:
            self.options['output'] = 'false'  
        else:
            self.options['output'] = 'true'

        if 'error' not in self.options:
            self.options['error'] = 'false'
        else:
            self.options['error'] = 'true'

        if 'feedback' not in self.options:
            self.options['feedback'] = 'false'
        else:
            self.options['feedback'] = 'true'

        tie_node = TieNode(self.options, rawsource=self.block_text)
        tie_node.source, tie_node.line = self.state_machine.get_source_and_line(self.lineno)

        return [tie_node]
        