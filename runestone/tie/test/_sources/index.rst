TIE Test
----------

.. .. raw:: html
  
..     <head>
..       <title>Technical Interview Exercises</title>
..       <meta charset="UTF-8">
..       <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
..       <link rel="stylesheet" href="../_static/angular/third_party/codemirror-5.19.0/lib/codemirror.css">
..       <link rel="stylesheet" href="../_static/angular/third_party/codemirror-5.19.0/lib/mbo.css">
..       <link rel="stylesheet" href="../_static/angular/assets/base.css">
..       <script src="../_static/angular/third_party/angular-1.6.1/angular.min.js"></script>
..       <script src="../_static/angular/third_party/angular-1.6.1/angular-aria.min.js"></script>
..       <script src="../_static/angular/third_party/angular-1.6.1/angular-sanitize.min.js"></script>
..       <script src="../_static/angular/third_party/angular-cookies-1.6.1/angular-cookies.min.js"></script>
..       <script src="../_static/angular/third_party/codemirror-5.19.0/lib/codemirror.js"></script>
..       <script src="../_static/angular/third_party/codemirror-5.19.0/mode/python/python.js"></script>
..       <script src="../_static/angular/third_party/codemirror-5.19.0/addon/edit/matchbrackets.js"></script>
..       <script src="../_static/angular/third_party/ui-codemirror-0.3.0/ui-codemirror.min.js"></script>
..       <script src="../_static/angular/client/config/config.js"></script>
..       <script src="../_static/angular/client/config/deploymentSpecificConfig.js"></script>
..       <script src="../_static/angular/client/data/data.js"></script>
..       <script src="../_static/angular/client/data/domain/BuggyOutputTestObjectFactory.js"></script>
..       <script src="../_static/angular/client/data/domain/PerformanceTestObjectFactory.js"></script>
..       <script src="../_static/angular/client/data/domain/QuestionObjectFactory.js"></script>
..       <script src="../_static/angular/client/data/domain/SuiteLevelTestObjectFactory.js"></script>
..       <script src="../_static/angular/client/data/domain/TaskObjectFactory.js"></script>
..       <script src="../_static/angular/client/data/domain/TestCaseObjectFactory.js"></script>
..       <script src="../_static/angular/client/data/domain/TestSuiteObjectFactory.js"></script>
..       <script src="../_static/angular/client/data/domain/TipObjectFactory.js"></script>
..       <script src="../_static/angular/client/data/services/QuestionDataService.js"></script>
..       <script src="../_static/angular/client/question/question.js"></script>
..       <script src="../_static/angular/assets/questions/bomberman.js"></script>
..       <script src="../_static/angular/assets/questions/checkBalancedParentheses.js"></script>
..       <script src="../_static/angular/assets/questions/findAlphabet.js"></script>
..       <script src="../_static/angular/assets/questions/findBestMeetupLocation.js"></script>
..       <script src="../_static/angular/assets/questions/findClosestValueBst.js"></script>
..       <script src="../_static/angular/assets/questions/findFirstNonRepeatingCharacter.js"></script>
..       <script src="../_static/angular/assets/questions/findMostCommonCharacter.js"></script>
..       <script src="../_static/angular/assets/questions/findMostCommonRepeatedCharacter.js"></script>
..       <script src="../_static/angular/assets/questions/getStrobogrammaticNumbers.js"></script>
..       <script src="../_static/angular/assets/questions/incrementDecimalCodedNumber.js"></script>
..       <script src="../_static/angular/assets/questions/internationalization.js"></script>
..       <script src="../_static/angular/assets/questions/isLeapYear.js"></script>
..       <script src="../_static/angular/assets/questions/isPalindrome.js"></script>
..       <script src="../_static/angular/assets/questions/longestSubstring.js"></script>
..       <script src="../_static/angular/assets/questions/pirateTranslator.js"></script>
..       <script src="../_static/angular/assets/questions/reverseWords.js"></script>
..       <script src="../_static/angular/assets/questions/runLengthEncoding.js"></script>
..       <script src="../_static/angular/assets/questions/sortItinerary.js"></script>
..       <script src="../_static/angular/assets/questions/splitStringIntoWords.js"></script>
..       <script src="../_static/angular/client/question/components/HtmlWithMarkdownLinksSnippetDirective.js"></script>
..       <script src="../_static/angular/client/question/components/LearnerViewDirective.js"></script>
..       <script src="../_static/angular/client/question/components/TranscriptParagraphsContainerDirective.js"></script>
..       <script src="../_static/angular/client/question/domain/CodeEvalResultObjectFactory.js"></script>
..       <script src="../_static/angular/client/question/domain/CodeSubmissionObjectFactory.js"></script>
..       <script src="../_static/angular/client/question/domain/ErrorTracebackObjectFactory.js"></script>
..       <script src="../_static/angular/client/question/domain/FeedbackDetailsObjectFactory.js"></script>
..       <script src="../_static/angular/client/question/domain/FeedbackObjectFactory.js"></script>
..       <script src="../_static/angular/client/question/domain/FeedbackParagraphObjectFactory.js"></script>
..       <script src="../_static/angular/client/question/domain/LearnerViewSubmissionResultObjectFactory.js"></script>
..       <script src="../_static/angular/client/question/domain/PreprocessedCodeObjectFactory.js"></script>
..       <script src="../_static/angular/client/question/domain/PrereqCheckErrorObjectFactory.js"></script>
..       <script src="../_static/angular/client/question/domain/PrereqCheckFailureObjectFactory.js"></script>
..       <script src="../_static/angular/client/question/domain/SnapshotObjectFactory.js"></script>
..       <script src="../_static/angular/client/question/domain/TranscriptParagraphObjectFactory.js"></script>
..       <script src="../_static/angular/client/question/domain/TracebackCoordinatesObjectFactory.js"></script>
..       <script src="../_static/angular/client/question/domain/TranscriptObjectFactory.js"></script>
..       <script src="../_static/angular/client/question/services/AutosaveService.js"></script>
..       <script src="../_static/angular/client/question/services/ConversationManagerService.js"></script>
..       <script src="../_static/angular/client/question/services/CurrentQuestionService.js"></script>
..       <script src="../_static/angular/client/question/services/EventHandlerService.js"></script>
..       <script src="../_static/angular/client/question/services/FeedbackDisplayService.js"></script>
..       <script src="../_static/angular/client/question/services/FeedbackGeneratorService.js"></script>
..       <script src="../_static/angular/client/question/services/LearnerStateService.js"></script>
..       <script src="../_static/angular/client/question/services/LocalStorageKeyManagerService.js"></script>
..       <script src="../_static/angular/client/question/services/LocalStorageService.js"></script>
..       <script src="../_static/angular/client/question/services/ParentPageService.js"></script>
..       <script src="../_static/angular/client/question/services/PrintTerminalService.js"></script>
..       <script src="../_static/angular/client/question/services/ServerHandlerService.js"></script>
..       <script src="../_static/angular/client/question/services/SessionHistoryService.js"></script>
..       <script src="../_static/angular/client/question/services/SessionIdService.js"></script>
..       <script src="../_static/angular/client/question/services/ThemeNameService.js"></script>
..       <script src="../_static/angular/client/question/services/UnpromptedFeedbackManagerService.js"></script>
..       <script src="../_static/angular/client/question/services/code_evaluators/CodeRunnerDispatcherService.js"></script>
..       <script src="../_static/angular/client/question/services/code_evaluators/PrereqCheckDispatcherService.js"></script>
..       <script src="../_static/angular/client/question/services/code_evaluators/PythonCodeRunnerService.js"></script>
..       <script src="../_static/angular/client/question/services/code_evaluators/PythonPrereqCheckService.js"></script>
..       <script src="../_static/angular/client/question/services/code_preprocessors/CodePreprocessorDispatcherService.js"></script>
..       <script src="../_static/angular/client/question/services/code_preprocessors/PythonCodePreprocessorService.js"></script>
..       <script type="text/javascript">
..         var rootApp = angular.module('rootApp', ['primaryApp', 'secondaryApp']);
..         var primaryApp = angular.module('primaryApp', ['tie']);
..         var secondaryApp = angular.module('secondaryApp', ['tie']);
..       </script>
..     </head>
..     <body>
..       <div ng-app="rootApp">
..         <div id="primaryApp">
..           <learner-view></learner-view>
..         </div>
..         <div id="secondaryApp">
..           <learner-view></learner-view>
..         </div>
..       </div>
..     </body>


.. .. raw:: html
  
..     <head>
..       <title>Technical Interview Exercises</title>
..       <meta charset="UTF-8">
..       <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
..       <link rel="stylesheet" href="../_static/angular/third_party/codemirror-5.19.0/lib/codemirror.css">
..       <link rel="stylesheet" href="../_static/angular/third_party/codemirror-5.19.0/lib/mbo.css">
..       <link rel="stylesheet" href="../_static/angular/assets/base.css">
..       <script src="../_static/angular/third_party/angular-1.6.1/angular.min.js"></script>
..       <script src="../_static/angular/third_party/angular-1.6.1/angular-aria.min.js"></script>
..       <script src="../_static/angular/third_party/angular-1.6.1/angular-sanitize.min.js"></script>
..       <script src="../_static/angular/third_party/angular-cookies-1.6.1/angular-cookies.min.js"></script>
..       <script src="../_static/angular/third_party/codemirror-5.19.0/lib/codemirror.js"></script>
..       <script src="../_static/angular/third_party/codemirror-5.19.0/mode/python/python.js"></script>
..       <script src="../_static/angular/third_party/codemirror-5.19.0/addon/edit/matchbrackets.js"></script>
..       <script src="../_static/angular/third_party/ui-codemirror-0.3.0/ui-codemirror.min.js"></script>
..       <script src="../_static/angular/client/config/config.js"></script>
..       <script src="../_static/angular/client/config/deploymentSpecificConfig.js"></script>
..       <script src="../_static/angular/client/data/data.js"></script>
..       <script src="../_static/angular/client/data/domain/BuggyOutputTestObjectFactory.js"></script>
..       <script src="../_static/angular/client/data/domain/PerformanceTestObjectFactory.js"></script>
..       <script src="../_static/angular/client/data/domain/QuestionObjectFactory.js"></script>
..       <script src="../_static/angular/client/data/domain/SuiteLevelTestObjectFactory.js"></script>
..       <script src="../_static/angular/client/data/domain/TaskObjectFactory.js"></script>
..       <script src="../_static/angular/client/data/domain/TestCaseObjectFactory.js"></script>
..       <script src="../_static/angular/client/data/domain/TestSuiteObjectFactory.js"></script>
..       <script src="../_static/angular/client/data/domain/TipObjectFactory.js"></script>
..       <script src="../_static/angular/client/data/services/QuestionDataService.js"></script>
..       <script src="../_static/angular/client/question/question.js"></script>
..       <script src="../_static/angular/assets/questions/bomberman.js"></script>
..       <script src="../_static/angular/assets/questions/checkBalancedParentheses.js"></script>
..       <script src="../_static/angular/assets/questions/findAlphabet.js"></script>
..       <script src="../_static/angular/assets/questions/findBestMeetupLocation.js"></script>
..       <script src="../_static/angular/assets/questions/findClosestValueBst.js"></script>
..       <script src="../_static/angular/assets/questions/findFirstNonRepeatingCharacter.js"></script>
..       <script src="../_static/angular/assets/questions/findMostCommonCharacter.js"></script>
..       <script src="../_static/angular/assets/questions/findMostCommonRepeatedCharacter.js"></script>
..       <script src="../_static/angular/assets/questions/getStrobogrammaticNumbers.js"></script>
..       <script src="../_static/angular/assets/questions/incrementDecimalCodedNumber.js"></script>
..       <script src="../_static/angular/assets/questions/internationalization.js"></script>
..       <script src="../_static/angular/assets/questions/isLeapYear.js"></script>
..       <script src="../_static/angular/assets/questions/isPalindrome.js"></script>
..       <script src="../_static/angular/assets/questions/longestSubstring.js"></script>
..       <script src="../_static/angular/assets/questions/pirateTranslator.js"></script>
..       <script src="../_static/angular/assets/questions/reverseWords.js"></script>
..       <script src="../_static/angular/assets/questions/runLengthEncoding.js"></script>
..       <script src="../_static/angular/assets/questions/sortItinerary.js"></script>
..       <script src="../_static/angular/assets/questions/splitStringIntoWords.js"></script>
..       <script src="../_static/angular/client/question/components/HtmlWithMarkdownLinksSnippetDirective.js"></script>
..       <script src="../_static/angular/client/question/components/LearnerViewDirective.js"></script>
..       <script src="../_static/angular/client/question/components/TranscriptParagraphsContainerDirective.js"></script>
..       <script src="../_static/angular/client/question/domain/CodeEvalResultObjectFactory.js"></script>
..       <script src="../_static/angular/client/question/domain/CodeSubmissionObjectFactory.js"></script>
..       <script src="../_static/angular/client/question/domain/ErrorTracebackObjectFactory.js"></script>
..       <script src="../_static/angular/client/question/domain/FeedbackDetailsObjectFactory.js"></script>
..       <script src="../_static/angular/client/question/domain/FeedbackObjectFactory.js"></script>
..       <script src="../_static/angular/client/question/domain/FeedbackParagraphObjectFactory.js"></script>
..       <script src="../_static/angular/client/question/domain/LearnerViewSubmissionResultObjectFactory.js"></script>
..       <script src="../_static/angular/client/question/domain/PreprocessedCodeObjectFactory.js"></script>
..       <script src="../_static/angular/client/question/domain/PrereqCheckErrorObjectFactory.js"></script>
..       <script src="../_static/angular/client/question/domain/PrereqCheckFailureObjectFactory.js"></script>
..       <script src="../_static/angular/client/question/domain/SnapshotObjectFactory.js"></script>
..       <script src="../_static/angular/client/question/domain/TranscriptParagraphObjectFactory.js"></script>
..       <script src="../_static/angular/client/question/domain/TracebackCoordinatesObjectFactory.js"></script>
..       <script src="../_static/angular/client/question/domain/TranscriptObjectFactory.js"></script>
..       <script src="../_static/angular/client/question/services/AutosaveService.js"></script>
..       <script src="../_static/angular/client/question/services/ConversationManagerService.js"></script>
..       <script src="../_static/angular/client/question/services/CurrentQuestionService.js"></script>
..       <script src="../_static/angular/client/question/services/EventHandlerService.js"></script>
..       <script src="../_static/angular/client/question/services/FeedbackDisplayService.js"></script>
..       <script src="../_static/angular/client/question/services/FeedbackGeneratorService.js"></script>
..       <script src="../_static/angular/client/question/services/LearnerStateService.js"></script>
..       <script src="../_static/angular/client/question/services/LocalStorageKeyManagerService.js"></script>
..       <script src="../_static/angular/client/question/services/LocalStorageService.js"></script>
..       <script src="../_static/angular/client/question/services/ParentPageService.js"></script>
..       <script src="../_static/angular/client/question/services/PrintTerminalService.js"></script>
..       <script src="../_static/angular/client/question/services/ServerHandlerService.js"></script>
..       <script src="../_static/angular/client/question/services/SessionHistoryService.js"></script>
..       <script src="../_static/angular/client/question/services/SessionIdService.js"></script>
..       <script src="../_static/angular/client/question/services/ThemeNameService.js"></script>
..       <script src="../_static/angular/client/question/services/UnpromptedFeedbackManagerService.js"></script>
..       <script src="../_static/angular/client/question/services/code_evaluators/CodeRunnerDispatcherService.js"></script>
..       <script src="../_static/angular/client/question/services/code_evaluators/PrereqCheckDispatcherService.js"></script>
..       <script src="../_static/angular/client/question/services/code_evaluators/PythonCodeRunnerService.js"></script>
..       <script src="../_static/angular/client/question/services/code_evaluators/PythonPrereqCheckService.js"></script>
..       <script src="../_static/angular/client/question/services/code_preprocessors/CodePreprocessorDispatcherService.js"></script>
..       <script src="../_static/angular/client/question/services/code_preprocessors/PythonCodePreprocessorService.js"></script>
..       <script type="text/javascript">
..         var primaryApp = angular.module('primaryApp', ['tie']);
..         var secondaryApp = angular.module('secondaryApp', ['tie']);

..         angular.element(document).ready(function() {
..           var primaryModule = document.getElementById('primaryApp');
..           angular.bootstrap(primaryModule, ['primaryApp']);
..           var secondaryModule = document.getElementById('secondaryApp');
..           angular.bootstrap(secondaryModule, ['secondaryApp']);
..         });
..       </script>
..     </head>
..     <body>
..       <div id="primaryApp">
..         <learner-view></learner-view>
..       </div>
..       <div id="secondaryApp">
..         <learner-view></learner-view>
..       </div>
..     </body>



.. .. raw:: html
  
..     <head>
..       <title>Technical Interview Exercises</title>
..       <meta charset="UTF-8">
..       <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
..       <link rel="stylesheet" href="../_static/angular/third_party/codemirror-5.19.0/lib/codemirror.css">
..       <link rel="stylesheet" href="../_static/angular/third_party/codemirror-5.19.0/lib/mbo.css">
..       <link rel="stylesheet" href="../_static/angular/assets/base.css">
..       <script src="../_static/angular/third_party/angular-1.6.1/angular.min.js"></script>
..       <script src="../_static/angular/third_party/angular-1.6.1/angular-aria.min.js"></script>
..       <script src="../_static/angular/third_party/angular-1.6.1/angular-sanitize.min.js"></script>
..       <script src="../_static/angular/third_party/angular-cookies-1.6.1/angular-cookies.min.js"></script>
..       <script src="../_static/angular/third_party/codemirror-5.19.0/lib/codemirror.js"></script>
..       <script src="../_static/angular/third_party/codemirror-5.19.0/mode/python/python.js"></script>
..       <script src="../_static/angular/third_party/codemirror-5.19.0/addon/edit/matchbrackets.js"></script>
..       <script src="../_static/angular/third_party/ui-codemirror-0.3.0/ui-codemirror.min.js"></script>
..       <script src="../_static/angular/client/config/config.js"></script>
..       <script src="../_static/angular/client/config/deploymentSpecificConfig.js"></script>
..       <script src="../_static/angular/client/data/data.js"></script>
..       <script src="../_static/angular/client/data/domain/BuggyOutputTestObjectFactory.js"></script>
..       <script src="../_static/angular/client/data/domain/PerformanceTestObjectFactory.js"></script>
..       <script src="../_static/angular/client/data/domain/QuestionObjectFactory.js"></script>
..       <script src="../_static/angular/client/data/domain/SuiteLevelTestObjectFactory.js"></script>
..       <script src="../_static/angular/client/data/domain/TaskObjectFactory.js"></script>
..       <script src="../_static/angular/client/data/domain/TestCaseObjectFactory.js"></script>
..       <script src="../_static/angular/client/data/domain/TestSuiteObjectFactory.js"></script>
..       <script src="../_static/angular/client/data/domain/TipObjectFactory.js"></script>
..       <script src="../_static/angular/client/data/services/QuestionDataService.js"></script>
..       <script src="../_static/angular/client/question/question.js"></script>
..       <script src="../_static/angular/assets/questions/bomberman.js"></script>
..       <script src="../_static/angular/assets/questions/checkBalancedParentheses.js"></script>
..       <script src="../_static/angular/assets/questions/findAlphabet.js"></script>
..       <script src="../_static/angular/assets/questions/findBestMeetupLocation.js"></script>
..       <script src="../_static/angular/assets/questions/findClosestValueBst.js"></script>
..       <script src="../_static/angular/assets/questions/findFirstNonRepeatingCharacter.js"></script>
..       <script src="../_static/angular/assets/questions/findMostCommonCharacter.js"></script>
..       <script src="../_static/angular/assets/questions/findMostCommonRepeatedCharacter.js"></script>
..       <script src="../_static/angular/assets/questions/getStrobogrammaticNumbers.js"></script>
..       <script src="../_static/angular/assets/questions/incrementDecimalCodedNumber.js"></script>
..       <script src="../_static/angular/assets/questions/internationalization.js"></script>
..       <script src="../_static/angular/assets/questions/isLeapYear.js"></script>
..       <script src="../_static/angular/assets/questions/isPalindrome.js"></script>
..       <script src="../_static/angular/assets/questions/longestSubstring.js"></script>
..       <script src="../_static/angular/assets/questions/pirateTranslator.js"></script>
..       <script src="../_static/angular/assets/questions/reverseWords.js"></script>
..       <script src="../_static/angular/assets/questions/runLengthEncoding.js"></script>
..       <script src="../_static/angular/assets/questions/sortItinerary.js"></script>
..       <script src="../_static/angular/assets/questions/splitStringIntoWords.js"></script>
..       <script src="../_static/angular/client/question/components/HtmlWithMarkdownLinksSnippetDirective.js"></script>
..       <script src="../_static/angular/client/question/components/LearnerViewDirective.js"></script>
..       <script src="../_static/angular/client/question/components/TranscriptParagraphsContainerDirective.js"></script>
..       <script src="../_static/angular/client/question/domain/CodeEvalResultObjectFactory.js"></script>
..       <script src="../_static/angular/client/question/domain/CodeSubmissionObjectFactory.js"></script>
..       <script src="../_static/angular/client/question/domain/ErrorTracebackObjectFactory.js"></script>
..       <script src="../_static/angular/client/question/domain/FeedbackDetailsObjectFactory.js"></script>
..       <script src="../_static/angular/client/question/domain/FeedbackObjectFactory.js"></script>
..       <script src="../_static/angular/client/question/domain/FeedbackParagraphObjectFactory.js"></script>
..       <script src="../_static/angular/client/question/domain/LearnerViewSubmissionResultObjectFactory.js"></script>
..       <script src="../_static/angular/client/question/domain/PreprocessedCodeObjectFactory.js"></script>
..       <script src="../_static/angular/client/question/domain/PrereqCheckErrorObjectFactory.js"></script>
..       <script src="../_static/angular/client/question/domain/PrereqCheckFailureObjectFactory.js"></script>
..       <script src="../_static/angular/client/question/domain/SnapshotObjectFactory.js"></script>
..       <script src="../_static/angular/client/question/domain/TranscriptParagraphObjectFactory.js"></script>
..       <script src="../_static/angular/client/question/domain/TracebackCoordinatesObjectFactory.js"></script>
..       <script src="../_static/angular/client/question/domain/TranscriptObjectFactory.js"></script>
..       <script src="../_static/angular/client/question/services/AutosaveService.js"></script>
..       <script src="../_static/angular/client/question/services/ConversationManagerService.js"></script>
..       <script src="../_static/angular/client/question/services/CurrentQuestionService.js"></script>
..       <script src="../_static/angular/client/question/services/EventHandlerService.js"></script>
..       <script src="../_static/angular/client/question/services/FeedbackDisplayService.js"></script>
..       <script src="../_static/angular/client/question/services/FeedbackGeneratorService.js"></script>
..       <script src="../_static/angular/client/question/services/LearnerStateService.js"></script>
..       <script src="../_static/angular/client/question/services/LocalStorageKeyManagerService.js"></script>
..       <script src="../_static/angular/client/question/services/LocalStorageService.js"></script>
..       <script src="../_static/angular/client/question/services/ParentPageService.js"></script>
..       <script src="../_static/angular/client/question/services/PrintTerminalService.js"></script>
..       <script src="../_static/angular/client/question/services/ServerHandlerService.js"></script>
..       <script src="../_static/angular/client/question/services/SessionHistoryService.js"></script>
..       <script src="../_static/angular/client/question/services/SessionIdService.js"></script>
..       <script src="../_static/angular/client/question/services/ThemeNameService.js"></script>
..       <script src="../_static/angular/client/question/services/UnpromptedFeedbackManagerService.js"></script>
..       <script src="../_static/angular/client/question/services/code_evaluators/CodeRunnerDispatcherService.js"></script>
..       <script src="../_static/angular/client/question/services/code_evaluators/PrereqCheckDispatcherService.js"></script>
..       <script src="../_static/angular/client/question/services/code_evaluators/PythonCodeRunnerService.js"></script>
..       <script src="../_static/angular/client/question/services/code_evaluators/PythonPrereqCheckService.js"></script>
..       <script src="../_static/angular/client/question/services/code_preprocessors/CodePreprocessorDispatcherService.js"></script>
..       <script src="../_static/angular/client/question/services/code_preprocessors/PythonCodePreprocessorService.js"></script>
..     </head>
..     <body>
..       <div id="view"><learner-view></learner-view></div>
..       <script type="text/javascript">
..         angular.module('tieInstance', ['tie']);
..         angular.bootstrap(document.getElementById('view'), ['tieInstance']);
..       </script>
..     </body>

.. tie:: codeexample1
  :question: sortItinerary
  :output:
  :feedback:


.. tie:: codeexample2
  :output:
  :feedback:
