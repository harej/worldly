# Worldly

Worldly is a simple module to create easily internationalizable Python code. Instead of using the gettext approach of compiled message files, Worldly reads translations defined in a YAML file, making it easy for others to contribute translations.

## The basics

Just put your messages in a YAML file (by default, in the same directory as your script, called i18n.yaml):

    "Welcome everyone!":
      en: "Welcome everyone!"
      fr: "Bienvenue tout le monde!"
      

You can use arbitrary language codes, but it is recommended you use ISO 639-1 or ISO 639-2 language codes. You can also use generic message labels or you can use the original-language message as the label, as long as it is included as one of the "translations." Note the example above: "Welcome everyone!" is specified as the English version of the message that has a label of "Welcome everyone!"

Are you used to using _() from gettext? If so, you will be able to easily adapt:

    >>> from worldly import Worldly
    >>> i18n = Worldly("i18n.yaml")
    >>> i18n.use_language = "fr"
    >>> _ = i18n.render
    >>> _("Welcome everyone!")
    'Bienvenue tout le monde!'

## Fallback languages

Worldly supports a "master fallback" language and fallbacks for individual languages through the `config` attribute:

The default:

    >>> i18n.config
    {'fallback': {}, 'master_fallback': 'en'}

The "master fallback" language is the language of last resort, when a message is translated in neither the used language nor a specific fallback language. By default this language is English, but it's easy to change:

    >>> i18n.config["master_fallback"] = "ja"

You can also use individualized fallbacks, for example to suggest a national language as a fallback to a regional language. As an example, let's have Limburgish fall back on German:

    >>> i18n.config["fallback"]["li"] = "de"
    >>> i18n.use_language = "li"
    >>> i18n.config
    {'fallback': {'li': 'de'}, 'master_fallback': 'ja'}

In this example, we have opted to use the Limburgish translations, falling back on German if Limburgish is not available. And if German is not available, it will fall back on the master fallback, which apparently is Japanese. Neat!

## More features?

This is a very new project and it is probably missing a lot! I encourage you to recommend new features.
