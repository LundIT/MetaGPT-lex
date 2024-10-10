#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/16 16:32
# @Author  : lidanyang
# @File    : __init__.py
# @Desc    :

from metagpt.tools.libs import (
    data_preprocess,
    feature_engineering,
    sd_engine,
    gpt_v_generator,
    web_scraping,
    email_login,
)

from metagpt.tools.tool_registry import register_tool


@register_tool()
def lex_app_setup():
    """
    Initializes the Django environment and sets up necessary paths for the project.

    This function performs the following tasks:
    1. Defines the paths to the application and project root directories.
       - `LEX_APP_PACKAGE_ROOT`: The parent directory of the `lex_app` package.
       - `PROJECT_ROOT_DIR`: The current working directory of the project.

    2. Adds the `LEX_APP_PACKAGE_ROOT` to the system path (`sys.path`) to ensure
       that modules from the parent package are accessible.

    3. Sets the required environment variables:
       - `DJANGO_SETTINGS_MODULE`: Specifies the settings module for the Django project.
       - `PROJECT_ROOT`: The root directory of the project.
       - `LEX_APP_PACKAGE_ROOT`: The root directory of the application package.

    4. Calls `django.setup()` to initialize the Django framework, making it possible to
       use Django ORM, models, and other features.

    Note: This script must be run in a Django-compatible environment, and
          the Django settings file must be properly configured.
    """

    import os
    import sys
    import django

    LEX_APP_PACKAGE_ROOT = "<absolute_path_of_lex_app_from_venv>" #TODO: This should be fetched programmatically
    PROJECT_ROOT_DIR = "<absolute_path_of_the_project_working_dir>" #TODO: This should be fetched programmatically
    sys.path.append(LEX_APP_PACKAGE_ROOT)

    # The DJANGO_SETTINGS_MODULE has to be set to allow us to access django imports
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "lex.lex_app.settings"
    )
    os.environ.setdefault(
        "PROJECT_ROOT", PROJECT_ROOT_DIR
    )
    os.environ.setdefault("LEX_APP_PACKAGE_ROOT", LEX_APP_PACKAGE_ROOT)

    django.setup()


_ = (
    data_preprocess,
    feature_engineering,
    sd_engine,
    gpt_v_generator,
    web_scraping,
    email_login,
    lex_app_setup
)  # Avoid pre-commit error
