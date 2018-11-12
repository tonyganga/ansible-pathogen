import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("dirs", [
    ("/.vim/autoload"),
    ("/.vim/bundle")
])
def test_directories_exist(host, dirs):
    conf = host.file(host.user("root").home + dirs)
    assert conf.exists
    assert conf.is_directory


@pytest.mark.parametrize("dotvim", [
    ("/.vim/autoload/pathogen.vim")
])
def test_pathogen_vim_installed(host, dotvim):
    pathogen = host.file(host.user("root").home+dotvim)
    assert pathogen.exists
    assert pathogen.is_file
