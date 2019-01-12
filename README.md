This repo exists to show off what appears to be a bug in PyCharm's django template folder detection mechanism.
The bug is that the initial definiton of django's TEMPLATES setting seems to be the only thing that PyCharm looks at to determine if
the APP_DIRS setting is True. This doesn't seem to make a lick of sense.

See here for more details: 
https://intellij-support.jetbrains.com/hc/en-us/community/posts/360002403919-PyCharm-2018-3-2-reads-Django-s-APP-DIRS-setting-in-TEMPLATES-wrong-causing-really-bizarre-behavior
