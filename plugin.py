# from django.conf import settings
from saleor.plugins.base_plugin import BasePlugin, ConfigurationTypeField


class KushkiPlugin(BasePlugin):

    PLUGIN_ID = "rc.plugins.kushki"  # plugin identifier
    PLUGIN_NAME = "Kushki for Saleor"  # display name of plugin
    PLUGIN_DESCRIPTION = "Kushki Payment Gateway for Saleor."
    CONFIG_STRUCTURE = {
        "merchant_id": {
            "type": ConfigurationTypeField.STRING,
            "help_text": "Provide your Merchant ID",
            "label": "Merchant ID",
        },
        "public_key": {
            "type": ConfigurationTypeField.STRING,
            "help_text": "Provide your Public Key",
            "label": "Public Key",
        },
        "private_key": {
            "type": ConfigurationTypeField.SECRET,
            "help_text": "Provide your Private Key",
            "label": "Private Key",
        },
        "is_prod_environment": {
            "type": ConfigurationTypeField.BOOLEAN,
            "help_text": "Check if this is a production environment.",
            "label": "Is production environment?",
        }
    }
    DEFAULT_CONFIGURATION = [
        {"name": "public_key", "value": None},
        {"name": "private_key", "value": None},
        {"name": "is_prod_environment", "value": False},
    ]

    DEFAULT_ACTIVE = False

    # @classmethod
    # def validate_plugin_configuration(cls, plugin_configuration: "PluginConfiguration"):
    #     """Validate if provided configuration is correct."""
    #     missing_fields = []
    #     configuration = plugin_configuration.configuration
    #     configuration = {item["name"]: item["value"] for item in configuration}
    #     if not configuration["login"]:
    #         missing_fields.append("username or account")
    #     if not configuration["password"]:
    #         missing_fields.append("password or API token")

    #     if plugin_configuration.active and missing_fields:
    #         error_msg = (
    #             "To enable a plugin, you need to provide values for the "
    #             "following fields: "
    #         )
    #         raise ValidationError(error_msg + ", ".join(missing_fields))
        