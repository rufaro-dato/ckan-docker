"""Tests for views.py."""

import pytest

import ckanext.rufaro.validators as validators


import ckan.plugins.toolkit as tk


@pytest.mark.ckan_config("ckan.plugins", "rufaro")
@pytest.mark.usefixtures("with_plugins")
def test_rufaro_blueprint(app, reset_db):
    resp = app.get(tk.h.url_for("rufaro.page"))
    assert resp.status_code == 200
    assert resp.body == "Hello, rufaro!"
