import pytest
from finemotion import emotion

def test_get_mixed_emotion():
    text = "fear fear fear fear trust trust trust trust"
    result = emotion.get_mixed_emotion(text)
    assert "submission" == result