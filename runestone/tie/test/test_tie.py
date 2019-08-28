from runestone.unittest_base import module_fixture_maker, RunestoneTestCase

setUpModule, tearDownModule = module_fixture_maker(__file__)

class TieTests(RunestoneTestCase):
    # Tests whether the TIE instance is displayed.
    def test_t1(self):
        self.driver.get(self.host + "/index.html")
        t1 = self.driver.find_element_by_id("test1")
        self.assertIsNotNone(t1)

    # Tests for the question ID when it is not specified and when it is
    # specified in the optional parameters.
    def test_t2(self):
        self.driver.get(self.host + "/index.html")
        t2DefaultQuestion = self.driver.find_element_by_id("test2DefaultQuestion")
        self.assertIsNotNone(t2DefaultQuestion)
        defaultQuestionId = t2DefaultQuestion.find_element_by_tag_name("learner-view")
        self.assertTrue(defaultQuestionId, "reverseWords")

        t2CustomQuestion = self.driver.find_element_by_id("test2CustomQuestion")
        self.assertIsNotNone(t2CustomQuestion)
        customQuestionId = t2CustomQuestion.find_element_by_tag_name("learner-view")
        self.assertTrue(customQuestionId, "sortItinerary")

    # Tests whether the feedback window is displayed or not displayed when the user
    # includes or doesn't include the optional parameter for displaying the feedback
    # window.
    def test_t3(self):
        self.driver.get(self.host + "/index.html")
        t3ShowFeedback = self.driver.find_element_by_id("test3ShowFeedback")
        self.assertIsNotNone(t3ShowFeedback)
        feedbackElement = t3ShowFeedback.find_element_by_class_name("tie-feedback-window")
        self.assertIsNotNone(feedbackElement)

        t3HideFeedback = self.driver.find_element_by_id("test3HideFeedback")
        self.assertIsNotNone(t3HideFeedback)
        feedbackElementList = t3HideFeedback.find_elements_by_class_name("tie-feedback-window")
        self.assertEqual(len(feedbackElementList), 0)

    # Tests whether the output window is displayed or not displayed when the user includes
    # or doesn't include the optional parameter for displaying the output window.
    def test_t4(self):
        self.driver.get(self.host + "/index.html")
        t4ShowOutput = self.driver.find_element_by_id("test4ShowOutput")
        self.assertIsNotNone(t4ShowOutput)
        outputElement = t4ShowOutput.find_element_by_class_name("tie-print-terminal")
        self.assertIsNotNone(outputElement)

        t4HideOutput = self.driver.find_element_by_id("test4HideOutput")
        self.assertIsNotNone(t4HideOutput)
        outputElementList = t4HideOutput.find_elements_by_class_name("tie-print-terminal")
        self.assertEqual(len(outputElementList), 0)
