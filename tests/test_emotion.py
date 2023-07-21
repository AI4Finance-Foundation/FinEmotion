from finemotion import emotion

def test_get_mixed_emotion_submission():
    text = "fear fear fear fear trust trust trust trust"
    result = emotion.get_mixed_emotion(text)
    assert "submission" == result

def test_get_mixed_emotion_fear():
    text = "The stock market is extremely volatile today!"
    result = emotion.get_mixed_emotion(text)
    assert "fear" == result