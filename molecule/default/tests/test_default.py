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
