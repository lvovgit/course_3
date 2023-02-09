from utils import get_data


def test_get_data(test_url):
    assert len(get_data(test_url)[0]) > 0
    assert get_data("https://wrong.url.com/")[0] is None
    assert get_data("https://github.com/lvovgit/course_3")[0] is None
    assert get_data("https://github.com/lvovgit/course_")[0] is None


def test_get_filtered_data():
    pass