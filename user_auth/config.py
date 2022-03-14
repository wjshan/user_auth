import os
from dynaconf import Dynaconf
HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix="user_auth",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["settings.toml", ".secrets.toml"],
    environments=["development", "production", "testing"],
    env_switcher="user_auth_env",
    load_dotenv=True,
)

"""
# How to use this application settings

```
from user_auth.config import settings
```

## Acessing variables

```
settings.get("SECRET_KEY", default="sdnfjbnfsdf")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Modifying variables

### On files

settings.toml
```
[development]
KEY=value
```

### As environment variables
```
export user_auth_KEY=value
export user_auth_KEY="@int 42"
export user_auth_KEY="@jinja {{ this.db.uri }}"
export user_auth_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

### Switching environments
```
user_auth_ENV=production user_auth run
```

Read more on https://dynaconf.com
"""
