from mezzanine.conf import register_setting

register_setting(
    name="RICHTEXT_ALLOWED_ATTRIBUTES",
    append=('script',),
)

# register_setting(
#     name="RICHTEXT_ALLOWED_TAGS",
#     append="script",
# )