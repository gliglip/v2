from tag.models import Tag


def test_display_name_conversion():
    normalize = Tag.normalize_name

    assert normalize('TEST') == 'test'
    assert normalize('a b') == 'a-b'
    assert normalize('a  b') == 'a-b'
    assert normalize('A  b') == 'a-b'
    assert normalize('a,b') == 'a-b'
    assert normalize('a, b') == 'a-b'
    assert normalize('1, b') == '1-b'
    assert normalize('1, *') == '1'
