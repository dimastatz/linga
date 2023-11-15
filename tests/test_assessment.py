""" test scenario module """
from linga.assessment import create_assessment_prompt
from linga.scenario import Levels


def test_create_assessment_prompt_for_beginner():
    """tests create assessment"""
    level = Levels.BEGINNER
    language = "Russian"
    comics = "Yuri Alekseyevich Gagarin was a Soviet pilot and cosmonaut who, aboard the first successful crewed " \
             "spaceflight, became the first human to journey into outer space. Travelling on Vostok 1, he orbited " \
             "Earth at an altitude of 327 kilometres for 108 minutes."
    res = create_assessment_prompt(
        comics,
        "",
        level.name, "Russian")
    print(res)

    assert comics in res
    assert "chat history" not in res
    assert level.name in res
    assert language in res
