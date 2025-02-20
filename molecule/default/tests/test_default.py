import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_httpd_is_running(host):
    service = host.service('httpd')
    assert service.is_running


def test_httpd_application_conf_created(host):
    f = host.file('/etc/httpd/conf.d/applications.conf')
    assert f.exists


def test_rails_app_in_place(host):
    app_dir = host.file("/var/www/nothing")
    assert app_dir.is_directory


def test_bundle_config_in_place(host):
    f = host.file("/home/nothing/.bundle/config")
    assert f.exists
    assert f.contains("NEEDS_FLAGS: \"--with-flags\"")


def test_rails_app_user_envvars(host):
    env = host.file("/var/www/nothing/.env.local")
    assert env.exists
    assert env.contains("MOO='cow'")
    assert env.contains("PIG='oink'")
    assert env.contains("COW='moo'") is False


def test_node_version(host):
    cmd = host.run("node --version")
    assert cmd.rc == 0
    assert cmd.stdout.rstrip() == "v23.8.0"
