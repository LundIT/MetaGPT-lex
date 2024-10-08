#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/16 16:32
# @Author  : lidanyang
# @File    : __init__.py
# @Desc    :
#
# import os
# import sys
# from pathlib import Path
#
# import django
#
# LEX_APP_PACKAGE_ROOT = Path(__file__).resolve().parent.parent.as_posix()
# PROJECT_ROOT_DIR = Path(os.getcwd()).resolve()
# sys.path.append(LEX_APP_PACKAGE_ROOT)
#
# # The DJANGO_SETTINGS_MODULE has to be set to allow us to access django imports
# os.environ.setdefault(
#     "DJANGO_SETTINGS_MODULE", "lex.lex_app.settings"
# )
# os.environ.setdefault(
#     "PROJECT_ROOT", PROJECT_ROOT_DIR.as_posix()
# )
# os.environ.setdefault("LEX_APP_PACKAGE_ROOT", LEX_APP_PACKAGE_ROOT)
#
# django.setup()

from metagpt.tools.libs import (
    data_preprocess,
    feature_engineering,
    sd_engine,
    gpt_v_generator,
    web_scraping,
    email_login,
)

# from lex.lex_app.model_utils.parse_utils import ModelStructure
# from lex.lex_app.model_utils.ModelStructureBuilder import ModelStructureBuilder
# from lex.lex_app.model_utils.ModelRegistration import ModelRegistration
# from lex.lex_app.lex_models.CalculationModel import CalculationModel
# from lex.lex_app.lex_models.LexModel import LexModel
# from lex.lex_app.logging.CalculationIDs import CalculationIDs
# from lex.lex_app.logging.CalculationLog import CalculationLog
# from lex.lex_app.auth_helpers import get_tokens_and_permissions, get_user_info, resolve_user
# from lex.lex_app.LexLogger import LexLogger

_ = (
    data_preprocess,
    feature_engineering,
    sd_engine,
    gpt_v_generator,
    web_scraping,
    email_login,
    # ModelStructure,
    # ModelStructureBuilder,
    # ModelRegistration,
    # CalculationModel,
    # LexModel,
    # CalculationIDs,
    # CalculationLog,
    # get_tokens_and_permissions,
    # get_user_info,
    # resolve_user,
    # LexLogger,
)  # Avoid pre-commit error
