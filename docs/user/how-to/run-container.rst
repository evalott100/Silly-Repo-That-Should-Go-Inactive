Run in a container
==================

Pre-built containers with silly_repo_that_may_go_inactive and its dependencies already
installed are available on `Github Container Registry
<https://ghcr.io/evalott100/silly_repo_that_may_go_inactive>`_.

Starting the container
----------------------

To pull the container from github container registry and run::

    $ docker run ghcr.io/evalott100/silly_repo_that_may_go_inactive:main --version

To get a released version, use a numbered release instead of ``main``.
