Rails App
=========

Temple University Libraries generic role for deploying rails applications, including blacklight applications.

Role Variables
--------------


### Required Variables
`rails_app_name: myapp`
`rails_app_prod_secret: EXTREMELY_LONG_SECRET_VALUE`

### Optional Variables

| variable  | default value  | description  |
|---|---|---|
| `is_blacklight_app` | false |   |
| `rails_app_use_ssl` | false   |  Set to true to create ssl virtual hosts and add certificates|
|`rails_app_user`   |  {{ rails_app_name }} |  The user that runs the app, under whose account rbenv is installed |
| `rails_app_git_branch` | master |   |
| `rails_app_install_path` | /var/www/{{ rails_app_name }} |   |
| `rails_app_ruby_path` | /home/{{ rails_app_user }}/.rbenv/versions/{{ rbenv.default_ruby}} |   |
| `rails_app_bundle_exe` | "{{rails_app_ruby_path}}/bin/bundle" |   |
| `rails_app_gem_path` | "{{rails_app_ruby_path}}/lib/ruby/gems" |   |
| `rails_app_url_base_path` | "/" | The url path where the application will be served  |
| `rails_app_env` | production |   |
| `rails_app_deployment_exclude_groups`: [test, development] | |



Dependencies
------------

* httpd/Apache2 - for example [geerlingguy.apache](https://galaxy.ansible.com/geerlingguy/apache/)
* Passenger module for httpd [ansible_passenger-apache](https://github.com/tulibraries/ansible_passenger-apache)
* Ruby installed via rbenv [zzet.rbenv](https://galaxy.ansible.com/zzet/rbenv)
* Solr (for Blacklight Apps) [geerlingguy.solr](https://galaxy.ansible.com/geerlingguy/solr/)


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: ansible-rails_app }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
