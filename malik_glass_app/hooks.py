from . import __version__ as app_version

app_name = "malik_glass_app"
app_title = "Malik Glass App"
app_publisher = "D-codE"
app_description = "App for Malik Glass and Interiors"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "mailtodecode@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/malik_glass_app/css/malik_glass_app.css"
# app_include_js = "/assets/malik_glass_app/js/malik_glass_app.js"

# include js, css files in header of web template
# web_include_css = "/assets/malik_glass_app/css/malik_glass_app.css"
# web_include_js = "/assets/malik_glass_app/js/malik_glass_app.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "malik_glass_app/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Quotation" : "public/js/quotation.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "malik_glass_app.install.before_install"
# after_install = "malik_glass_app.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "malik_glass_app.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"malik_glass_app.tasks.all"
# 	],
# 	"daily": [
# 		"malik_glass_app.tasks.daily"
# 	],
# 	"hourly": [
# 		"malik_glass_app.tasks.hourly"
# 	],
# 	"weekly": [
# 		"malik_glass_app.tasks.weekly"
# 	]
# 	"monthly": [
# 		"malik_glass_app.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "malik_glass_app.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "malik_glass_app.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "malik_glass_app.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"malik_glass_app.auth.validate"
# ]

fixtures = [
	{
		"dt": "Custom Field", 
		"filters":[["name", "in", [
									'Quotation Item-width',
									'Quotation Item-height',
									'Quotation Item-quantity_of_glass',
									'Quotation Item-per_sqm',
									'Quotation Item-total_sqm',
									'Quotation Item-side_w',
									'Quotation Item-side_h',
									'Quotation Item-running_meter',
									'Quotation-total_running_mtr',
									'Sales Invoice-total_running_mtr',
									'Sales Invoice Item-height',
									'Sales Invoice Item-per_sqm',
									'Sales Invoice Item-quantity_of_glass',
									'Sales Invoice Item-running_meter',
									'Sales Invoice Item-side_h',
									'Sales Invoice Item-side_w',
									'Sales Invoice Item-total_sqm',
									'Sales Invoice Item-width'

								]]]
	}
]
