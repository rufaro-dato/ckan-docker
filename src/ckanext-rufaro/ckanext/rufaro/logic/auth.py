import ckan.plugins.toolkit as tk


@tk.auth_allow_anonymous_access
def rufaro_get_sum(context, data_dict):
    return {"success": True}


def get_auth_functions():
    return {
        "rufaro_get_sum": rufaro_get_sum,
    }
