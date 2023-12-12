"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.rufaro.logic import validators


def test_rufaro_reauired_with_valid_value():
    assert validators.rufaro_required("value") == "value"


def test_rufaro_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.rufaro_required(None)
