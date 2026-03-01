# Copyright (c) 2026, Frappe Technologies, AgriTheory and contributors
# For license information, please see license.txt

from frappe import _


def get_data():
	return {"transactions": [{"label": _("Crop Cycle"), "items": ["Crop Cycle"]}]}
