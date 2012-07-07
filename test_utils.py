import mock
import utils
def test_insert_middle():
    with mock.patch("i3.command") as i3command:
        names = ["1: main", "2: zik"]
        res = utils.insert_new_workspace(names, "www")
    call_list = i3command.call_args_list
    assert len(call_list) == 1
    assert call_list[0][0] == ('rename workspace "2: zik" to "3: zik"',)
    assert res == "2: www"

def test_insert_end():
    with mock.patch("i3.command") as i3command:
        names = ["1: main", "2: www"]
        utils.insert_new_workspace(names, "zik")
    call_list = i3command.call_args_list
    assert len(call_list) == 1
    assert call_list[0][0] == ('workspace "3: zik"',)

def test_insert_start():
    with mock.patch("i3.command") as i3command:
        names = ["1: main", "2: www", "3: zik"]
        utils.insert_new_workspace(names, "git")
    call_list = i3command.call_args_list
    assert len(call_list) == 4
    assert call_list[0][0] == ('rename workspace "1: main" to "2: main"',)
    assert call_list[1][0] == ('rename workspace "2: www" to "3: www"',)
    assert call_list[2][0] == ('rename workspace "3: zik" to "4: zik"',)
    assert call_list[3][0] == ('workspace "1: git"',)
