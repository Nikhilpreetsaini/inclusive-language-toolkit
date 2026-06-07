import inclusive_toolkit as it


def test_make_inclusive_changes_words():
    original = "Hello guys!"
    result = it.make_inclusive(original)
    assert isinstance(result, str)
    assert result != original


def test_get_stats_returns_dict():
    stats = it.get_stats("guys chairman mankind")
    assert isinstance(stats, dict)
    assert 'total_words' in stats and 'non_inclusive_count' in stats and 'proportion' in stats


def test_analyze_sentiment_range():
    sentiment = it.analyze_sentiment("This is a wonderful tool.")
    assert isinstance(sentiment, float)
    assert -1.0 <= sentiment <= 1.0


def test_highlight_non_inclusive():
    original = "The fireman talked to the chairman."
    highlighted = it.highlight_non_inclusive(original)
    assert isinstance(highlighted, str)
    assert highlighted != original


def test_suggest_alternatives():
    suggestions = it.suggest_alternatives("man-made objects and mankind")
    assert isinstance(suggestions, dict)
    assert len(suggestions) >= 1
