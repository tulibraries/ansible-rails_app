Rails App
=========

Temple University Libraries generic role for deploying rails applications, including blacklight applications.

Role Variables
--------------


### Required Variables
These must be defined in your playbook for this role to work.

`rails_app_name: myapp` # Name of your app which will define the install directory, app user, and more

`rails_app_git_url`: # URL to the public github repo where you app can be found

`rails_app_git_branch`: the branch or tag to use 

`rails_app_prod_secret`: EXTREMELY_LONG_SECRET_VALUE` # This should be vaulted.

### Optional Variables

| variable  | default value  | description  |
|---|---|---|
| `rails_app_url_base_path` | "/" | The url path where the application will be served  |
| `is_blacklight_app` | false | If this is a blacklight app, then it does some Blacklight specific things  |
| `rails_app_use_ssl` | false   |  Set to true to create ssl virtual hosts and add certificates |
| `rails_app_force_ssl` | false   |  Set to true to redirect all incoming traffic to https |
|`rails_app_user`   |  {{ rails_app_name }} |  The user that runs the app, under whose account rbenv is installed |
| `rails_app_install_path` | /var/www/{{ rails_app_name }} |   |
| `rails_app_ruby_path` | /home/{{ rails_app_user }}/.rbenv/versions/{{ rbenv.default_ruby}} |   |
| `rails_app_bundle_exe` | "{{rails_app_ruby_path}}/bin/bundle" |   |
| `rails_app_gem_path` | "{{rails_app_ruby_path}}/lib/ruby/gems" |   |
| `rails_app_env` | production |   |
| `rails_app_user_envvars`| [] | Array of dictionaries of evvars to be set. `{envvar: "COW", value: "moo"}`. Can also take an `when` for conditional envvar setting |
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
         - {role: ansible-rails_app, rails_app_name: myapp, rails_app_git_url: https://github.com/tulibraries/myapp}

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
