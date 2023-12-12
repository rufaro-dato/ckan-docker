"""Tests for helpers.py."""

import ckanext.rufaro.helpers as helpers


def test_rufaro_hello():
    assert helpers.rufaro_hello() == "Hello, rufaro!"
