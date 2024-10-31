class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        reply = f"Name: {self.name}" + f"\nDescription: {self.description or '-'}" + \
            f"\nLicense: {self.license or '-'}" + \
            f"\n"
        
        reply = reply + f"\nAuthors:"
        for author in self.authors:
            reply = reply + f"\n- {author}"
        reply = reply + f"\n\nDependencies:"
        for dep in self.dependencies:
            reply = reply + f"\n- {dep}"
        reply = reply + f"\n\nDevelopment dependencies:"
        for dep in self.dev_dependencies:
            reply = reply + f"\n- {dep}"
        return reply
