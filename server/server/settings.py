from pathlib import Path

"""
Django项目的设置。

通过使用Django 5.0.7生成的'django-admin startproject'。

有关此文件的更多信息，请参见
https://docs.djangoproject.com/en/5.0/topics/settings/

有关设置及其值的完整列表，请参见
https://docs.djangoproject.com/en/5.0/ref/settings/
"""


# 构建项目内的路径，例如：BASE_DIR / 'subdir'。
BASE_DIR = Path(__file__).resolve().parent.parent


# 快速启动开发设置 - 不适用于生产环境
# 请参见https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# 安全警告：在生产环境中保持用于密钥的秘密！
SECRET_KEY = "django-insecure-(t8_9k(g6%0^_6-svq(j=_6m(q7qbv#c7e+dr%9w=8ayqrb54u"

# 安全警告：在生产环境中不要开启调试！
DEBUG = True

ALLOWED_HOSTS = []


# 应用程序定义

INSTALLED_APPS = [
    "django.contrib.admin",  # Django管理后台应用
    "django.contrib.auth",  # Django认证应用
    "django.contrib.contenttypes",  # Django内容类型应用
    "django.contrib.sessions",  # Django会话应用
    "django.contrib.messages",  # Django消息应用
    "django.contrib.staticfiles",  # Django静态文件应用
    "rest_framework",  # Django REST framework
    "api",  # 自定义应用
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",  # 安全中间件
    "django.contrib.sessions.middleware.SessionMiddleware",  # 会话中间件
    "django.middleware.common.CommonMiddleware",  # 通用中间件
    "django.middleware.csrf.CsrfViewMiddleware",  # CSRF中间件
    "django.contrib.auth.middleware.AuthenticationMiddleware",  # 认证中间件
    "django.contrib.messages.middleware.MessageMiddleware",  # 消息中间件
    "django.middleware.clickjacking.XFrameOptionsMiddleware",  # 防止点击劫持中间件
]

ROOT_URLCONF = "server.urls"  # 根URL配置

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "server.wsgi.application"  # WSGI应用程序


# 数据库
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",  # SQLite数据库引擎
        "NAME": BASE_DIR / "db.sqlite3",  # 数据库文件路径
    }
}


# 密码验证
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # 用户属性相似性验证器
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # 密码最小长度验证器
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # 常见密码验证器
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # 数字密码验证器
    },
]


# 国际化
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"  # 语言代码

TIME_ZONE = "UTC"  # 时区

USE_I18N = True  # 启用国际化

USE_TZ = True  # 启用时区


# 静态文件（CSS、JavaScript、图像）
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"  # 静态文件URL

# 默认主键字段类型
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"  # 默认自动增长主键字段类型
