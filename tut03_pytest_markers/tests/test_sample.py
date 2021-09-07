import sys

import pytest

from tut03_pytest_markers.myapp.sample import add


@pytest.mark.skip(reason="just wanna skip it")
def test_add_num():
    assert add(1, 2) == 3


@pytest.mark.skipif(sys.version_info > (3, 7), reason="use python 3.7 or less")
def test_add_str():
    assert add("a", "b") == "ab"


@pytest.mark.xfail(sys.platform == "darwin", reason="don't run on mac")
def test_add_list():
    assert add([1], [2]) == [1, 2]
    raise Exception()
