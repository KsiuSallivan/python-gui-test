def test_del_group(app):
    if app.groups.count() == 1:
        app.groups.add_new_group("my group")
    old_list = app.groups.get_group_list()
    app.groups.del_group()
    new_list = app.groups.get_group_list()
    assert old_list == new_list
