Phill93 Traefik
=========

Installs traefik in a docker container and configures it.

Requirements
------------

* Docker (i use this one: [geerlingguy.docker](https://github.com/geerlingguy/ansible-role-docker))
* Python docker library (for [ansible](https://docs.ansible.com/ansible/latest/modules/docker_container_module.html))

Role Variables
--------------

  ```yaml
    traefik_static_conf:
    providers:
      file:
        filename: /etc/traefik/dynamic_conf.yaml
    entryPoints:
        web:
            address: :80

    traefik_dynamic_conf: {}
  ```

Example Playbook
----------------

```
    - hosts: servers
      roles:
         - { role: Phill93.traefik}
````

License
-------

[MIT](License.md)

Thanks for the markdown version goes to [IQAndreas](https://github.com/IQAndreas/markdown-licenses)
