import yaml


class Worldly:
    def __init__(self, filename="i18n.yaml"):
        with open(filename, "r") as f:
            self.messages = yaml.load(f)

        self.use_language = "en"  # default; please override

        self.config = {
                          "master_fallback": "en",
                          "fallback": {}
                      }

    def render(self, entry):
        if entry in self.messages:
            # Picking a return language: the defined language itself
            if self.use_language in self.messages[entry]:
                return_language = self.use_language
            elif self.use_language in self.config["fallback"]:
                    if self.config["fallback"][self.use_language] in self.messages[entry]:
                        return_language = self.config["fallback"][self.use_language]
            else:
                return_language = self.config["master_fallback"]

            return self.messages[entry][return_language]

        else:
            raise KeyError("Message is not defined")