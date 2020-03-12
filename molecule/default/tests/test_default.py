import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_config_dir(host):
    conf_dir = "/etc/traefik"
    assert host.file(conf_dir).is_directory
    assert host.file(conf_dir).user == "root"
    assert host.file(conf_dir).group == "root"
    assert host.file(conf_dir).mode == 0o750


def test_config_static(host):
    conf_file = "/etc/traefik/traefik.json"
    assert host.file(conf_file).is_file
    assert host.file(conf_file).user == "root"
    assert host.file(conf_file).group == "root"
    assert host.file(conf_file).mode == 0o640


def test_config_dynamic(host):
    conf_file = "/etc/traefik/dynamic.json"
    assert host.file(conf_file).is_file
    assert host.file(conf_file).user == "root"
    assert host.file(conf_file).group == "root"
    assert host.file(conf_file).mode == 0o640


def test_docker(host):
    traefik = host.docker('traefik')
    assert traefik.is_running


def test_ports(host):
    assert host.socket("tcp://80").is_listening
    assert host.socket("tcp://443").is_listening
