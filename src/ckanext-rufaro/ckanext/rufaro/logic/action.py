import ckan.plugins.toolkit as tk
import ckanext.rufaro.logic.schema as schema


@tk.side_effect_free
def rufaro_get_sum(context, data_dict):
    tk.check_access(
        "rufaro_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.rufaro_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'rufaro_get_sum': rufaro_get_sum,
    }
